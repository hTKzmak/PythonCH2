# PythonCH2
Task: 
Скачать файлы: https://github.com/konflic/front_example/blob/master/data/books.csv и https://github.com/konflic/front_example/blob/master/data/users.json.
Написать скрипт, который из двух данных файлов будет читать данные и на их основании создаст result.json файл со структурой: https://github.com/konflic/front_example/blob/master/data/reference.json.
Идея в том что нужно раздать все книги из csv файла пользователям из списка. Книги складываются в виде словарей в массив books у каждого пользователя.
Книг изначально больше чем пользователей, поэтому раздавать нужно по принципу "максимально поровну", т.е. если книг, например 10. а пользователей 3 то распределение будет таким - 4 3 3 (один получит оставшуюся книгу).
Итоговая структура должна соответствовать стандарту json и парситься соответствующей библиотекой.
