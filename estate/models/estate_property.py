# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
