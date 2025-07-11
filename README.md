# scrcpy Auto

## What is it?

**scrcpy Auto** is a Python script designed to automate and simplify working with the popular Android screen mirroring tool **scrcpy**. It helps speed up and streamline common tasks like launching scrcpy with customized settings.

## How and why does it work? 

The script runs on **Python 3.13+** and automates scrcpy commands using a simple console interface. Instead of typing full commands manually, you just enter the number of the desired mode — each number corresponds to a specific set of scrcpy options.

Under the hood, the script uses a large Python dictionary with many predefined command sets. These are selected via keys based on user input. Multiple modes can be combined in one run for more flexible control, making the script powerful for various use cases.

You can also use your own scrcpy commands and parameters by simply entering them in the appropriate field. You can also enable or disable the display of commands in the list of available ones. When disabled, only the description will be visible, which in turn provides a complete understanding of what the command does.

## How to install and use?

1. Make sure you have **Python 3.13+** installed on your system.
2. IMPORTANT. Make sure you have **scrcpy** installed.
3. Clone the repository via git:
   ```bash
   git clone https://github.com/eviltrapgod/Scrcpy-Auto.git
   ```
4. Or download the ZIP archive via GitHub.
5. Navigate to the project folder and run the script:
   ```bash
   python3 main.py
   ```
   or start `main.py` in Your file manager
7. Follow the console menu: just enter the number of the action you want.

8. I recommend turning off the command list display when starting, otherwise it becomes difficult to understand anything in the console.


## Wishes

All suggestions, ideas, and feature requests are welcome! Feel free to open an issue or contribute via pull request.

## Notice on Third-Party Code

This project includes elements based on the [scrcpy](https://github.com/Genymobile/scrcpy) project,  
which is licensed under the Apache License, Version 2.0.

Use of this portion complies with the terms of the Apache 2.0 license.  
See [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0) for details.

