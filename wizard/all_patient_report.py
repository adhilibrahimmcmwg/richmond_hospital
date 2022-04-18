from odoo import api, fields, models, _


class PatientReportWizard(models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Print patient Wizard"

    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking=True
    )
    age = fields.Integer(string='Age', tracking=True)

    def action_print_report(self):
        data = {
            'form_data': self.read()[0],
        }
        return self.env.ref('richmond_hospital.action_report_all_patient_details').report_action(self, data=data)
