# Import all the models, so that Base has them before being
# imported by Alembic
from webapp.db.base_class import Base  # noqa
from webapp.models.item import Item  # noqa
from webapp.models.user import User  # noqa
