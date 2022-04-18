from odoo import api, fields, models
class SaleOrder(models.Model):

    _inherit = "sale.order"

    sale_description = fields.Text(string='Sale Description')
    sale_location = fields.Text(string='Sale Location')

