# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Order Inheritance',
    'author': 'John Doe',
    'version': '1.0',
    'depends': ['sale', 'product'],
    'sequence': 1,
    'data': [
        'security/ir.model.access.csv',
        'wizards/products_confirmation_wizards.xml',
        # 'views/sale_management_performance_menus.xml',
        'views/cron.xml',
        'views/custom_sale_order_views.xml'
    ],
    'installable': True,
    'application': True,
}
