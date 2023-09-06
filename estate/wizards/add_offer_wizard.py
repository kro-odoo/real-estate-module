from odoo import models,fields

class estate_property_wizard(models.TransientModel):
    _name = "estate.property.wizard"

    amount = fields.Float(string="Amount")
    partner_id=fields.Many2one("res.partner")

    def add_offers(self):
        selected_properties=self.env.context.get('active_ids',[])
        for active_id in selected_properties:
                offer=self.env['estate.property.offer'].create({
                'property_id':active_id,
                'price':self.amount,
                'partner_id':self.partner_id.id,
            })
        return offer
