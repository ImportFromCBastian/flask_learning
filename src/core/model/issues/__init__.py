from src.core.model.issues.issue import Issue
from src.core.database import db


def list_issues():
    """
    Lists all issues.
    :return: The list of issues.
    """

    issues = Issue.query.all()

    return issues


def create_issue(**kwargs):
    """
    Creates an issue.
    :param kwargs: The issue's attributes.
    :return: The created issue.
    """

    issue = Issue(**kwargs)

    db.session.add(issue)
    db.session.commit()

    return issue


def assign_issue(issue, user):
    """
    Assigns an issue to a user.
    :param issue: The issue to assign.
    :param user: The user
    """
    issue.user = user

    db.session.add(issue)
    db.session.commit()

    return issue
