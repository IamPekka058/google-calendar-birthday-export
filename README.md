# Google Calendar Birthday Export

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)

A simple Python tool to export birthdays from Google Contacts (CSV or VCF) into an iCalendar (.ics) file. This allows you to easily import your contacts' birthdays into your calendar.

## Features
- Supports CSV and VCF exports from Google Contacts
- Creates standard-compliant .ics calendar files with annually recurring birthday events
- Customizable event summaries (with placeholders for names)
- Interactive configuration in the terminal

>**Note:**  
A pre-built `.exe` is available in the [Releases section](https://github.com/IamPekka058/google-calendar-birthday-export/releases). This allows you to use the tool without a Python installation.

## Requirements
- Python 3.7 or newer
- All required packages are listed in `requirements.txt`

Install the dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/IamPekka058/google-calendar-birthday-export.git
   cd google-calendar-birthday-export
   ```
2. Export your contacts from [Google Contacts](https://contacts.google.com/) as CSV or VCF. See [this guide](https://support.google.com/contacts/answer/7199294).
3. Start the script:
   ```bash
   python export.py
   ```
   Follow the instructions to select file type, input file, event summary, and output file.

## Placeholders for Event Summary
You can use placeholders like `{name}` in the summary, e.g.:
```
Birthday of {name}
```

Currently supported placeholders:
- `{name}` – The full name of the person

## Notes on the CSV Format
The script only supports the CSV format exported from Google Contacts. The file must contain the columns `First Name`, `Middle Name`, `Last Name`, and `Birthday`.

## Notes on the VCF Format
The script supports vCards (VCF) that contain at least a name (`FN`) and a birthday (`BDAY`).

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

<div align="center">
  <sub>Made with ❤️ in Bavaria</sub>
</div>
