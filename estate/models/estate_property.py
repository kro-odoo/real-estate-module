# -*- coding: utf-8 -*-

from odoo import models, fields


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property Model'
    _order = 'expected_price'

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
