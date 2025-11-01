import datetime


# словарь email
email = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "  lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam"
}


# добавляем дату отправки
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["send_date"] = send_date


# нормализация email
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()


# извлечение логина и домена отправителя
login = email["from"].split("@")[0]
domen = email["from"].split("@")[1]
print("1. Извлечение логина и домена отправителя")
print(f"login: {login}")
print(f"domen: {domen}")


# Создание сокращённой версии текста
email["short_body"] = email["body"][:10] + '...'


# Создаем списки доменов
personal_domains = [
    'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com',
    'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru', 'inbox.ru'
]
corporate_domains = [
    'company.ru', 'corporation.com', 'university.edu',
    'organization.org', 'company.org', 'business.net', 'business.net'
]
personal_domains = list(set(personal_domains))
corporate_domains = list(set(corporate_domains))
print(f"personal_domains: {personal_domains}")
print(f"corporate_domains: {corporate_domains}")

#Убираем пересечения доменов

common_domains = set(personal_domains) & set (corporate_domains)
if common_domains:
    print(f"common_domains: {common_domains}")


# Проверяем «корпоративность» отправителя
is_corporate = domen in corporate_domains

print("2. Проверяем «корпоративность» отправителя")
print(f"Domen is corporated: {is_corporate}")


# Собираем «чистый» текст сообщения
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")


#Сформируем текст отправленного письма
sent_text = f'''Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}
Дата {email["send_date"]}
{email["clean_body"]}
'''
email["sent_text"] = sent_text

print("3. Сформируем текст отправленного письма")
print(email["sent_text"])

#Рассчитаем количество страниц печати
text_for_print = email["sent_text"]
length = len(text_for_print)
pages = (length + 499) // 500

print(f"4. Количество страниц: {pages}")


#Проверка пустоты темы и тела письма
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

print(f"5. Тема пуста: {is_subject_empty}")
print(f"6. Тело пустое: {is_body_empty}")


#Создаем маску email
masked_form = login[:2] + "***@" + domen
email["masked_form"] = masked_form

print(f"7. Маска email: {email["masked_form"]}")


#Удаляем лишние домены
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

print(f"8. Персональные домены после чистки: {personal_domains}")

