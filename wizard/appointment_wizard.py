from odoo import api, fields, models, _


class AppointmentWizard(models.TransientModel):
    _name = "appointment.wizard"
    _description = "Create Appointment"

    date = fields.Date(string='Date')
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        required=False)
    doctor_id = fields.Many2one('doctors.hospital', string="Doctor", required=True)

# create button in wizard and view records
    def action_create_appointment(self):
        print("Button Clicked!!!!!!!!!!!")
        vals = {
            'doctor_id': self.doctor_id.id,
            'patient_id': self.patient_id.id,
            'date_appointment': self.date
        }
        appointment_rec = self.env['patient.appointment'].create(vals)
        print("appointment", appointment_rec.id)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'patient.appointment',
            'res_id': appointment_rec.id,
            'target': 'new',
        }
# view appointment button and return

    def action_view_appointment(self):
        action = self.env.ref('richmond_hospital.appointment_hospital_action').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action
