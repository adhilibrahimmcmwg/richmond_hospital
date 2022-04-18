from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = "doctors.hospital"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Doctors"
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True, copy=False)
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking=True
    )
    note = fields.Text(string='Description')
    image = fields.Binary(string="Patient Image")
    active = fields.Boolean(string="Active", default=True)

# overriding of copy function
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('doctor_name'):
            default['doctor_name'] = _("%s (Copy)", self.doctor_name)
        default['note'] = "Copied Record"
        return super(HospitalPatient, self).copy(default)

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['patient.appointment'].search_count([('doctor_id', '=', rec.id)])
            rec.appointment_count = appointment_count