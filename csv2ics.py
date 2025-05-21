import csv
from datetime import datetime
import pyfiglet
import pytz
from icalendar import Calendar, Event
import argparse

translations = {
    "en": {
        "birthday_label": "Birthday"
    },
    "de": {
        "birthday_label": "Geburtstag"
    },
}

def checkIfCSVFileIsValid(file_path):
    print("Checking if file is valid: []", end="\r")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            if 'First Name' not in header or 'Birthday' not in header:
                print("The CSV File has to contain the columns 'Name' and 'Birthday'.")
                exit(1)
            for row in reader:
                if len(row) != len(header):
                    print("The CSV File is malformed.")
                    exit(1)

        print("Checking if file is valid: [✓]", end="\n")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        exit(1)

def readCSVFile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        header = rows.pop(0)
    return (header, rows)

def fillICSWithCSVData(header, rows, language):
    cal = Calendar()
    cal.add('prodid', '-//Geburtstage CSV Import//example.com//')
    cal.add('version', '2.0')

    count = 0

    for row in rows:
        first_name = row[header.index('First Name')]
        middle_name = row[header.index('Middle Name')]
        last_name = row[header.index('Last Name')]
        name = f"{first_name} {middle_name} {last_name}".strip()

        bday_str = row[header.index('Birthday')].strip()

        if not bday_str:
            continue
        try:
            if bday_str.startswith('-'):
                current_year = datetime.today().year
                bday_str = f"{current_year}{bday_str[1:]}"

            bday = datetime.strptime(bday_str, "%Y-%m-%d")
        except ValueError:
            print(f"Invalid date format for {name}: {bday_str}. Expected format: YYYY-MM-DD or --MM-DD.")
            continue

        event = Event()
        event.add('summary', f'{translations[language]['birthday_label']}: {name}')
        event.add('dtstart', datetime(bday.year, bday.month, bday.day).date())
        event.add('dtstamp', datetime.now(tz=pytz.UTC))
        event.add('rrule', {'freq': 'yearly'})
        event.add('transp', 'TRANSPARENT')
        cal.add_component(event)
        print(f"Added birthday for {name} on {bday_str}", end="\r")
        count += 1

    print(" " * 100, end="\r")  # Clear the last line
    print(f"Added birthdays for {count} people.")
    print("Finished parsing.")
    return cal

def writeICSFile(cal, output_file):
    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())
    print(f"iCalendar file {output_file} created successfully.")

def printBanner():
    ascii_banner = pyfiglet.figlet_format("IamPekka058")
    print(ascii_banner)

def checkLanguage(language):
    if language not in translations:
        print(f"Language '{language}' is not supported. Defaulting to 'en'.")
        return "en"
    return language

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Import birthdays from a CSV file and generate an iCalendar file.")
    parser.add_argument("input_csv", help="The CSV file to import.")
    parser.add_argument("--output", help="The iCalendar file.", default="output.ics")
    parser.add_argument("--language", help="The language of the iCalendar file.", default="en")
    args = parser.parse_args()

    input_csv = args.input_csv
    output_ics = args.output

    printBanner()

    language = checkLanguage(args.language)

    checkIfCSVFileIsValid(input_csv)

    (header, rows) = readCSVFile(input_csv)

    cal = fillICSWithCSVData(header, rows, language)

    writeICSFile(cal, output_ics)
