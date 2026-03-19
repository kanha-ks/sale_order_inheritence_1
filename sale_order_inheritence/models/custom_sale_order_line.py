# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api


class CustomSaleOrderLine(models.Model):
    """
    Custom Sale Order Line to manage specific product metrics.

        This model extends the basic logic of order lines to calculate
        taxes and amounts based on custom triggers.
    """
    _name = "sale.order.custom.order.line"
    _description = "Custom sale order line field"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    product_id = fields.Many2one('product.product', string="Product")

    qty = fields.Float(string="Quantity", default=1.0)
    delivered = fields.Float(string="Delivered")
    invoiced = fields.Float(string="Invoiced")
    unit_price = fields.Float(string="Unit Price")

    tax = fields.Many2many('account.tax',string="Taxes")
    amount = fields.Float(compute="_calculate_amounts", string="Amount")

    order_id = fields.Many2one('sale.order', string="Order ID")

    # -------------------------------------------------------------------------
    # COMPUTE METHODS
    # -------------------------------------------------------------------------
    @api.depends('qty')
    def _calculate_amounts(self):
        # functionality
        for each in self:
            subtotal = each.qty * each.unit_price
            each.amount = subtotal

    # -------------------------------------------------------------------------
    # ONCHANGE METHODS
    # -------------------------------------------------------------------------
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.unit_price = self.product_id.lst_price
