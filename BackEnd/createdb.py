from BackEnd.app import db
from BackEnd.app.models import *


if __name__ == '__main__':
    db.create_all()
# db.create_all()