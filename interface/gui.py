"""
Module: gui.py
Author: Jacob Pitsenberger
Date: 1-2-2024

Description:
    This module defines the GUI class for the Custom Security Camera UI. It utilizes customtkinter for the graphical user
    interface and includes components from the interface.utils module.
"""

import customtkinter as ctk
import datetime
import cv2
import requests
import logging


class GUI(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, url: str) -> None:
        """
        Initialize Feeds instance.

        Args:
            parent (ctk.CTk): The parent widget.
            url (str): The camera url/ip to connect to.

        Returns:
            None
        """

        super().__init__(parent)
        self.pack(fill='both')

        self.parent: ctk.CTk = parent

        # 4 colors by index (light green, green, dark green, black green)
        self.gui_colors = self.parent.gui_colors

        self.url: str = url

        self.widget_frame: ctk.CTkFrame = ctk.CTkFrame(self, fg_color=self.gui_colors[3], border_width=2,
                                                       border_color=self.gui_colors[2])

        self.welcome_lbl: ctk.CTkLabel = ctk.CTkLabel(self.widget_frame,
                                                      text='Welcome to the camera system User Interface!',
                                                      font=('Roboto', 16, 'bold'))

        self.help_lbl: ctk.CTkLabel = ctk.CTkLabel(self.widget_frame,
                                                   text='- Press the View Feed button to display the live camera feed.',
                                                   font=('Roboto', 12), justify='left')

        self.view_cam_btn: ctk.CTkButton = ctk.CTkButton(self.widget_frame, text="View Feed",
                                                         fg_color=self.gui_colors[1], font=('Roboto', 20, 'bold'),
                                                         text_color=self.gui_colors[3], hover_color=self.gui_colors[0],
                                                         command=lambda: self.display_camera_feed())

        self.status_lbl: ctk.CTkLabel = ctk.CTkLabel(self.widget_frame, text='', font=('Roboto', 20, 'bold'),
                                                     text_color='white')

        self.bottom_border_lbl: ctk.CTkLabel = ctk.CTkLabel(self.widget_frame, text='', bg_color=self.gui_colors[2],
                                                            text_color='white')

        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Create widgets for the PostProcessDetections frame.

        Returns:
            None
        """
        self.widget_frame.pack(fill='both', expand=True)
        self.welcome_lbl.pack(padx=20, pady=(30, 10))
        self.help_lbl.pack(padx=20, pady=10)
        self.view_cam_btn.pack(padx=20, pady=(20, 10))
        self.status_lbl.pack(padx=20, pady=(10, 0))
        self.bottom_border_lbl.pack(fill='both', expand=True)

    def clear_status_label(self) -> None:
        """
        Clear the status label text.

        Returns:
            None
        """
        try:
            self.status_lbl.configure(text="")
        except Exception as e:
            logging.error(f"Error clearing status label: {e}")

    @staticmethod
    def set_resolution(url: str, index: int = 1, verbose: bool = False) -> None:
        """
        From Hardware Documentation on OV2640 camera
        - UXGA/SXGA: 15 fps [use waitKey(66)]
        - SVGA: 30 fps
        - CIF: 60 fps
        - VGA: 25 fps [use waitKey(40)]
        """
        try:
            if verbose:
                resolutions: str = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n" \
                                   "7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n" \
                                   "3: HQVGA(240x176)\n0: QQVGA(160x120)"
                logging.info("available resolutions\n{}".format(resolutions))

            if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
                requests.get(url + "/control?var=framesize&val={}".format(index))
            else:
                logging.warning("Wrong index")
        except requests.RequestException as re:
            logging.error(f"RequestException in set_resolution: {re}")
        except Exception as e:
            logging.error(f"Error in set_resolution: {e}")

    @staticmethod
    def set_quality(url: str, value: int = 1, verbose: bool = False) -> None:
        try:
            if 10 <= value <= 63:
                requests.get(url + "/control?var=quality&val={}".format(value))
        except requests.RequestException as re:
            logging.error(f"RequestException in set_quality: {re}")
        except Exception as e:
            logging.error(f"Error in set_quality: {e}")

    @staticmethod
    def set_awb(url: str, awb: int = 1) -> bool:
        try:
            awb = not awb
            requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
        except requests.RequestException as re:
            logging.error(f"RequestException in set_awb: {re}")
        except Exception as e:
            logging.error(f"Error in set_awb: {e}")
        return awb

    def display_camera_feed(self) -> None:
        """
        Stream from url cam.

        Raises:
            ValueError: If the selected camera channel is unable to be connected to.
            cv2.error: If an OpenCV-related error occurs during real-time feed processing.
            requests.RequestException: For issues related to making requests.
            Exception: For other generic exceptions.

        Returns:
            None
        """
        try:
            AWB: bool = True
            current_date: str = str(datetime.datetime.now().date())
            cap: cv2.VideoCapture = cv2.VideoCapture(self.url + ":81/stream")

            # Resolution is 640x480(VGA) so setting to index 6
            self.set_resolution(self.url, index=6)
            self.set_awb(self.url, AWB)
            self.set_quality(self.url, value=10)
            if not cap.isOpened():
                # Update the status label after processing
                self.status_lbl.config(text=f"Error opening camera.")
                # Schedule clearing the label after 5 seconds
                self.after(5000, self.clear_status_label)
                raise ValueError(f"Error opening camera url: {self.url}")

            while True:
                if cap.isOpened():
                    ret, frame = cap.read()
                    cv2.putText(frame, current_date, (5, 15), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
                                color=(0, 255, 0), thickness=1)
                    cv2.imshow("frame", frame)

                    # change waitKey for VGA: 25 fps ~= waitKey(40)
                    key: int = cv2.waitKey(40)

                    if key == 27:
                        cv2.destroyAllWindows()
                        cap.release()
                        break

        except cv2.error as cve:
            logging.error(f"OpenCV Error in display_camera_feed: {cve}")
        except requests.RequestException as re:
            logging.error(f"RequestException in display_camera_feed: {re}")
        except Exception as e:
            logging.error(f"Error in display_camera_feed: {e}")
