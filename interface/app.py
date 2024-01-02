"""
Module: app.py
Author: Jacob Pitsenberger
Date: 1-2-2024

Description:
    This module defines the main application class for the Custom Security Camera UI. It utilizes the customtkinter library
    for the graphical user interface and includes components from the interface.utils and interface.gui modules.
"""

import customtkinter as ctk
from interface.utils import MATRIX_GREENS, get_cam_url
from interface.gui import GUI
import logging

class App(ctk.CTk):
    """Main application for the Custom Security Camera UI."""
    def __init__(self) -> None:
        """
        Initialize the main application.

        Args:
            None

        Returns:
            None
        """
        try:
            # main setup
            super().__init__()

            self.title('Camera System UI')

            # Define custom colors
            self.gui_colors = MATRIX_GREENS

            self.url: str = get_cam_url()

            self.gui: GUI = GUI(self, self.url)

            self.mainloop()
        except Exception as e:
            logging.error(f"Error in App initialization: {e}")

# Rest of the code remains unchanged
