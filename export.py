from datetime import datetime
from csv_wrapper import start as start_csv
from vcf_wrapper import start as start_vcf
from icalendar import Calendar, Event

import questionary
import pyfiglet
import pytz

possible_placeholders = [
    "{name} - The full name of the person"
]

def populate_template(summary_template, contact):
    """
    Populates the summary template with the contact's name.
    """
    placeholders = {}
    for entry in possible_placeholders:
        key = entry.split('}')[0][1:]
        value = getattr(contact, key, "")
        placeholders[key] = value
    return summary_template.format(**placeholders)

def populate_ics_file(list_of_contacts, summary_template, verbose):
    """
    Populates the iCalendar file with birthday events for each contact.
    :param list_of_contacts: List of contacts with their birthdays
    :param summary_template: Template for the event summary
    :return: iCalendar object
    """
    cal = Calendar()
    cal.add('prodid', '-//GCBE//https://github.com/IamPekka058/google-calendar-birthday-export//')
    cal.add('version', '2.0')

    count = 0

    for contact in list_of_contacts:
        birthday_dt = contact.birthday

        event = Event()
        event.add('summary', populate_template(summary_template, contact))
        event.add('dtstart', datetime(birthday_dt.year, birthday_dt.month, birthday_dt.day).date())
        event.add('dtstamp', datetime.now(tz=pytz.UTC))
        event.add('rrule', {'freq': 'yearly'})
        event.add('transp', 'TRANSPARENT')
        cal.add_component(event)
        if verbose:
            print(f"Added birthday for {contact.name} on {birthday_dt.strftime('%Y-%m-%d')}", end="\n")
        count += 1

    print(" " * 100, end="\r")
    print(f"Added birthdays for {count} people.")
    return cal

def writeICSFile(cal, output_file):
    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())
    print(f"iCalendar file {output_file} created successfully.")

def printBanner():
    ascii_banner = pyfiglet.figlet_format("IamPekka058")
    print(ascii_banner)

def configurationDialog():
    print("Welcome to the Google Calendar Birthday Exporter!")
    print("This program will help you export your birthday list to Google Calendar.")
    print("", end="\n")
    file_type = questionary.select(
        "Do you want to use a CSV file or a VCF file?",
        choices=["CSV file", "VCF file"],
    ).ask()
    print("", end="\n")
    if file_type == None:
        print("You didn't select a file type.")
        exit(1)
    file_type = file_type.lower()
    print("You can use the following placeholders in the summary:")
    for placeholder in possible_placeholders:
        print(f"{placeholder}")
    print("", end="\n")
    while True:
        summary_template = questionary.text(
            "Please enter the summary template:",
            default="Birthday {name}",
            validate=lambda text: len(text) > 0,
        ).ask()
        confirm = questionary.confirm(
            f'You entered: "{summary_template}". Is this correct?'
        ).ask()
        if confirm:
            break
    return summary_template, file_type

if __name__ == '__main__':
    printBanner()

    summary_template, file_type = configurationDialog()

    list_of_contacts = []

    if file_type == "csv file":
        list_of_contacts = start_csv()
    elif file_type == "vcf file":
        list_of_contacts = start_vcf()

    print("", end="\n")

    while True:
        output_file = questionary.text(
            "Please enter the output file name:",
            default="birthdays.ics",
            validate=lambda text: text.endswith('.ics') and len(text) > 0,
        ).ask()
        confirm = questionary.confirm(
            f'You entered: "{output_file}". Is this correct?'
        ).ask()
        if confirm:
            break

    print("", end="\n")

    verbose = questionary.confirm(
        "Do you want to see the details of the contacts?",
        default=False,
    ).ask()

    cal = populate_ics_file(list_of_contacts, summary_template, verbose)

    writeICSFile(cal, output_file)
