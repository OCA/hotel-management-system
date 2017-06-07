# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Hotel Management Base',
    'version' : '10.0.1.0.0',
    'author' : '''Tiny, Odoo Community Association (OCA), Serpent Consulting
                Services Pvt. Ltd.''',
    'category' : 'Generic Modules/Hotel Management',
    'license' : 'AGPL-3',
    'description' : '''
        Module for Hotel/Resort/Rooms/Property management. You can manage:
            * Configure Property
            * Hotel Configuration
            * Check In, Check out
            * Manage Folio
            * Payment
        Different reports are also provided, mainly for hotel statistics.
    ''',
    'depends' : ['sale_stock', 'point_of_sale', 'report'],
    'demo': ['views/hotel_data.xml'],
    'data': [
            'security/hotel_security.xml',
            'security/ir.model.access.csv',
            'views/hotel_sequence.xml',
            'views/hotel_report.xml',
            'views/report_hotel_management.xml',
            'views/hotel_view.xml',
            'wizard/hotel_wizard.xml',
    ],
    'css': ['static/src/css/room_kanban.css'],
    'auto_install' : False,
    'installable' : True,
    'application' : True,
}
