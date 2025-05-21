import csv
from datetime import datetime
import questionary
from contact import Contact

def start():
  print("", end="\n")
  file_path = questionary.text(
      "Please enter the path to the CSV file:",
      default="contacts.csv",
  ).ask()
  checkIfCSVFileIsValid(file_path)
  return readCSVFile(file_path)

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
  list_of_contacts = []
  with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)
    header = rows.pop(0)

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
      list_of_contacts.append(Contact(name, bday))
    except ValueError:
      print(
        f"Invalid date format for {name}: {bday_str}. Expected format: YYYY-MM-DD or --MM-DD.")
      continue

  return list_of_contacts
