from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "patient.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Appointment of Patients"
    _rec_name = "doctor_id"
    _order = 'id desc'

    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        required=True)
    patient_name_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient Name',
        required=False)
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
    doctor_id = fields.Many2one('doctors.hospital', string="Doctor", required=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking=True)
    state = fields.Selection([('draft', "Draft"), ('confirm', "Confirmed"), ('done', "Done"), ('cancel', "Cancelled")],
                             default='draft', string='Status', tracking=True)
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string='Date')
    date_checkup = fields.Datetime(string='Checkup Time')
    prescription = fields.Text(string="Prescription")
    prescription_line_ids = fields.One2many(
        comodel_name='appointment.prescription.lines', inverse_name='appointment_id',
        string='Prescription Line')

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
            else:
                self.gender = ''
                self.note = ''
# overriding method of delete(unlink)

    def unlink(self):
        if self.state == 'done':
            raise ValidationError(_("You Cannot Delete %s as it is in Done State % self.name"))
        return super(HospitalAppointment, self).unlink()

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://apps.odoo.com/apps',
        }


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines"


    medicine = fields.Char(
    string='Medicine',
    required=False)
    quantity = fields.Integer(
    string='Quantity',
    required=False)
    appointment_id = fields.Many2one('patient.appointment', string='Appointment')
