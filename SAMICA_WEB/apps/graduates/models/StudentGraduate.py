from django.db import models as md

class StudentGraduate(md.Model):
    """
    Esta clase pertenece al modelo de la tabla de estudiantes graduados dentro del sistema
    """
    class Meta:
        db_table = 'student_graduate'


class StudentGraduateJobs(md.Model):
    class Meta:
        db_table = 'student_graduate_jobs'


class StudentGraduateAct(md.Model):
    class Meta:
        db_table = 'student_graduate_act'