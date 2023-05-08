import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys
import os
if not os.path.exists('sources/.xml'):
    print("file does not exist")
    sys.exit(1)
# XMLファイルを解析してroot要素を取得する
tree = ET.parse('i18n/AdGuard Applications.xml')
root = tree.getroot()

# plurals要素を取得する
plurals_elements = root.findall("./values-ja/plurals")

# strings要素を取得する
strings_elements = root.findall("./values-ja/string")

# plurals.xmlファイルに書き出す
plurals_root = ET.Element('resources')
for plurals_element in plurals_elements:
    plurals_root.append(plurals_element)
plurals_string = ET.tostring(plurals_root, encoding='utf-8', xml_declaration=True)
plurals_string = minidom.parseString(plurals_string).toprettyxml(indent='    ')
plurals_string = '\n'.join(line for line in plurals_string.split('\n') if line.strip())
with open('plurals.xml', 'w', encoding='utf-8') as f:
    f.write(plurals_string)

# strings.xmlファイルに書き出す
strings_root = ET.Element('resources')
for string_element in strings_elements:
    strings_root.append(string_element)
strings_string = ET.tostring(strings_root, encoding='utf-8', xml_declaration=True)
strings_string = minidom.parseString(strings_string).toprettyxml(indent='    ')
strings_string = '\n'.join(line for line in strings_string.split('\n') if line.strip())
with open('strings.xml', 'w', encoding='utf-8') as f:
    f.write(strings_string)
