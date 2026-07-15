from app.database import Base
from app.database import engine

import models


def init_db():
    Base.metadata.create_all(bind=engine)