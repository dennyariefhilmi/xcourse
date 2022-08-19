from odoo import fields, models, api


class Peserta(models.Model):
    _inherit = 'res.partner'
    _description = 'Description'

    jenis_kursus = fields.Selection(selection=[('pemrograman', 'Pemrograman'),
                                               ('bahasa','Bahasa'),
                                               ('keterampilan', 'Keterampilan')],
                                    string="jenis_kursus",
                                    required=False)
    is_peserta = fields.Boolean(string='Peserta',
                                required=False)

