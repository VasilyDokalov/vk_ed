import gspread
from faker import Faker

# Укажите путь к вашему JSON-файлу с учетными данными
credentials_path = "C:/kekulon-9a5b2af128d6.json"

try:
    # Подключаемся к Google таблицам
    gc = gspread.service_account(filename=credentials_path)

    # Получаем объект существующей таблицы
    spreadsheet = gc.create("99000")
    spreadsheet.share("mistixmag1@gmail.com", perm_type="user", role="writer")

    # Генерим данные
    fake = Faker('ru_RU')
    data = [[fake.first_name(), fake.last_name(), fake.date_of_birth().strftime("%d.%m.%Y")] for _ in range(99000)]

    # Добавляем данные в таблицу
    sheet = spreadsheet.get_worksheet(0)
    sheet.insert_rows(data)

except FileNotFoundError:
    print("Файл с учетными данными не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")