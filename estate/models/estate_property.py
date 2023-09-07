# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError
from odoo.tools.float_utils import float_compare


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property Model'
    _order = 'expected_price'

    #basic fields
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    state = fields.Selection([
        ('new','New'),
        ('offer_received','offer received'),
        ('offer_accepted','offer accepted'),
        ('sold','sold'),
        ('canceled','canceled')
    ],default='new')
    active = fields.Boolean("active",default=True)

    #relational fields
    salesperson_id=fields.Many2one('res.users',string='Salesperson', default=lambda self:self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False, readonly=True)
    offer_ids=fields.One2many('estate.property.offer','property_id')
    tag_ids = fields.Many2many('estate.property.tag','property_tags_rel','tag_id','property_id', string="Tags")

    # Compute field
    best_offer = fields.Float(string="Best Offers", compute="_compute_best_offer")

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price'), default=0)

    # Actions
    def action_property_sold(self):
        self.state = 'sold'

    def action_property_cancel(self):
        self.state = 'canceled'

    def unlink(self):
        for record in self:
            if record.state != 'new' and record.state != 'canceled':
                raise UserError("Only New and Canceled Properties can be deleted!")
        return super().unlink()

     # SQL Constraints
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'The expected Price must be strictly positive!'),
        ('check_selling_price', 'CHECK(selling_price >=0)', 'The Selling Price must be positive!')
    ]

    # Python Constraints
    @api.constrains('expected_price', 'selling_price')
    def _check_expected_price(self):
        for record in self:
            if record.offer_ids and record.selling_price < record.expected_price:
                raise ValidationError("The Selling price must higher than Expected price")
