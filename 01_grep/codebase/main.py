"""
Main application entry point.
"""
import os
import sys
import logging
from modules.api import create_app
from modules.db import init_db

# TODO: Add CLI arguments parser (argparse or click)
# FIXME: Graceful shutdown handler is missing for SIGTERM

logger = logging.getLogger("app")

def main():
    logger.info("Initializing system...")
    db = init_db()
    # TODO: Verify database migration version
    app = create_app(db)
    print("Application started on port 8000")
    return app

if __name__ == "__main__":
    main()
