from django.db import models as md


class Students(md.Model):
    class Meta:
        db_table = 'students'
        
        
class StudentPhones(md.Model):
    class Meta:
        db_table = 'students_phones'
        
        
class StudentContact(md.Model):
    class Meta:
        db_table = 'student_contact'
        
        
class Gender(md.Model):
    class Meta:
        db_table = 'genders'
