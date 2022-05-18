from openpyxl import load_workbook

def excelparsing(link):
    book = load_workbook(link)
    sheets = book.sheetnames
    for sheet in sheets:
        sheet = book.active

    FIO = []
    school = []
    result = ''
    for row in sheet.rows:
        if row[0].value != None and row[0].value != "ФИО":
            FIO.append(row[0].value)
        if row[1].value != None and row[1].value != "Школа":
            school.append(row[1].value)
    print("{}\n{} \t\n{} ".format(sheet.title,'\n'.join(FIO),'\n'.join(school)))
    return result
link = str(input("Вставьте ссылку на документ:"))
excelparsing(link)
