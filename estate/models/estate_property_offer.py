# -*- coding: utf-8 -*-

from odoo import fields,models

class estatePropertyOffer(models.Model):
	_name = 'estate.property.offer'

	price=fields.Float(string='price',required=True)
	status = fields.Selection(
		string="Status",
		selection=[
			('accepted', 'Accepted'),
			('refused', 'Refused')],
        copy=False)
	partner_id=fields.Many2one('res.partner',required=True)
	property_id = fields.Many2one('estate.property', required=True)
