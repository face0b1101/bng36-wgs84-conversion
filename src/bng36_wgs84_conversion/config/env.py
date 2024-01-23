#!/usr/bin/env python

# Configuration loader for a Python application using 'decouple' and 'unipath' libraries.
# It fetches log level and timezone settings from environment variables with defaults.

from decouple import config  # Fetches environment variables
from unipath import Path  # OS-independent file manipulation

# Base directory of the script
BASE_DIR = Path(__file__).parent

# Log level setting, defaults to 'WARNING' if not set
LOG_LEVEL = config("LOG_LEVEL", cast=str, default="WARNING")

# Timezone setting, defaults to 'Europe/London' if not set
DEFAULT_TZ = config("TZ", cast=str, default="Europe/London")

# Summary:
# This script sets up basic configuration for a Python project by determining the base directory
# and extracting environment variables for log level and timezone with default values.
# It utilizes 'decouple' for configuration management and 'unipath' for file path handling.
