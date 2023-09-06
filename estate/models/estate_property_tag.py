# -*- coding: utf-8 -*-

from odoo import models, fields

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Consists Property Tags"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()
