import gspread
import faker
# Импортируем библиотеку google.auth.service_account
from google.auth.service_account import Credentials

# Получаем учетные данные из файла credentials.json
credentials = Credentials.from_service_account_file("client_secret_1029733915306-2uatfhu1qp6th7rj4siis8rurss1qe9h.apps.googleusercontent.com.json")

# Подключаемся к Google Sheets
spreadsheet = gspread.authorize(credentials).create("Таблица с ФИО и датами рождения")

# Задаем диапазон ячеек для заполнения
range_name = "A1:B99000"

# Генерируем данные
first_names = [faker.first_name() for _ in range(99000)]
last_names = [faker.last_name() for _ in range(99000)]
birth_dates = [faker.date_of_birth().strftime("%d.%m.%Y") for _ in range(99000)]

# Добавляем данные в таблицу
spreadsheet.values_update(range_name, [[first_name, birth_date] for first_name, birth_date in zip(first_names, birth_dates)])

# Закрываем таблицу
spreadsheet.close()