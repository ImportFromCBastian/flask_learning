from src.core.model import auth
from src.core.model import issues


def grow():
    """
    Seeds the database
    """

    issue1 = issues.create_issue(
        title="Issue 1", description="This is issue 1", status="open"
    )
    issue2 = issues.create_issue(
        title="Issue 2", description="This is issue 2", status="closed"
    )
    issue3 = issues.create_issue(
        title="Issue 3", description="This is issue 3", status="open"
    )

    user1 = auth.create_user(name="Alice")
    user2 = auth.create_user(name="Bob")
    user3 = auth.create_user(name="Charlie")

    issues.assign_issue(issue1, user1)
    issues.assign_issue(issue2, user2)
    issues.assign_issue(issue3, user3)
