from odoo import fields, models, api


class Session(models.Model):
    _name = 'xcourse.session'
    _description = 'Description'
    name = fields.Char(string='Nama')

    nama_kursus = fields.Many2one(
        comodel_name='xcourse.pemrograman',
        string='Nama Kursus',
        required=False)
    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama_tutor',
        required=False,
        domain=[('function', '=', 'Tutor Pemrograman')])

    tgl_mulai = fields.Datetime(
        string='Tgl Mulai',
        required=False,
        default=fields.Datetime.now())

    peserta_ids = fields.One2many(
        comodel_name='xcourse.pesertapemrograman',
        inverse_name='session_id',
        string='Peserta',
        required=False)
    jml_siswa = fields.Integer(
        compute='_compute_peserta',
        string='Jml Siswa',
        required=False)

    @api.model
    def _compute_peserta(self):
        for record in self:
            a = self.env['xcourse.pesertapemrograman'].search([('session_id', '=', record.id)]).mapped(
                'display_name')
            b = len(a)
            record.jml_siswa = b
            record.nama_kursus.jml_siswa_prog = b

class PesertaPemrograman(models.Model):
    _name = 'xcourse.pesertapemrograman'
    _description = 'Peserta Pemrograman'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Pemrograman',
        required=False,
        domain=[('is_peserta', '=', True), ('jenis_kursus', '=', 'pemrograman')])
    session_id = fields.Many2one(
        comodel_name = 'xcourse.session',
        string='Session_id',
        required=False)



