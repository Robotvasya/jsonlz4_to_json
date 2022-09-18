# CLI converter jsonlz4 to json

## Description

This command line tool converts Firefox bookmark backup file from .jsonlz4 format to JSON format

What is a JSONLZ4 file?

A JSONLZ4 file contains compressed user profile data created by Mozilla Firefox web browser. It stores various profile data and settings, such as bookmarks, home page configuration, toolbar layout, and saved passwords. JSONLZ4 files are compressed with LZ4 compression to reduce their size.

You will most likely encounter JSONLZ4 files only if you are exploring the Profile folder where Firefox stores information about user profile.
The reason user information is saved in a separate place from the Firefox application is to protect user profile from being deleted if you need to uninstall and reinstall Firefox on your computer.

Sometimes, for various reasons, users or Forensic specialists want to extract data from this user profile file.
This converterprogram is designed to help in this matter.

## Installation

To run this tool,the Python3 shoul be in your system.

1. Download script zip-file or clone repo
2. Make virtual environment to avoid broken dependences when you install the script. Activate environment
3. Install dependences pip3 install -r requirements.txt
4. Run jsonlz4_conv.py

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

