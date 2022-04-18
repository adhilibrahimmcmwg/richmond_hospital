from odoo import api, fields, models

from odoo import models
import base64
import io


class PatientAppointmentXls(models.AbstractModel):
    _name = 'report.richmond_hospital.report_patient_appointment_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        print("xls...................", data['appointments'])

        sheet = workbook.add_worksheet('Appointments')
        bold = workbook.add_format({'bold': True})
        sheet.set_column('D:D', 10)
        sheet.set_column('E:E', 22)
        row = 3
        col = 3
        sheet.write(row, col, 'Reference:', bold)
        sheet.write(row, col + 1, 'Patient Name:', bold)
        for appointment in data['appointments']:
            # row = row + 1
            row += 1
            sheet.write(row, col, appointment['reference'])
            sheet.write(row, col + 1, appointment['name'])
