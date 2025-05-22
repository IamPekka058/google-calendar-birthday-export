from datetime import datetime

import vobject
import os
import questionary
from contact import Contact

def start():
  print("", end="\n")
  file_path = questionary.text(
      "Please enter the path to the VCF file:",
      default="contacts.vcf",
  ).ask()
  checkIfVcfFileIsValid(file_path)
  return read_vcf_file(file_path)


def checkIfVcfFileIsValid(file_path):
  print(f"Checking if file is valid: []:", end="\r")
  if not os.path.isfile(file_path):
    print(f"Checking if file is valid: [✖]", end="\n")
    print(f"The file {file_path} does not exist.")
    exit(1)
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      found_valid = False
      for vcard in vobject.readComponents(file, allowQP=True):
        name = vcard.fn.value if hasattr(vcard, 'fn') else None
        bday = vcard.bday.value if hasattr(vcard, 'bday') else None
        if name and bday:
          found_valid = True
          break
      if not found_valid:
        print("The VCF file does not contain any valid vCard (with either fullname or birthday) entries.")
        exit(1)
    print("Checking if file is valid: [✓]", end="\n")
  except Exception as e:
    print(f"An error ({e.args}) occurred while reading the file {file_path}.")
    exit(1)


def read_vcf_file(file_path):
  # Reads a vCard file and extracts the name and birthday
  # fn = Full Name
  # bday = Birthday
  list_of_contacts = []
  with open(file_path, 'r', encoding='utf-8') as file:
    for vcard in vobject.readComponents(file, allowQP=True):
      name = vcard.fn.value if hasattr(vcard, 'fn') else None
      bday = vcard.bday.value if hasattr(vcard, 'bday') else None

      if bday is not None:
        try:
          bday = datetime.strptime(bday, "%Y%m%d")
        except ValueError:
          bday = datetime.strptime(bday, "%Y-%m-%d")

      if not name or not bday:
        continue
      list_of_contacts.append(Contact(name, bday))
  return list_of_contacts
