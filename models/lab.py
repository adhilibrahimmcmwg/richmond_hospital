from odoo import api, fields, models, _


class HospitalLab(models.Model):
    _name = "hospital.lab"
    _description = "Laboratory"
    _rec_name = 'doctor_id'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    doctor_id = fields.Many2one('doctors.hospital', string="Doctor")
    nurse_id = fields.Many2one('nurse.hospital', string="Nurse")
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
