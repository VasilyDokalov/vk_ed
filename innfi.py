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

    # Добавляем заголовок для нового столбца
    header.append("ИНН")

    # Генерируем ИНН и добавляем его к каждой строке
    for row in data[1:]:
        inn = fake.random_int(min=100000000000, max=999999999999)  # Генерируем случайный ИНН для физлица
        row.append(str(inn).lstrip('0'))  # Преобразуем ИНН в строку и убираем ведущие нули

    # Обновляем таблицу с новыми данными
    sheet = spreadsheet.get_worksheet(0)
    sheet.update("A1", [header])  # Обновляем заголовок с новым столбцом
    sheet.update("A2", data[1:])  # Обновляем данные с новым столбцом

except FileNotFoundError:
    print("Файл с учетными данными не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    print("Подробности:", gc.auth, credentials_path)