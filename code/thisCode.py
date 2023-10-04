import json
from csv import DictReader
from Checkpoint2.data import JSON_FILE_PATH
from Checkpoint2.data import CSV_FILE_PATH

# Чтение двух файлов (users.json и books.csv)
with open(JSON_FILE_PATH, "r") as json_file:
    users = json.loads(json_file.read())

with open(CSV_FILE_PATH, newline="") as csv_file:
    reader = DictReader(csv_file)
    rows = list(reader)

# Распределение книг максимально поровну по пользователям
num_books = len(rows)
num_users = len(users)
books_per_user = num_books // num_users
remaining_books = num_books % num_users

for i in range(num_users):
    user = users[i]
    user["books"] = []

    for j in range(books_per_user):
        book = rows[i * books_per_user + j]
        user["books"].append(book)

    # Раздача оставшихся книг одному пользователю
    if remaining_books > 0:
        book = rows[num_users * books_per_user + i]
        user["books"].append(book)
        remaining_books -= 1


# Запись в result.json
result = []

for user in users:
    result_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user["books"]
    }
    result.append(result_user)

with open("result.json", "w") as file:
    json.dump(result, file, indent=4)
