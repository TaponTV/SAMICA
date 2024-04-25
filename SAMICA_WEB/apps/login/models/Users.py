from django.db import models as md


class Users(md.Model):
    class Meta:
        db_table = 'users'


class UserRol(md.Model):
    class Meta:
        db_table = 'user_relation_rol'


class Permissions(md.Model):
    class Meta:
        db_table = 'permissions'


class RolWeb(md.Model):
    class Meta:
        db_table = 'rol'


class PermissionRol(md.Model):
    class Meta:
        db_table = 'permissions_relation_rol'
