from odoo import models,fields,api,_

class SchoolInformation(models.Model):
    _name = 'school.information'
    _description = 'School Information'

    name = fields.Char(string = 'Name', required = True)
    type = fields.Selection([
        ('private','private'),
        ('public','public'),
    ],default='public',string='Loại trường')
    email = fields.Text(string = 'Email')
    address = fields.Text(string = 'Address')

    phoneNu = fields.Char(string= 'Số điện thoại')
    hasOnlineClass = fields.Boolean(string= 'Có lớp online k')
    rank = fields.Integer(string ='Xếp hạng')
    establishDay = fields.Date(string= 'Ngày thành lập')
    document = fields.Binary(string= 'Tài liệu',attachment=True)
    document_name = fields.Char(string= 'Tên tài liệu')
    class_list = fields.One2many('class.infor', 'school_id', string = 'List Class')
    tuition = fields.Float(compute ='compute_tuition',string = 'Tuition')

    @api.depends('type')
    def compute_tuition(self):
        for r in self:
            if r.type == 'private':
                r.tuition =2000
            elif r.type == 'public':
                r.tuition = 500