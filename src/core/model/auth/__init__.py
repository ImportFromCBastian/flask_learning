from src.core.model.auth.user import User
from src.core.database import db


def list_users():
    """
    Lists all users.
    :return: The list of users.
    """

    users = User.query.all()

    return users


def create_user(**kwargs):
    """
    Creates a user.
    :param kwargs: The user's attributes.
    :return: The created user.
    """

    user = User(**kwargs)

    db.session.add(user)
    db.session.commit()

    return user
