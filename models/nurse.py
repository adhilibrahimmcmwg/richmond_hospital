from odoo import api, fields, models, _


class HospitalNurse(models.Model):
    _name = "nurse.hospital"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Nurse"

    nurse_name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    gmail_id = fields.Char(string='Gmail')
    age = fields.Integer(string='Age', tracking=True, copy=False)
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking=True
    )
    note = fields.Text(string='Description')
    image = fields.Binary(string="Nurse Image")
    active = fields.Boolean(string="Active", default=True)
