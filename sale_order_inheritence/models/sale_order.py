# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api

class SaleOrder(models.Model):
    """
    Sale Order to manage specific product metrics.

            This model inherits the basic logic of sale order to get
            the properties from sale.order module
    """
    _inherit = 'sale.order'

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------

    custom_order_line = fields.One2many('sale.order.custom.order.line', 'order_id', string="Custom Order Line")

    # -------------------------------------------------------------------------
    # ACTIONS (Wizards)
    # -------------------------------------------------------------------------

    # scheduled action
    @api.model
    def cron_auto_cancel_expired_orders(self):
        todays_date = fields.Date.today()
        expired_order = self.search([('state', '=', 'draft')])
        for each_data in expired_order:
            print(each_data)

    def action_product_confirm_wizard(self):
        lines = []
        for line in self.custom_order_line:
            lines.append((0, 0, {
                'product_id': line.product_id.id,
                'qty': line.qty,
                'unit_price': line.unit_price,
            }))
        return {
            'type': 'ir.actions.act_window',
            'name': 'Product Confirm Wizard',
            'res_model': 'product.confirm.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_order_id': self.id,
                'default_product_line_ids': lines
            }
        }

    # -------------------------------------------------------------------------
    # ACTIONS for buttons in sale order
    # -------------------------------------------------------------------------

    def action_product_create(self):
        treat_data = []
        for each_data in self.custom_order_line:
            treat_data.append((0, 0, {
                'name': each_data.product_id.name,
                'product_template_id': each_data.product_id,
                'product_uom_qty': each_data.qty,
                'price_unit': each_data.unit_price,
            }))

        self.write({
            'order_line': treat_data,
        })

    def action_product_update(self):
        #     update the price
        data = []
        for each_data in self.order_line:
            data.append((1, each_data.id, {
                'price_unit': each_data.price_unit + 2
            }))

        self.write({
            'order_line': data
        })

    def action_product_delete(self):
        data = []
        for each_data in self.order_line:
            if each_data.price_unit > 2:
                data.append((2, each_data.id, 0))

        self.write({
            'order_line': data
        })

    def action_product_unlink(self):
        data = []
        for each_data in self.order_line:
            data.append((3, each_data.id))  # for every data ham ye kar rhe h

        self.write({
            'order_line': data
        })

    def action_product_clear_all(self, passed=False):
        """
            Params
            passed: Boolean
            return: bool
        """
        self.write({
            'order_line': [(5, 0, 0)]
        })
