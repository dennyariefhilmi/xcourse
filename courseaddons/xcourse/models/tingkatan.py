from odoo import fields, models, api


class tingkatan(models.Model):
    _name = 'xcourse.tingkatan'
    _description = 'Description'

    name = fields.Selection(string='Jenis Tingkatan',
                            selection=[('pemula','Pemula'),
                                       ('menengah','Menengah'),
                                       ('lanjut','Lanjut')])
    keterangan = fields.Char(string='Keterangan')
    biaya = fields.Integer(string='Biaya',
                           required=True)

    tingkat_ids = fields.One2many(comodel_name='xcourse.category',
                                  inverse_name='tingkatan',
                                  string='Id tingkatan',
                                  required=False)
