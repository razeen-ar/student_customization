from odoo import models,fields,api

class Student(models.Model):

    _name = 'student.student'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    class_ = fields.Char(string="Class")
    image  = fields.Binary(string="Image")
    status  = fields.Selection([('Waiting list', 'Waiting list'),('Admitted','Admitted')],default="Waiting list")

    def waiting(self):
        self.write({'status':'Waiting list'})

    def admit(self):
        self.write({'status':'Admitted'})