from django.contrib.auth.hashers import make_password


class User:

    def __init__(self, **kwargs) -> None:
        self._datalist = {}
        for (key, data) in kwargs.items():
            self._datalist[key] = data
        self._datalist['password'] = make_password(self._datalist['password'])

    @property
    def username(self) -> str:
        return self._datalist['username']

    @username.setter
    def username(self, value):
        self._datalist['username'] = value

    @property
    def academicKey(self) -> str:
        return self._datalist['academic_key']

    @academicKey.setter
    def academicKey(self, value):
        self._datalist['academic_key'] = value

    @property
    def password(self) -> str:
        return self._datalist['password']

    @password.setter
    def password(self, value):
        self._datalist['password'] = make_password(value)

    @property
    def status(self) -> str:
        if self._datalist['status'] == 1:
            return 'Activo'
        else:
            return 'Inactivo'

    @status.setter
    def status(self, value):
        self._datalist['status'] = value
