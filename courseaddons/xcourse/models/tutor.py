from odoo import api, fields, models


class Tutor (models.Model):
    _inherit = 'res.partner'
    _description = 'Pengajar'

    is_tutor = fields.Boolean(string='Tutor',
                              required=False)
    is_admin = fields.Boolean(string='Admin',
                              required=False)