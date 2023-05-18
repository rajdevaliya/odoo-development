# -*- coding: utf-8 -*-
{
    'name': "is_dropzone",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/dropzone_files_menu.xml',
        'views/dropzone.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'is_dropzone/static/src/js/dropzone_view.js',
            'is_dropzone/static/src/js/audio_control_widget.js',
            'is_dropzone/static/src/css/audio_control_widget.css',
        ],
        'web.assets_qweb': [
            'is_dropzone/static/src/xml/dropzone_template.xml',
            'is_dropzone/static/src/xml/audio_control_widget.xml',
        ],
    },
}
