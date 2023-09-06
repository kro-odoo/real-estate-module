# -*- coding: utf-8 -*-

from odoo import fields,models
from odoo.exceptions import UserError

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

	def action_offer_rejected(self):
		for record in self:
			record.status = 'refused'
		return True

	def action_offer_accepted(self):
		if 'accepted' in self.mapped("property_id.offer_ids.status"):
			raise UserError("Cannot Accept Offers from Multiple Properties!!")
		else:
			for record in self:
				record.status = 'accepted'
				record.property_id.selling_price = record.price
				record.property_id.buyer_id = record.partner_id
				record.property_id.state = 'offer_accepted'
		return True
