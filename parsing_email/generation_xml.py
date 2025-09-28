import xml.etree.ElementTree as ET

# Создаем корневой элемент
root = ET.Element("Statistics")
date = ET.SubElement(root, "Date")
date.text = "2025-01-21"

views = ET.SubElement(root, "Views")
views.text = "150"

clicks = ET.SubElement(root, "Clicks")
clicks.text = "25"

# Генерируем строку XML
xml_data = ET.tostring(root, encoding="utf-8", method="xml").decode()

# Сохраняем XML в файл
with open("statistics.xml", "w") as file:
    file.write(xml_data)

print("XML-файл 'statistics.xml' сгенерирован.")