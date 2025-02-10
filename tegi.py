from bs4 import BeautifulSoup
import re

def check_unclosed_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    unclosed_tags = []

    # Проверяем все теги в документе
    for tag in soup.find_all(True):  # True находит все теги
        # Если тег не является пустым элементом и у него нет закрывающего тега
        if not tag.is_empty_element and tag.name not in unclosed_tags:
            # Проверяем, есть ли у тега закрывающий тег
            if tag.find_all(tag.name):
                unclosed_tags.append(tag.name)

    return unclosed_tags

def find_unclosed_tags_with_line(html):
    lines = html.splitlines()

    def findall_with_line(pattern, string):
        matches = []
        for i, line in enumerate(string.splitlines(), 1):
            for match in re.finditer(pattern, line):
                matches.append((match.group(1), i, match.span()[1]))
        return matches

# Пример HTML-кода для проверки
html_code = """
<!DOCTYPE html>
<html lang="ru">
<head>
</head>
<body>
    <h1>Привет, мир!<h1>
    <p>Это пример HTML-кода с незакрытым тегом h1.</p>
</body>
</html>
"""

unclosed_tags = check_unclosed_tags(html_code)

if unclosed_tags:
    for tag, line in unclosed_tags:
        print(f"Незакрытый тег '{tag}' найден в строке {line}")
else:
    print("Все теги закрыты корректно.")