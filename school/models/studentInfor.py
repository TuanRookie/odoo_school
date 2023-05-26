from odoo import models,fields,api,_
from odoo.exceptions import UserError

class StudentInfor(models.Model):
    _name = 'student.infor'
    _description = 'student Management'

    name = fields.Char(string = 'Name', required = True)
    birthday = fields.Date(string = 'Birthday',required = True)
    class_id = fields.Many2one('class.infor' ,string = 'Class',required = True)
    school_id = fields.Many2one('school.information',string = 'School')

    subject_list = fields.Many2many('subject.infor', 'relation_subject_student',
                                    'student_id', 'subject_id',string = 'QH Student and Subject')
    currency_id = fields.Many2one('res.currency',string = 'Đơn vị')
    tuition = fields.Monetary(string = 'Tổng học Phí',compute = 'compute_tuition')
    fee_per_semester = fields.Float(related= 'school_id.tuition',string = 'Tuition one year')
    semester = fields.Integer(string = 'So ki',compute='compute_semester')
    grade = fields.Char(related= 'class_id.grade',string ='grade')

    @api.depends('grade')
    def compute_semester(self):
        for r in self:
            if r.grade ==10:
                r.semester = 2
            elif r.grade ==11:
                r.semester = 4
            else:
                r.semester=6

    @api.depends('semester','fee_per_semester')
    def compute_tuition(self):
        for r in self:
            r.tuition = r.semester * r.fee_per_semester

    def write(self,vals):
        rth = super(StudentInfor,self).write(vals)
        if not self.subject_list:
            raise UserError("Bạn cần chọn môn học")
        return rth


class ClassInfor(models.Model):
    _inherit = 'class.infor'

    student_list = fields.One2many('student.infor', 'class_id', string = 'List Student')

class SubjectInfor(models.Model):
    _name = 'subject.infor'
    _description = 'subject Management'

    name = fields.Char(string = 'Name', required = True)
    author = fields.Char(string = 'Author', required = True)