# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management  Software',
    'sequence': 2,
    'description': """ Hospital Management Software
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.richmond.hospital.com',
    'license': 'LGPL-3',

    'depends': ['sale', 'mail', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        "wizard/appointment_wizard_view.xml",
        "wizard/search_appointment_wizard.xml",
        "wizard/appointment_pdf_report_wizard.xml",
        "wizard/all_patient_report_view.xml",
        "views/patient_view.xml",
        "views/kids_view.xml",
        "views/patient_gender_view.xml",
        "views/appointment_view.xml",
        "views/sale_inherit.xml",
        "views/partner.xml",
        "views/doctors.xml",
        "views/nurse.xml",
        "views/lab.xml",
        "views/surgery.xml",
        "report/patient_details.xml",
        "report/patient_card.xml",
        "report/report.xml",
        "report/appointment_details.xml",
        "report/all_patients_list.xml",
    ],

    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
