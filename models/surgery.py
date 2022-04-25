from odoo import api, fields, models, _


class HospitalSurgery(models.Model):
    _name = "hospital.surgery"
    _description = "Surgery Lab"

    name = fields.Char(string='name')
    note = fields.Text(string='Details')
    base_condition = fields.Char(string='Base Condition')
    surgery = fields.Selection(string='Surgery Classification',
                               selection=[('required', 'Required'), ('not_required', 'Not Required')])
    date = fields.Date(string='Date Of Surgery', default=fields.Date.context_today)
    age = fields.Integer(string='Patient Age')
    checkup_time = fields.Datetime(string='Checkup Time', default=fields.Datetime.now)
