from odoo import api, fields, models


class AllPatientReport(models.AbstractModel):
    _name = 'report.richmond_hospital.report_all_patient_list'
    _description = 'Patient Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        if gender:
            domain += [('gender', '=', gender)]
        if age != 0:
            domain += [('age', '=', age)]
        docs = self.env['hospital.patient'].search(domain)
        return {
            'docs': docs,
            'email': 'richmond@gmail.com'
        }


# browse method for printing patient details


class PatientDetailsReport(models.AbstractModel):
    _name = 'report.richmond_hospital.report_patient_detail'
    _description = 'Patient details  Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("Test Odoo Mates", docids, data)
        docs = self.env['hospital.patient'].search([])
        return {
            'docs': docs,
        }
