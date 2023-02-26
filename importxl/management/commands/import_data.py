from django.core.management.base import BaseCommand
import pandas as pd
from importxl.models import Student

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Add bulk data')

    def handle(self, *args, **kwargs):
        my_file = kwargs['file']
        excel_file = pd.ExcelFile(my_file)
        all_sheets = excel_file.sheet_names
        df = pd.read_excel(my_file, index_col=None, sheet_name='Sheet1')
        data_index = df.columns.get_loc('std_id')
        for row in df.values:
            student_qs = Student.objects.create(std_id=row[data_index],student_name=row[data_index+1],contact_number=row[data_index+2])