# CLI converter jsonlz4 to json

## Description

This command line tool converts Firefox user profile data backup file from .jsonlz4 format to JSON format.

What is a JSONLZ4 file?

A JSONLZ4 file contains compressed user profile data created by Mozilla Firefox web browser. It stores various profile data and settings, such as bookmarks, home page configuration, toolbar layout, and saved passwords. JSONLZ4 files are compressed with LZ4 compression to reduce their size.

You will most likely encounter JSONLZ4 files only if you are exploring the Profile folder where Firefox stores information about user profile.
The reason user information is saved in a separate place from the Firefox application is to protect user profile from being deleted if you need to uninstall and reinstall Firefox on your computer.

Where are JSONLZ4 files stored?

JSONLZ4 files are stored in subdirectories of Firefox's Profiles directory, including the bookmarkbackups and datareporting/archived directories. Firefox's Profiles directory is stored in different locations on different operating systems.

In Windows - You can navigate to the location of your profile information by clicking the Menu icon (appears as three horizontal lines) and selecting Help → Troubleshooting Information in Firefox. Then, click the Open Folder button next to "Profile Folder" in the "Application Basics" section to open a window that displays your profile folder. The directory is most likely the following path:

C:\Users\\[username]\AppData\Roaming\Mozilla\Firefox\Profiles\

In Linux, macOS - You can navigate to the location of your profile information by selecting Help → Troubleshooting Information in Firefox. Then, click the Show in Finder button next to "Profile Folder" in the "Application Basics" section to open a window that displays your profile folder. The directory is most likely the following path:

/Users/[username]/Library/Application Support/Firefox/Profiles/

/home/[username]/.mozilla/firefox/[somename].default

Sometimes, for various reasons, users or Forensic specialists want to extract data from this user profile file.
This converterprogram is designed to help in this matter.

## Installation

To run this tool,the Python3 shoul be in your system.

1. Download script zip-file or clone repo
2. Make virtual environment ([Venv environment](https://docs.python.org/3/library/venv.html)) to avoid broken dependences when you install the script. Activate environment
3. Install dependences `python3 -m pip install -r requirements.txt` or `python -m pip install -r requirements.txt` on windows 

Then run jsonlz4_conv.py

## Usage

To convert file run this in terminal

```python3 jsonlz4_conv.py input_file [-o OUTPUT_FILE] ```

or this to get help

```python3 jsonlz4_conv.py --help```

Script usage:

```bash
jsonlz4_conv.py [-h | --help] input_file [-o OUTPUT_FILE]
```

Arguments:

  ```input_file```      Absolute or relative path to jsonlz4 file.

Optional arguments:

  ```-h``` or ```--help```      show this help message and exit
  
  ```-o OUTPUT_FILE```      Absolute or relative path to output JSON file. If argument is omitted, script uses the name of input_file

