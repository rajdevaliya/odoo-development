# -*- coding: utf-8 -*-
{
    'name': "customer_hierachy_chart",

    'summary': """
        To group the branch company as per parent company""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",
    'category': 'customer segmentation',
    'version': '0.1',
    'depends': ['base', 'mail', 'contacts', 'sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/customer_hierarchy_chart.xml',
    ],
    'auto_install': False,
    'application': True,
    'sequence': -500,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'customer_hierachy_chart/static/src/js/partner_tree.js'
    #     ]
    # },
}
