# -*- coding: utf-8 -*-

from odoo import http

class Properties(http.Controller):
    @http.route('/estate', website=True)
    def description(self):
        properties = http.request.env['estate.property'].search([])
        return http.request.render('estate.index', {
            'properties': properties
        })
