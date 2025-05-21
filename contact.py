from datetime import datetime

class Contact:
    def __init__(self, name : str, birthday : datetime):
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}: {self.birthday}"

    def __repr__(self):
        return f"Contact(name={self.name}, phone_number={self.birthday})"