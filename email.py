import datetime


# словарь email
email = {
    "subject": "  Quarterly Report  ",
    "from": "  Alice.Cooper@Company.ru ",
    "to": "   bob_smith@Gmail.com   ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}


# добавляем дату отправки
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["send_date"] = send_date


# нормализация email
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()
email["subject"] = email["subject"].strip()


# извлечение логина и домена отправителя
login = email["from"].split("@")[0]
domen = email["from"].split("@")[1]
print("1. Извлечение логина и домена отправителя")
print(login)
print(domen)


# Создание сокращённой версии текста
short_body = email["body"]
short_body = short_body[0:10] + '...'
email["short_body"] = short_body


# Создаем списки доменов
personal_domains = [
    'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com',
    'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru'
]
corporate_domains = [
    'company.ru', 'corporation.com', 'university.edu',
    'organization.org', 'company.org', 'business.net'
]


#Убираем пересечения доменов
personal_set = set(personal_domains)
corporate_set = set(corporate_domains)

uniq_personal = personal_set - corporate_set
uniq_corporate = corporate_set - personal_set

personal_domains = list(uniq_personal)
corporate_domains = list(uniq_corporate)


# Проверяем «корпоративность» отправителя
if domen in corporate_domains:
    is_corporate = True

print("2. Проверяем «корпоративность» отправителя")
print(f"Domen is corporated: {is_corporate}")


# Собираем «чистый» текст сообщения
clean_body = email["body"]
clean_body = clean_body.replace("\t", " ").replace("\n", " ")
email["clean_body"] = clean_body


#Сформируем текст отправленного письма
sent_text = f'''Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}
Дата {email["send_date"]}
{email["clean_body"]}
'''
email["sent_text"] = sent_text

print("3. Сформируем текст отправленного письма")
print(email["sent_text"])