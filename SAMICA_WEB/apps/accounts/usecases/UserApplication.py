from ..domain import User


class UserApplication:

    def __init__(self, obj):
        self.userRepository = obj

    def save_user(self, **kwargs):
        user = User(kwargs)
        self.userRepository.save(user)

    def read_users(self) -> list:
        return self.userRepository.getusers()

    def read_by_id(self, key) -> object:
        return self.userRepository.getbyid(key)
