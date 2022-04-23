from odoo import api, fields, models, _


class HospitalLab(models.Model):
    _name = "hospital.lab"
    _description = "Laboratory"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking=True
    )
    note = fields.Text(string='Address')
    test_type = fields.Selection(
        string='Test Type',
        selection=[('antigen', 'Antigen'), ('rtpcr', 'RTPCR')]
    )
    number = fields.Integer(string="Contact Number")
