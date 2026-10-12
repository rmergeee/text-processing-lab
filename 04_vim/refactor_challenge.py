# ==============================================================================
# VIM REFACTORING CHALLENGE
# Завдання для тренування складних команд Vim:
# 1. Вирівняйте знаки '=' за допомогою Visual Block mode (Ctrl-v).
# 2. Замініть print(...) на logger.info(...) за допомогою :%s/print(\([^)]*\))/logger.info(\1)/g
# 3. Видаліть усі рядки коментарів з '#' через :g/^\s*#/d
# 4. Відсортуйте імпорти алфавітно через візуальне виділення і :sort
# ==============================================================================

import sys
import json
import os
import requests
import time
import math

# Temporary debug variables
db_host = "127.0.0.1"
db_port = 5432
db_user = "postgres"
db_password = "very_secret_password"
db_timeout_seconds = 30

# Calculate some settings
def run_diagnostics():
    # Print statement 1
    print("Starting diagnostics pipeline...")
    # Print statement 2
    print("Checking connection to database...")
    # Print statement 3
    print("Diagnostics completed successfully.")

# Extra junk comments to remove
# Junk line 1
# Junk line 2
# Junk line 3

def process_data(items):
    total = 0
    for item in items:
        # Debug print
        print(f"Processing item: {item}")
        total += item
    return total
