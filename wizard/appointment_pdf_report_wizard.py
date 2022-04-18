from odoo import api, fields, models, _


class AppointmentReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Appointment Wizard"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_print_excel_report(self):

        domain = []

        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_appointment', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_appointment', '<=', date_to)]
            print("Excel Print", domain)

        appointments = self.env['patient.appointment'].search_read(domain)
        data = {
            'appointments': appointments,
            'form_data': self.read()[0]
        }
        return self.env.ref('richmond_hospital.action_patient_appointment_xlsx').report_action(self, data=data)

    def action_print_report(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_appointment', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_appointment', '<=', date_to)]
        appointments = self.env['patient.appointment'].search_read(domain)
        data = {
            'form_data': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('richmond_hospital.action_report_appointment').report_action(self, data=data)
