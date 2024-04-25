from django.db import models as md


class StudentDeserter(md.Model):
    class Meta:
        db_table = 'students_deserters'


class StudentWithdrawn(md.Model):
    class Meta:
        db_table = 'students_withdrawn'