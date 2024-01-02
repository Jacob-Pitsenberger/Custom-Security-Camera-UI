"""
Module: main.py
Author: Jacob Pitsenberger
Date: 1-2-2024

Description:
    This module serves as the entry point for the Custom Security Camera UI application. It initializes the main application
    and handles any exceptions that may occur during execution.
"""

import logging
from interface.app import App


def main() -> None:
    """
    Entry point for the Custom Security Camera UI application.

    Returns:
        None
    """
    try:
        App()
    except Exception as e:
        logging.error(f"Error in main: {e}")


if __name__ == "__main__":
    main()
