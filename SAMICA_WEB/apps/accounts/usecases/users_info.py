from ..models import Users

class GetUserInfo:
    
    def __init__(self, keyID = None):
        if not keyID:
            self.execute_1()
        else:
            self.execute_2(keyID)
            
    def execute_1(self):
        try:
            self.ListObject = Users.objects.all()
        except Users.DoesNotExist:
            self.ListObject = []
        
    def execute_2(self, keyID):
        try:
            self.UserObject = Users.objects.get(academic_key=keyID)
        except Users.DoesNotExist:
            self.UserObject = None