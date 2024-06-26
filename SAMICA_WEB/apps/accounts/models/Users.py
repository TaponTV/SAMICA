from django.db import models as md
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class RoleWeb(md.Model):

    id_rol = md.AutoField(primary_key=True)
    rolname = md.CharField(max_length=20)
    description = md.CharField(max_length=25)
    status = md.IntegerField(default=1)

    class Meta:
        db_table = 'role_web'
  

class Users(AbstractBaseUser):

    id_user = md.AutoField(primary_key=True)
    username = md.CharField(max_length=25, unique=True)
    academic_key = md.CharField(max_length=20, unique=True)
    password = md.CharField(max_length=255)
    status = md.IntegerField(default=1)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['academic_key']

    objects = BaseUserManager()

    class Meta:
        db_table = 'users'


class UserData(md.Model):

    academic_key = md.CharField(primary_key=True, max_length=20, unique=True)
    firstname = md.CharField(max_length=40)
    lastname = md.CharField(max_length=40)
    institutional_email = md.CharField(max_length=60, null=True)
    personal_email = md.CharField(max_length=60, null=True)
    status = md.IntegerField(default=1)

    class Meta:
        db_table = 'UserData'


class UserRole(md.Model):

    id_user = md.ForeignKey(Users, on_delete=md.CASCADE)
    id_rol = md.ForeignKey(RoleWeb, on_delete=md.CASCADE)
    status = md.IntegerField(default=1)

    class Meta:
        db_table = 'users_role'


class Permissions(md.Model):

    id_permission = md.AutoField(primary_key=True)
    description = md.CharField(max_length=40)
    permission_name = md.CharField(max_length=25)

    class Meta:
        db_table = 'permissions'


class RolePermissions(md.Model):

    id_rol = md.ForeignKey(RoleWeb, on_delete=md.CASCADE)
    id_permission = md.ForeignKey(Permissions, on_delete=md.CASCADE)

    class Meta:
        db_table = 'role_permissions'


class actionsDict(md.Model):

    id_action = md.AutoField(primary_key=True)
    name = md.CharField(max_length=25)
    description = md.CharField(max_length=60)

    class Meta:
        db_table = 'dictionary_actions'


class UserActivityLog(md.Model):

    id_log_activity = md.AutoField(primary_key=True)
    id_user = md.ForeignKey(Users, on_delete=md.CASCADE)
    action = md.CharField(max_length=100)
    timestamp = md.DateTimeField(auto_now_add=True)
    device = md.CharField(max_length=100)

    class Meta:
        db_table = 'user_log_activity'
