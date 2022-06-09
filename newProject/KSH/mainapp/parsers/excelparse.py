from openpyxl import load_workbook
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
        for row in sheet.rows:
            if row[0].value is not None and row[0].value != "ФИО":
                FIO.append(row[0].value)
                i = i + 1
            if row[1].value is not None and row[1].value != "Школа":
                school.append(row[1].value)

    print('\n'.join(FIO))
    print('\n'.join(school))
    return result





