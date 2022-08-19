from odoo import fields, models, api


class CourseCategory(models.Model):
    _name = 'xcourse.category'
    _description = 'Nama Kategori Course'

    name = fields.Char(string='Kategori Kursus')
    kapasitas_kelas = fields.Integer(
        string='Kapasitas Kelas',
        required=True)

    tingkatan = fields.Many2one(
        comodel_name='xcourse.tingkatan',
        string='Level Belajar',
        required=True)

    biaya = fields.Integer(compute='_compute_biaya',
                           string='Biaya',
                           required=False)

    @api.depends('tingkatan')
    def _compute_biaya(self):
        for a in self:
            a.biaya = a.tingkatan.biaya


class Pemrograman(models.Model):
    _inherit = 'xcourse.category'
    _name = 'xcourse.pemrograman'
    _description = 'ini kelas pemrograman'

    jml_siswa_prog = fields.Integer(string='Jml_siswa_prog',
                                    required=False)
    kapasitas_sisa = fields.Integer(compute='_compute_sisa',
                                    string='Sisa Kapasitas',
                                    required=False)

    @api.depends('jml_siswa_prog')
    def _compute_sisa(self):
        for record in self:
            record.kapasitas_sisa = record.kapasitas_kelas - record.jml_siswa_prog


class Bahasa(models.Model):
    _inherit = 'xcourse.category'
    _name = 'xcourse.bahasa'
    _description = 'ini kelas bahasa'
    jml_siswa_bahasa = fields.Integer(string='Jml_siswa_bahasa',
                                      required=False)
    kapasitas_sisa = fields.Integer(compute='_compute_sisa',
                                    string='Sisa Kapasitas',
                                    required=False)

    @api.depends('jml_siswa_bahasa')
    def _compute_sisa(self):
        for record in self:
            record.kapasitas_sisa = record.kapasitas_kelas - record.jml_siswa_bahasa

class Keterampilan(models.Model):
    _inherit = 'xcourse.category'
    _name = 'xcourse.keterampilan'
    _description = 'ini kelas keterampilan'
    jml_siswa_ket = fields.Integer(string='Jml_siswa_ket',
                                      required=False)
    kapasitas_sisa = fields.Integer(compute='_compute_sisa',
                                    string='Sisa Kapasitas',
                                    required=False)

    @api.depends('jml_siswa_ket')
    def _compute_sisa(self):
        for record in self:
            record.kapasitas_sisa = record.kapasitas_kelas - record.jml_siswa_ket


