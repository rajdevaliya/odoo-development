# -*- coding: utf-8 -*-
{
    'name': "civil_hospital",

    'summary': """
        Welcome to Hospital aanagement system""",

    'description': """
 MISSION
Mission
Since its inception in the year 1841, Civil Hospital is devoted to the mission of “Providing the best healthcare services to all the sections of society at free of cost through unrelenting strategy of motivation, quality improvement, value addition and dedication towards humanity with selflessness.”    """,

    'author': "Department of Health, Government of Gujarat",
    'website': "https://civilhospitalahd.gujarat.gov.in",
    'auto_install': False,
    'application': True,
    'sequence': -500,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'is_visa_processing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product', 'sale', 'sale_crm'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/tag_patient_data.xml',
        'data/sequence_data.xml',
        'data/tag.patient.csv',
        'views/patient_view.xml',
        'wizard/cancel_appointment_view.xml',
        'views/tag_patient_view.xml',
        'views/operation_view.xml',
        'views/appointment_view.xml',
        'views/res_config_settings_views.xml',
        'views/inherit_model_view.xml',
        'views/female_patient_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
