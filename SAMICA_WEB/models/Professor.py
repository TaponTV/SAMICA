from django.db import models as md


class Professor(md.Model):
    class Meta:
        db_table = 'professors'


class ProfessorSubject(md.Model):
    class Meta:
        db_table = 'professor_relation_subject'