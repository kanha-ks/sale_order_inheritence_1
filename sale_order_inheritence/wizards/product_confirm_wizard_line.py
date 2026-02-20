from odoo import models, fields


class ProductConfirmWizardLine(models.TransientModel):
    """
    Transient model for displaying product lines within the confirmation wizard.

        This model stores temporary data to be reviewed by the user before
        it is processed and converted into permanent Sale Order Lines.
    """
    _name = "product.confirm.wizard.line"
    _description = "Wizards Child"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    wizard_id = fields.Many2one('product.confirm.wizard', string="Wizard")

    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string="Quantity", default=1.0, readonly=True)
    unit_price = fields.Float(string="Unit Price", readonly=True)
