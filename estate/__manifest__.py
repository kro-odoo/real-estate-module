# -*- coding: utf-8 -*-

{
    'name': "estate",
    'summary': "Real Estate advertisements",
    'category':'Real Estate/Brokerage',
    'depends':['base', 'website'],
    'data':[
        'security/ir.model.access.csv',
        'wizards/add_offer_wizard.xml',
        'views/estate_property_views.xml',
        'views/estate_property_tags_views.xml',
        'views/estate_menus.xml',
        'reports/estate_property_report.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'application':True,
}
