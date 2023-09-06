# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property model'
    _order = 'expected_price'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    state=fields.Selection([
        ('new','New'),
        ('offer_received','offer received'),
        ('offer_accepted','offer accepted'),
        ('sold','sold'),('canceled','canceled')
    ],copy=False,default='new')
    active=fields.Boolean("active",default=True)

    #relational fields
    salesperson_id=fields.Many2one('res.users',string='salesperson', default=lambda self:self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False, readonly=True)
    offer_ids=fields.One2many('estate.property.offer','property_id')
    tag_ids = fields.Many2many('estate.property.tag','property_tags_rel','tag_id','property_id', string="Tags")

    #computed Fields
    best_offer = fields.Float(compute="_compute_best_offer", default=0)

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price'), default=0)

    # SQL Constraints
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'The expected Price must be strictly positive!'),
        ('check_selling_price', 'CHECK(selling_price >=0)', 'The Selling Price must be positive!')
    ]

    # Python Constraints
    @api.constrains('expected_price', 'selling_price')
    def _check_expected_price(self):
        for record in self:
            if not float_is_zero(record.selling_price, precision_digits = 2) and float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
                raise ValidationError("The selling price must be 90 % of Expected Price")

    # Action Methods
    def action_property_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Canceled Properties cannot be sold")
            record.state = 'sold'
        return True

    def action_property_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold Properties cannot be canceled")
            record.state = 'canceled'
        return True

    @api.ondelete(at_uninstall=False)
    def _prevent_deletion(self):
        for record in self:
            if record.state != 'new' and record.state != 'canceled':
                raise UserError("Only New and Canceled Properties can be deleted!")
