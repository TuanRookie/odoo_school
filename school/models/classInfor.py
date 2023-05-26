from odoo import models,fields,api,_

class ClassInfor(models.Model):
    _name = 'class.infor'
    _description = 'Class Management'

    name = fields.Char(string = 'Name', required = True)
    grade = fields.Char(string = 'Grade')
    mainTeacher = fields.Char(string = 'Teacher')
    school_id = fields.Many2one('school.information' ,string = 'School')

    # address = fields.Text(related = 'school_id.address',string = 'Address School', store =True)

