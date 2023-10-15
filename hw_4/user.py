import hashlib
from abc import ABC, abstractmethod


class User:
    def __init__(self, user_id, username, hash_password, card_number):
        self.user_id = user_id
        self.username = username
        self.hash_password = hash_password
        self.card_number = card_number

    def hashcode(self):
        data_to_hash = f"{self.user_id}{self.username}{self.hash_password}{self.card_number}"
        hashed_data = hashlib.sha256(data_to_hash.encode()).hexdigest()
        return hashed_data


class UserRepo(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def remove_user(self, user_id):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass


class UserRepository(UserRepo):
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def get_user(self, user_id):
        return self.users.get(user_id, None)
