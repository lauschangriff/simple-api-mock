class Person:
    def __init__(self, pid, name, vorname, position, telefon, email):
        self.pid = pid
        self.name = name
        self.vorname = vorname
        self.position = position
        self.telefon = telefon
        self.email = email
        self

    def __repr__(self):
        return (
            'Person ('
            f'pid: {self.pid}, '
            f'name: {self.name}, '
            f'vorname: {self.vorname}, '
            f'position: {self.position}, '
            f'telefon: {self.telefon} ,'
            f'email: {self.email})'
        )

    def to_json(self):
        return self.__dict__
