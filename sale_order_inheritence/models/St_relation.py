# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields

class TestAbstract(models.AbstractModel):

    _name = 'test.abstract'
    abstract_name = fields.Char(string="Name")
    abstract_phone_number = fields.Integer(string="Mobile Number")

class StRelation(models.Model):
    """
    StRelation : Model for showing the Many2one relationship
                    between sale.order and sale.order.st
    """
    _name = 'sale.order.st'
    _description = "Implementing _auto = false "
    _inherit = ['test.abstract']
    # _auto = False

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    name = fields.Char(string="Salesperson Name")
    total_orders = fields.Integer(string="Total Order")
    total_revenue = fields.Integer(string="Total Revenue")
    last_order_date = fields.Date(string="Last Order Date")

#     let say here i want to make some changes with it i can show the product data, sale order data only and doesn't have any relationship
#       sales person performance dashboard
#     def init(self):
#         # table = self._name.replace('.','_')
#         self.env.cr.execute(f"""  
#             CREATE OR REPLACE VIEW {self._table} AS (
#                 SELECT min(s.id) as id,
#                        p.name as name,
#                        count(s.id) as total_orders,
#                        sum(s.amount_total) as total_revenue,
#                        max(s.date_order) as last_order_date
#                        FROM sale_order s
#                 JOIN res_users u ON s.user_id = u.id
#                 JOIN res_partner p ON u.partner_id = p.id
#                 GROUP BY p.name
#             )
#         """)

