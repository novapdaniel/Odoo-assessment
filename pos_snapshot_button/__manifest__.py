# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Point of sale Snapshot Button',
    'version' : '15.0.0',
    'summary': 'Point of sale Snapshot Button',
    'sequence': 10,
    'description': """
        Add a Snapshot Button in point of sale Numpad

    """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : ['sale','point_of_sale'],
    'data': [

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
            'pos_snapshot_buttons/static/src/js/pos_snap_button.js’,'

        ],
        'web.assets_frontend': [
        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
            'pos_snapshot_button/static/xml/pos_snap.xml'
        ],
    },
    'license': 'LGPL-3',
}
