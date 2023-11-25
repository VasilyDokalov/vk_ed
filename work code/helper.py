import gspread
from faker import Faker

credentials_path = "C:/kekulon-9a5b2af128d6.json"

try:
    gc = gspread.service_account(filename=credentials_path)

    spreadsheet = gc.create("table")
    spreadsheet.share("mistixmag1@gmail.com", perm_type="user", role="writer")

    fake = Faker('ru_RU')
    data = [[f"{fake.first_name()} {fake.last_name()}", fake.date_of_birth().strftime("%d.%m.%Y")] for _ in range(99000)]

    sheet = spreadsheet.get_worksheet(0)
    sheet.insert_rows(data)

except FileNotFoundError:
    print("Файл с учетными данными не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
