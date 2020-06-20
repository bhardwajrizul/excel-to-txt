import openpyxl

file = open('D:/file/text.txt', 'w+')

wb = openpyxl.load_workbook("C:/Users/RIZUL/PycharmProjects/cleverprogrammer_course/transactions.xlsx")

sheet = wb.active

for transaction_id, product_id, price in sheet:
    file.write(f'insert into [table] values {transaction_id.value} , {product_id.value} , {price.value}\r\n')

file.close()
