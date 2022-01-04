from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from student_info.models import Student, Module, Staff

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

DATE_FORMAT = "%Y-%m-%d"


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data"

    def handle(self, *args, **options):
        if Student.objects.exists() or Module.objects.exists() or Staff.objects.exists():
            print('Data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Load Staff Data
        print("Loading staff data")
        for row in DictReader(open("./staff_data.csv", encoding="utf-8-sig")):
            staff = Staff()
            staff.name = row["name"]
            staff.save()

        # Load Module Data
        print("Loading module data")
        for row in DictReader(open("./module_data.csv", encoding="utf-8-sig")):
            module = Module()
            module.code = row["code"]
            module.name = row["name"]
            module.lecturer = Staff.objects.get(name=row["lecturer"])
            module.save()

        # Load Student Data
        print("Loading student data")
        for row in DictReader(open('./student_data.csv', encoding="utf-8-sig")):
            student = Student()
            student.name = row["name"]
            student.address = row["address"]
            student.sex = row["sex"]
            day, month, year = row["DOB"].split("/")
            student.dob = datetime(int(year), int(
                month), int(day)).strftime(DATE_FORMAT)
            student.save()
            raw_module_codes = row["modules"]
            module_codes = [
                code for code in raw_module_codes.split(" | ") if code
            ]
            for code in module_codes:
                m_code = Module.objects.get(code=code)
                student.modules.add(m_code)
            student.save()
