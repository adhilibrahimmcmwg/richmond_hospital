from odoo import api, fields, models, _


class HospitalLab(models.Model):
    _name = "hospital.lab"
    _description = "Laboratory"
    _rec_name = 'doctor_id'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    note = fields.Text(strig="Address")
    doctor_id = fields.Many2one('doctors.hospital', string="Doctor")
    nurse_id = fields.Many2one('nurse.hospital', string="Nurse")
    test_type = fields.Selection(
        string='Test Type',
        selection=[('antigen', 'Antigen'), ('rtpcr', 'RTPCR')]
    )
    appointment_ids = fields.One2many('patient.appointment', 'doctor_id', string='Appointments')
