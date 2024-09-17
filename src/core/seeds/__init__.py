from src.core.model import auth


def grow():
    """
    Seeds the database
    """

    user1 = auth.create_user(name="Alice")
    user2 = auth.create_user(name="Bob")
    user3 = auth.create_user(name="Charlie")
