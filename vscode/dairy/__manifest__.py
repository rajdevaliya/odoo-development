# -*- coding: utf-8 -*-

{
    'name': 'Dairy',
    'version': '1.0.0',
    'summary': 'second module of dairy',
    'sequence': 1,
    'description': """This is a second Dairy Shop""",
    'category': '',
    'author': "Intechual Solutions",
    'website': '',
    'images': [],
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/seller_view.xml',
        'views/template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'dairy/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
