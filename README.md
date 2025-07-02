# scrcpy Auto

## What is it?

**scrcpy Auto** is a Python script designed to automate and simplify working with the popular Android screen mirroring tool **scrcpy**. It helps speed up and streamline common tasks like launching scrcpy with customized settings.

## How and why does it work?

The script runs on **Python 3.13+** and automates scrcpy commands using a simple console interface. Instead of typing full commands manually, you just enter the number of the desired mode — each number corresponds to a specific set of scrcpy options.

Under the hood, the script uses a large Python dictionary with many predefined command sets. These are selected via keys based on user input. Multiple modes can be combined in one run for more flexible control, making the script powerful for various use cases.

## How to install and use?

1. Make sure you have **Python 3.13+** installed on your system.
2. Clone the repository via git:
   ```bash
   git clone https://github.com/eviltrapgod/Scrcpy-Auto.git
   ```
3. Or download the ZIP archive via GitHub.
4. Navigate to the project folder and run the script:
   ```bash
   python scrcpy_auto.py
   ```
5. Follow the console menu: just enter the number of the action you want. You can also combine modes to run multiple features at once.

## Wishes

All suggestions, ideas, and feature requests are welcome! Feel free to open an issue or contribute via pull request.

## Base Project

This project is built around and relies on the official [scrcpy](https://github.com/Genymobile/scrcpy) tool. Please make sure it is installed and available on your system.
