# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Roxane Sancho y Fran",
    'website': "http://www.sanchoyfran.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
