from django.db import models as md


class StudentGraduate(md.Model):
    class Meta:
        db_table = 'student_graduate'


class StudentGraduateJobs(md.Model):
    class Meta:
        db_table = 'student_graduate_jobs'


class StudentGraduateAct(md.Model):
    class Meta:
        db_table = 'student_graduate_act'