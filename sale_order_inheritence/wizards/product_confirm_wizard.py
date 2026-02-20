from odoo import models, fields, api


class ProductConfirmWizard(models.TransientModel):
    """
    Wizard to confirm and create Sale Order Lines from custom data.

        This wizard acts as an intermediary step to allow users to review
        product data before final insertion into the sale order.
    """
    _name = 'product.confirm.wizard'
    _description = 'Wizard showing while saving product'

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------

    order_id = fields.Many2one(
        'sale.order',
        string="Order ID",
        readonly=True
    )

    product_line_ids = fields.One2many(
        'product.confirm.wizard.line',
        'wizard_id',
        string="Products"
    )

    # -------------------------------------------------------------------------
    # ACTIONS
    # -------------------------------------------------------------------------

    def action_save(self):
        for each_product in self.product_line_ids:
            self.env['sale.order.line'].create({
                'name': each_product.product_id.name,
                'product_template_id': each_product.product_id,
                'product_uom_qty': each_product.qty,
                'price_unit': each_product.unit_price
            })
        return {
            'type': 'ir.actions.act_window_close'
        }

    def action_close(self):
        return {
            'type': 'ir.actions.act_window_close'
        }
