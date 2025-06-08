from FabExample.core.engine import fetch_users
from FabExample.core.processor import transform_email
from FabExample.utils.logger import get_logger

logger = get_logger("ShowUsers")

if __name__ == "__main__":
    users = fetch_users()
    for uid, email in users:
        logger.info(f"User ID: {uid}, Email: {transform_email(email)}")
