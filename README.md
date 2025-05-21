# csv-birthday-export

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)

A simple Python script to export birthdays from a Google Contacts CSV export to an iCalendar (.ics) file.

Easily convert birthdays from a Google Contacts CSV export into an iCalendar (.ics) file. This script helps you transfer birthday reminders from your Google contacts directly into your favorite calendar application.

## Features
- Reads birthdays from CSV files exported from Google Contacts
- Exports events to a standard .ics calendar file
- Easy to use and customize

## Requirements
- Python 3.7 or higher

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/IamPekka058/csv-birthday-export.git
   cd csv-birthday-export
   ```
2. Export your contacts from Google Contacts as a CSV file (see below).
3. Run the script:
   ```bash
   python csv2ics.py contacts.csv
   ```
   Replace `contacts.csv` with your exported file.

## How to export contacts from Google Contacts
See this [Google support page](https://support.google.com/contacts/answer/7199294) for instructions on how to export your contacts.

## CSV Format
This script only works with the CSV format exported from Google Contacts. No other CSV formats are currently supported.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<div align="center">
  <sub>Made with ❤️ in Bavaria</sub>
</div>
