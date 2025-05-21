# Google Calendar Birthday Export

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)

A simple Python tool to export birthdays from Google Contacts (CSV or VCF) to an iCalendar (.ics) file. Easily import your contacts' birthdays into your favorite calendar app.

## Features
- Supports both CSV and VCF exports from Google Contacts
- Creates standard .ics calendar files with annually recurring birthday events
- Customizable event summaries (with placeholders for names)
- Interactive configuration in the terminal

**Note:**  
You can use the pre-built `.exe` file available in the [Releases](https://github.com/IamPekka058/google-calendar-birthday-export/releases) section. This allows you to run the tool without installing Python or any dependencies.


## Requirements
- Python 3.7 or newer
- All required packages are listed in `requirements.txt`

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/IamPekka058/csv-birthday-export.git
   cd csv-birthday-export
   ```
2. Export your contacts from [Google Contacts](https://contacts.google.com/) as CSV or VCF. See [this guide](https://support.google.com/contacts/answer/7199294) for help.
3. Run the script:
   ```bash
   python export.py
   ```
   Follow the prompts to select file type, input file, event summary, and output file.

## Event Summary Placeholders
You can use placeholders like `{name}` in the event summary, e.g.:
```
Birthday of {name}
```

## Notes on CSV Format
This script only supports the CSV format exported from Google Contacts. The file must include columns like `First Name`, `Middle Name`, `Last Name`, and `Birthday`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<div align="center">
  <sub>Made with ❤️ in Bavaria</sub>
</div>
