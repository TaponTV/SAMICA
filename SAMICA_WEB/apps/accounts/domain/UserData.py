class UserData:

    def __init__(self, **args) -> None:
        self._academic_key = args[0]
        self._firstname = args[1]
        self._lastname = args[2]
        self._institutionalE = args[3]
        self._personalE = args[4]

    @property
    def academicKey(self) -> str:
        return self.academicKey

    @academicKey.setter
    def academicKey(self, value):
        self._academic_key = value

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    @property
    def institutionalE(self) -> str:
        return self._institutionalE

    @institutionalE.setter
    def institutionalE(self, value):
        self._institutionalE = value

    @property
    def personalE(self) -> str:
        return self._personalE

    @personalE.setter
    def personalE(self, value):
        self._personalE = value
