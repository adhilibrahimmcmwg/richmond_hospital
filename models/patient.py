from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _order = 'id asc'

# overriding method
    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['gender'] = 'male'
        return res

    name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    age = fields.Integer(string='Age', tracking=True)

    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking=True
    )

    note = fields.Text(string='Description')
    state = fields.Selection([('draft', "Draft"), ('confirm', "Confirmed"), ('done', "Done"), ('cancel', "Cancelled")],
                             default='draft', string='Status', tracking=True)

    responsible_id = fields.Many2one('res.partner', string='Responsible')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    image = fields.Binary(string="Patient Image")
    appointment_ids = fields.One2many('patient.appointment', 'patient_id', string='Appointments')

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['patient.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count

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
        res = super(HospitalPatient, self).create(vals)
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if patients:
                raise ValidationError(_("Name %s Already Exists" % rec.name))

    @api.constrains('name')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_("Age Cannot be Zero...!!!"))

    def name_get(self):
        result = []
        for rec in self:
            if not self.env.context.get('hide_code'):
                name = '[' + rec.reference + ']' + rec.name
            else:
                name = rec.name
            result.append((rec.id, name))
        return result

    def action_open_appointments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Appointment'),
            'res_model': 'patient.appointment',
            'domain': [('patient_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': '',
        }