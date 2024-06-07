from apps.accounts.models import UserData, UserRole, RolePermissions

def get_user_data(auth_user) -> dict:
    
    #Obtiene los datos del usuario desde la tabla UserData
    try:
        user_data = UserData.objects.get(academic_key=auth_user.academic_key)
        first_name = user_data.firstname
        last_name = user_data.lastname
    except UserData.DoesNotExist:
        first_name = ""
        last_name = ""
    
    #Obtiene los datos del usuario en cuestion de sus respectivos roles y permisos
    try:
        user_role = UserRole.objects.get(id_user_web=auth_user)
        role_name = user_role.id_rol_web.rolname
        role_permissions = RolePermissions.objects.filter(id_rol_web=user_role.id_rol_web)
    except UserRole.DoesNotExist:
        role_name = ""
        role_permissions = []
        
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'role_name': role_name,
        'role_permissions': role_permissions,
    }

    return context
    