from django.db import models as md


class Users(md.Model):
    """
    _Clase utilizada como modelo para la tabla "users" en la BD_

    Args:
        md(_Model_): Class Model for Django
        
    """
    id_user = md.AutoField(primary_key=True)
    username = md.CharField(max_length=25)
    password = md.CharField(max_length=25)
    id_rol = md.IntegerField()
    status = md.IntegerField()
    
    class Meta:
        db_table = 'users'


class UserRol(md.Model):
    """
    _Clase utilizada como modelo para la tabla "user_relation_rol" en la BD_

    Args:
        md(_Model_): Class Model for Django
        
    """
    class Meta:
        db_table = 'user_relation_rol'


class Permissions(md.Model):
    """
    _Clase utilizada como modelo para la tabla "users" en la BD_

    Args:
        md(_Model_): Class Model for Django
        
    """
    class Meta:
        db_table = 'permissions'


class RolWeb(md.Model):
    """
    _Clase utilizada como modelo para la tabla "users" en la BD_

    Args:
        md(_Model_): Class Model for Django
        
    """
    class Meta:
        db_table = 'rol'


class PermissionRol(md.Model):
    """
    _Clase utilizada como modelo para la tabla "users"_
    
    

    Args:
        md(_Model_): Class Model for Django
        
    """
    class Meta:
        db_table = 'permissions_relation_rol'
        
        
class UserActivityLog(md.Model):
    """
    _Clase utilizada como modelo para la tabla "userLog"_
    
    Cumple la función de mostrar un registro de la actividad de los usuarios en el sistema como conexiones y desconexiones
 
    Args:
        md(_Model_): Class Model for Django
        
    """
    _id_log_activity = md.AutoField(primary_key=True)
    user = md.ForeignKey(Users, on_delete=md.CASCADE)
    action = md.CharField(max_length=100)
    _timestamp = md.DateTimeField(auto_now_add=True)
    device = md.CharField(max_length=100)
    
    class Meta:
        db_table = 'userLog'