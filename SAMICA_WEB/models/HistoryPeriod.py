from django.db import models as md


class PeriodHistory(md.Model):
    class Meta:
        db_table = 'period_history'


class StudentPeriodEnroll(md.Model):
    class Meta:
        db_table = 'student_period_enroll'
