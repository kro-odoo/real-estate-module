# -*- coding: utf-8 -*-

from odoo import fields,models

class resUsers(models.Model):
	_inherit = 'res.users'
	
	property_ids=fields.One2many("estate.property","salesperson_id")
