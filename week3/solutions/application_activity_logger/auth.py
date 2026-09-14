"""Login and logout operations."""

from .exceptions import AuthenticationError


DEMO_USERNAME = "admin"
DEMO_PASSWORD = "python123"


def login(username, password, logger):
    """Validate the demonstration credentials and return the logged-in username."""
    logger.debug("Login attempt received for username %r.", username)

    if not isinstance(username, str) or not username.strip():
        logger.warning("Login attempted without a username.")
        raise AuthenticationError("Username is required.")
    if not isinstance(password, str) or not password:
        logger.warning("Login attempted without a password.")
        raise AuthenticationError("Password is required.")

    cleaned_username = username.strip()
    if cleaned_username != DEMO_USERNAME or password != DEMO_PASSWORD:
        logger.warning("Failed login attempt for user %s.", cleaned_username)
        raise AuthenticationError("Incorrect username or password.")

    logger.info("User %s logged in.", cleaned_username)
    return cleaned_username


def logout(username, logger):
    """Log a user out and record the activity."""
    if username:
        logger.info("User %s logged out.", username)
    else:
        logger.warning("Logout selected without an active user session.")

