import gspread
from faker import Faker

# Укажите путь к вашему JSON-файлу с учетными данными
credentials_path = "C:/kekulon-9a5b2af128d6.json"

try:
    # Подключаемся к Google Sheets
    gc = gspread.service_account(filename=credentials_path)

    # Получаем объект существующей таблицы
    spreadsheet = gc.open("99000")  # Укажите имя вашей действующей таблицы

    # Генерируем данные
    fake = Faker('ru_RU')
    data = spreadsheet.sheet1.get_all_values()  # Получаем все текущие данные из листа
    header = data[0]
    header.append("ИНН")  # Добавляем заголовок для нового столбца

    for row in data[1:]:
        inn = fake.random_int(min=1000000000, max=9999999999)  # Генерируем случайный ИНН
        row.append(str(inn))  # Преобразуем ИНН в строку и добавляем к текущей строке

    # Обновляем таблицу с новыми данными
    sheet = spreadsheet.get_worksheet(0)
    sheet.update("E1", [header])  # Обновляем заголовок с новым столбцом
    sheet.update("E2", data[1:])  # Обновляем данные с новым столбцом

except FileNotFoundError:
    print("Файл с учетными данными не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    print("Подробности:", gc.auth, credentials_path)