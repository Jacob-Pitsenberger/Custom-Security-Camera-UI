# Custom Security Camera UI

## Project Description

The Custom Security Camera UI is a Python application designed to provide a user-friendly interface for streaming video from any camera that uses the 'http' protocol. The camera's IP is accessed by the program through storing it in a text file 'cameras.txt' with the IP address format as ###.###.#.###. This project is particularly useful for devices like the ESP32 camera module, which was used for the creation and testing of this project. The application utilizes the customtkinter library for the graphical user interface and includes components for streaming live camera feed and retrieving camera IP information from a text file for connection as a web URL.

## Project Structure

The project structure is organized as follows:

### 1. `main.py`

This module serves as the entry point of the application. It initializes the main application class (`App` from `interface.app`) and handles any exceptions that may occur during the application's execution.

### 2. `interface` Package

The `interface` package contains the main modules of the Custom Security Camera UI:

   - `app.py`: Defines the main application class for the Custom Security Camera UI. It inherits from the customtkinter library and sets up the main application window. It also initializes the GUI and handles the main event loop.

   - `gui.py`: Defines the GUI class for the Custom Security Camera UI. It inherits from the customtkinter library and includes components for displaying a welcome message, providing instructions, and streaming the live camera feed. Additionally, it offers functionalities for adjusting camera settings like resolution and white balance.

   - `utils.py`: Provides utility functions for the Custom Security Camera UI. It includes functions for opening a file explorer, opening a file with the default system player, getting the camera IP address and URL, and defining color constants. The current implementation only makes use of the camera IP and URL retrieval operations, with the others planned for future use in saving video feeds to a file for later viewing.


## Usage

To use the Custom Security Camera UI with your ESP32 camera module or any other camera that uses the 'http' protocol with a standard IP address:

1. Run the `main.py` module.
2. The main application window will appear, featuring the GUI.
3. Press the "View Feed" button to display the live camera feed.
4. Adjust camera settings, such as resolution and white balance, as needed.

The application supports opening files using the default system player and retrieving the camera's IP address and URL from a configuration file.

## Configuration

Camera configurations, such as IP addresses and URLs, can be specified in the `cameras.txt` file. Ensure that your camera is set up to use the 'http' protocol for video streaming.

## Dependencies

The project depends on the following Python libraries:

- customtkinter~=5.2.1
- opencv-python~=4.8.0.74
- requests~=2.28.2

Make sure to install these dependencies before running the application.

## Additional Notes

- The application utilizes a custom color scheme represented by the `MATRIX_GREENS` constants in the utils.py module.
- Logging has been implemented throughout the modules to facilitate debugging and error tracking.

## Project Status

The Custom Security Camera UI is an ongoing software project aimed at providing continuous improvements and enhancements. The current set of modules provides a basic and functional proof of concept. As part of ongoing development, future updates and features are planned, such as:

- Unit tests for program modules.
- Improved file handling and video recording capabilities.
- Enhanced user interface elements and customization options.
- Integration of advanced camera settings.
- Displaying feeds from multiple cameras at once.
- Computer vision for object detection and still image captures.
- Support for additional camera models and protocols.

Feel free to check back for updates, and contributions or suggestions are welcome!

## License

This software is licensed under the MIT License. By using this software, you agree to comply with the terms outlined in the license.