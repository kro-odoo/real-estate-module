# -*- coding: utf-8 -*-

from odoo import fields,models

class estatePropertyOffer(models.Model):
	_name = 'estate.property.offer'

	price = fields.Float(string='Price',required=True)
	status = fields.Selection(
		selection=[
			('accepted', 'Accepted'),
			('refused', 'Refused')
	],string="Status")
	partner_id = fields.Many2one('res.partner',required=True)
	property_id = fields.Many2one('estate.property', required=True)

	#Actions
	def action_offer_accepted(self):
		self.status = 'accepted'
		self.property_id.state = 'offer_accepted'
		self.property_id.buyer_id = self.partner_id
		self.property_id.selling_price = self.price

	def action_offer_rejected(self):
		self.status = 'refused'
