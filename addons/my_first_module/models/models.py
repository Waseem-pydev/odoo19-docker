from odoo import fields,models

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Information'
    student_id = fields.Char(string='Student ID')
    name = fields.Char(string='Name')
    image = fields.Binary(string='image')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('female','Female'),
        ('male','Male'),
        ('other','Other')
    ],string='Gender')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    admission_date = fields.Date(string='Admission Date')
    age = fields.Integer(string='Age')
    course = fields.Char(string='Course')
    fees = fields.Float(string='Fees')