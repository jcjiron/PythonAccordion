from app import db


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))
    email = db.Column(db.String(200))

    def __str__(self):
        return (
            f'Id:{self.id}',
            f'Name:{self.name}',
            f'Surname:{self.surname}',
            f'Email:{self.email}'
        )
