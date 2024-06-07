from ..models.button import Button
from typing import List, Tuple


class RoleButtons:
    def get_taglist(self) -> List[Tuple[str, str]]:
        raise NotImplementedError


class AdminRole(RoleButtons):
    def get_taglist(self) -> List[Tuple[str, str]]:
        return [
            ('Tablas', 'tables/'),
            ('Paginas', '/dashboard/pages/'),
            ('Usuarios', '/accounts/users'),
            ('Graficas', '/controlpanel/charts')
        ]


class TutorRole(RoleButtons):
    def get_taglist(self) -> List[Tuple[str, str]]:
        return [
            ('Estudiantes', '/students/'),
            ('Historial', '/students/historial')
        ]


# class DefaultButtons(RoleButtons):
#     def get_taglist(self) -> List[Tuple[str, str]]:
#         return []

class GetDashboardButtons:
    def __init__(self, roleuser):
        self.roleuser = roleuser
        self.buttons = [
            Button(label='Dashboard', url='/dashboard/'),
            Button(label='Configuracion', url='/accounts/config'),
            Button(label='Cerrar Sesión', url='/logout')
        ]
        self.method_role = self.__select_role()

    def __select_role(self) -> RoleButtons:
        if self.roleuser == 'admin':
            return AdminRole()
        elif self.roleuser == 'tutor':
            return TutorRole()
        else:
            # return DefaultButtons()
            pass

    def execute(self) -> List[Button]:
        taglist = self.method_role.get_taglist()
        self.__generate_buttons(taglist)
        return self.buttons

    def __generate_buttons(self, taglist: List[Tuple[str, str]]) -> None:
        index = 1
        for label, url in taglist:
            self.buttons.insert(index, Button(label=label, url=url))
            index += 1