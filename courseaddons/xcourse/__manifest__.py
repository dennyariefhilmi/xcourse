# -*- coding: utf-8 -*-
{
    'name': "XCourse",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Denny",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/category_view.xml',
        'views/bahasa_view.xml',
        'views/peserta_view.xml',
        'views/tingkatan_view.xml',
        'views/tutor_view.xml',
        'views/session_view.xml',
        'views/session_bahasa_view.xml',
        'views/session_keterampilan_view.xml',
        'views/keterampilan_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
