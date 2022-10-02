# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Order Delivery Charges',
    'version' : '15.0.0',
    'summary': 'Delivery Charges',
    'sequence': 10,
    'description': """
        Add a field in sale order and value in should be added as new sale oderline and invisible from view

    """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : ['sale'],
    'data': [
        'views/so_delivery_charge.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web._assets_primary_variables': [
        ],
        'web.assets_backend': [

        ],
        'web.assets_frontend': [
        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
        ],
    },
    'license': 'LGPL-3',
}
