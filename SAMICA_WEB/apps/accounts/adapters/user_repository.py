from ..models import Users
from ..domain import User


class users_repository:

    def save(self, user: User):
        objinst = Users(
            username=user.username,
            academic_key=user.academicKey,
            password=user.password
        )
        objinst.save()

    def getusers(self) -> list:
        QueryResult = []
        objectList = []
        try:
            QueryResult = Users.objects.all()
        except Users.DoesNotExist:
            QueryResult = []
        for item in QueryResult:
            objectList.append(
                User(
                    username=item.username,
                    academic_key=item.academic_key,
                    password=item.password,
                    status=item.status
                ))
        return objectList

    def getbyid(self, key):
        try:
            objinst = Users.objects.get(academic_key=key)
        except Users.DoesNotExist:
            objinst = None
        return User(username=objinst.username,
                    academic_key=objinst.academic_key,
                    password=objinst.password,
                    status=objinst.status)
