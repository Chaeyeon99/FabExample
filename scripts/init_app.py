from FabExample.db.init_db import initialize_database
from FabExample.utils.logger import get_logger

logger = get_logger("InitApp")

if __name__ == "__main__":
    logger.info("Initializing FabExample system...")
    initialize_database()
    logger.info("Database initialized.")
