from odoo import api, fields, models, _


class SearchAppointmentWizard(models.TransientModel):
    _name = "search.appointment.wizard"
    _description = "Search Appointment"

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        required=True)

    def action_search_appointment_m1(self):
        action = self.env.ref('richmond_hospital.appointment_hospital_action').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

    def action_search_appointment_m2(self):
        action = self.env['ir.actions.actions']._for_xml_id("richmond_hospital.appointment_hospital_action")
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

    def action_search_appointment_m3(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Appointment'),
            'res_model': 'patient.appointment',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_mode': 'tree,form',
            'target': 'new',
        }
        return action


