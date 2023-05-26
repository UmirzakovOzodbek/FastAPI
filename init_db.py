from core import models, database

from core.models import User, Item  # noqa

models.Base.metadata.create_all(bind=database.engine)
