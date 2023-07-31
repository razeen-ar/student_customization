from odoo import models,fields,api

class Student(models.Model):

    _name = 'student.student'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    class_ = fields.Char(string="Class")