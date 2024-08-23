from ..models.button import Button
from typing import List, Tuple


class RoleButtons:
    def get_taglist(self) -> List[Tuple[str, str]]:
        raise NotImplementedError


class adminRole(RoleButtons):
    def get_taglist(self) -> List[Tuple[str, str]]:
        return [
            ('Usuarios', '/users/'),
            ('Estudiantes', '/users/students/'),
            ('Académicos', '/users/academics'),
            ('Roles - Permisos', '/accounts/roles/'),
            ('Registro (log)', '/system/log/'),
            ('Estadisticas', '/accounts/graphs/'),
            ('Vistas', '/system/views/')
        ]


class adminFacuRole(RoleButtons):
    def get_taglist(self) -> List[Tuple[str, str]]:
        return [
            ('Estudiantes', '/users/students/'),
            ('Académicos', '/users/academics'),
            ('Tutores', '/users/academics/tutors/'),
            ('Estadisticas', '/accounts/graphs/'),
            ('Experiencias Ed.', '/institution/EE/'),
            ('Informes', '/report_generator/')
        ]


class tutorRole(RoleButtons):
    def get_taglist(self) -> List[Tuple[str, str]]:
        return [
            ('Historial Académico', '/users/students/history/'),
            ('Estadisticas', '/accounts/graphs/professor/'),
            ('Horarios', '/users/academics/schedule/'),
            ('Experiencias Ed.', '/users/academics/EE/'),
            ('Informes', '/report_generator/')
        ]


class professorRole(RoleButtons):
    def get_taglist(self) -> List[Tuple[str, str]]:
        return [
            ('Historial Académico', '/users/students/history/'),
            ('Estadisticas', '/accounts/graphs/professor/'),
            ('Horarios', '/users/academics/schedule/'),
            ('Experiencias Ed.', '/users/academics/EE/'),
            ('Informes', '/report_generator/')
        ]


class studentRole(RoleButtons):
    def get_taglist(self) -> List[Tuple[str, str]]:
        return [
            ('Historial Académico', '/users/students/history/'),
            ('Estadisticas', '/accounts/graphs/professor/'),
            ('Horarios', '/users/academics/schedule/'),
            ('Experiencias Ed.', '/users/academics/EE/'),
            ('Informes', '/report_generator/')
        ]


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
            return adminRole()
        elif self.roleuser == 'tutor':
            return tutorRole()
        elif self.roleuser == 'adminFacu':
            return adminFacuRole()
        elif self.roleuser == 'professor':
            return professorRole()
        elif self.roleuser == 'student':
            return studentRole()
        else:
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
