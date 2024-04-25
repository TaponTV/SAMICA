from django.db import models as md


class Subjects(md.Model):
    class Meta:
        db_table = 'subjects'
