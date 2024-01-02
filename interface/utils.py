"""
Module: utils.py
Author: Jacob Pitsenberger
Date: 1-2-2024

Description:
    This module provides utility functions for the Custom Security Camera UI. It includes functions for opening a file explorer,
    opening a file with the default system player, getting the camera IP address and URL, and defining color constants.
"""

from tkinter import filedialog
import os
import subprocess
import logging

# COLORS FROM LIGHT TO DARK
MATRIX_GREENS = ['#00FF41', '#008F11', '#003B00', '#0D0208']

def open_file_explorer() -> str:
    """
    Open a file explorer dialog to allow the user to select a file.

    Returns:
        str: The path of the selected file.
    """
    try:
        initial_dir: str = os.path.join(os.getcwd())
        file_path: str = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("All files", "*.*")])
        # `file_path` will contain the path of the selected file.
        logging.info("Selected file: %s", file_path)
        return file_path
    except Exception as e:
        logging.error("Error opening file explorer: %s", e)
        return None


def open_with_default_player(file_path: str) -> None:
    """
    Open a file using the default system application.

    Args:
        file_path (str): The path to the file to be opened.

    Returns:
        None
    """
    try:
        if os.name == 'nt':
            os.startfile(file_path)  # Opens the file using the default Windows application
        elif os.name == 'posix':
            subprocess.run(['xdg-open', file_path])  # Opens the file using xdg-open (Linux)
    except Exception as e:
        logging.error("Error opening file: %s", e)


def open_file_with_default_player() -> None:
    """
    Open a file selected by the user using the default system application.

    Returns:
        None
    """
    try:
        file_path: str = open_file_explorer()
        if file_path:
            open_with_default_player(file_path)
    except Exception as e:
        logging.error("Error opening file with default player: %s", e)


def get_cam_ip() -> str:
    """
    Get the camera IP address from the 'cameras.txt' file.

    Returns:
        str: The camera IP address.
    """
    try:
        with open('cameras.txt', 'r') as file:
            url: str = file.read().replace('\n', '')
        return url
    except Exception as e:
        logging.error("Error getting camera IP: %s", e)
        return ''


def get_cam_url() -> str:
    """
    Get the camera URL by combining 'http://' and the camera IP.

    Returns:
        str: The camera URL.
    """
    try:
        ip: str = get_cam_ip()
        url: str = "".join(['http://', ip])
        return url
    except Exception as e:
        logging.error("Error getting camera URL: %s", e)
        return ''
