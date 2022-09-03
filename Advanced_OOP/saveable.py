from database import DataBase


class Saveable:
    def save(self):
        DataBase.insert(self.to_dict())
