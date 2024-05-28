from django.db import models as md
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class RoleWeb(md.Model):
    
    id_rol = md.AutoField(primary_key=True)
    rolname = md.CharField(max_length=20)
    description = md.CharField(max_length=25)
    status = md.IntegerField()
    
    class Meta:
        db_table = 'role_web'
        

class Users(AbstractBaseUser):          
    
    id_user = md.AutoField(primary_key=True)
    username = md.CharField(max_length=25, unique=True)
    academic_key = md.CharField(max_length=20)
    password = md.CharField(max_length=255)     # para hash
    status = md.IntegerField()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['academic_key']
    
    objects = BaseUserManager()
    
    class Meta:
        db_table = 'users'


class UserRole(md.Model):
    
    id_user_web = md.ForeignKey(Users, on_delete=md.CASCADE)
    id_rol_web = md.ForeignKey(RoleWeb, on_delete=md.CASCADE)
    status = md.IntegerField()
    
    class Meta:
        db_table = 'users_role'


class Permissions(md.Model):
    
    id_permission = md.AutoField(primary_key=True)
    description = md.CharField(max_length=40)
    
    class Meta:
        db_table = 'permissions'


class RolePermissions(md.Model):
    
    id_rol_web = md.ForeignKey(RoleWeb, on_delete=md.CASCADE)
    id_permission_data = md.ForeignKey(Permissions)
    
    class Meta:
        db_table = 'role_permissions'
        
        
class UserActivityLog(md.Model):
    
    id_log_activity = md.AutoField(primary_key=True)
    user = md.ForeignKey(Users, on_delete=md.CASCADE)
    action = md.CharField(max_length=100)
    timestamp = md.DateTimeField(auto_now_add=True)
    device = md.CharField(max_length=100)
    
    class Meta:
        db_table = 'user_log_activity'
