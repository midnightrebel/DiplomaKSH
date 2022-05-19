from openpyxl import load_workbook
import psycopg2
from config import host, user,password,db_name
def excelparsing(link):
    book = load_workbook(link)
    sheets = book.worksheets
    FIO = []
    school = []
    subject = []
    result = ''
    for sheet in sheets:
        subject.append(sheet)
    for i in range(0, len(subject)):
        sheet = subject[i]
        print(subject[i].title)
        for row in sheet.rows:
            if row[0].value is not None and row[0].value != "ФИО":
                FIO.append(row[0].value)
                i = i + 1
            if row[1].value is not None and row[1].value != "Школа":
                school.append(row[1].value)

    print('\n'.join(FIO))
    print('\n'.join(school))
    return result


link = str(input("Вставьте ссылку на документ:"))

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        db_name = db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO Students"""
        )
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Connection closed.")

excelparsing(link)
