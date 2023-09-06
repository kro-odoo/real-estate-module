# -*- coding: utf-8 -*-

from odoo import models, fields

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tags"

    name = fields.Char(required=True)
    color = fields.Integer()
