from odoo import models,fields,api
from datetime import date

class Student(models.Model):

    _name = 'student.student'

    name = fields.Char(string="Name")
    dob = fields.Date(string="Date of Birth")
    class_ = fields.Char(string="Class")
    image  = fields.Binary(string="Image")
    status  = fields.Selection([('Waiting list', 'Waiting list'),('Admitted','Admitted')],default="Waiting list")
    age = fields.Integer(compute='_compute_age', string="Age")
    birthday_message = fields.Char(compute='_compute_birthday_message', string="Birthday Message")


    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for student in self:
            if student.dob:
                dob = fields.Date.from_string(student.dob)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                student.age = age
            else:
                student.age = 0

    @api.depends('dob')
    def _compute_birthday_message(self):
        today = date.today()
        for student in self:
            if student.dob:
                dob = fields.Date.from_string(student.dob)
                if (today.month, today.day) == (dob.month, dob.day):
                    student.birthday_message = "Today is your birthday!"
                else:
                    next_birthday = date(today.year, dob.month, dob.day)
                    if today > next_birthday:
                        next_birthday = next_birthday.replace(year=today.year + 1)
                    days_remaining = (next_birthday - today).days
                    student.birthday_message = f"{days_remaining} days remaining for your birthday!"
            else:
                student.birthday_message = ""

    def waiting(self):
        self.write({'status':'Waiting list'})

    def admit(self):
        self.write({'status':'Admitted'})