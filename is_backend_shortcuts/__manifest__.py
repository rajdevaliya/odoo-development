# -*- coding: utf-8 -*-

{
    'name': 'Backend Shortcuts',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'author': 'InTechual Solutions',
    'license': 'OPL-1',
    'summary': 'Backend Shortcuts',
    'description': """
Jump to specific action using predefined routes/controllers
""",
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/backend_shortcuts.xml',
        'views/ir_actions_views.xml',
    ],
    'images': ['static/description/main_screenshot.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 1,
    'currency': 'EUR',
    'price': 0,
}
