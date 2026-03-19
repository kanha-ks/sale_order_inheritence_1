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
        'views/cron.xml',
        'views/custom_sale_order_views.xml',
        'views/custom_account_move_views.xml',
        'views/sale_order_form.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'sale_order_inheritence/static/src/js/ShowCustomerInfo.js',
            'sale_order_inheritence/static/src/js/CustomerInfo.js',
            'sale_order_inheritence/static/src/widgets/customer_info_widget.xml',
        ],
    },
    'installable': True,
    'application': True,
}
