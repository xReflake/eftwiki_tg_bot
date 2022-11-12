import requests
from bs4 import BeautifulSoup as BS
import handlers.client

#link = "https://escapefromtarkov.fandom.com/ru/wiki/%D0%9F%D0%BE%D1%80%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5"
# r = requests.get(link)
# soup = BS(r.content, 'lxml')
# page_h1 = soup.find("div", class_="mw-parser-output")
# page_h1 = page_h1.text.strip()

def parse_name_quest(link,soup):
    title = soup.title
    title = title.string
    title = title.replace("— Escape from Tarkov Wiki","")
    title = title.strip()
    return title

def parse_target(link,soup):
    page_h1 = soup.find("div", class_="mw-parser-output")
    page_h1 = page_h1.text.strip()
    pos = page_h1.find('Цель(и)[]')
    part1 = page_h1[pos:]
    #part2 = part1[pos:]
    pos2 = part1.find('П | Р')
    part2 = part1[:pos2]
    # pos3 = part3.find('Цель(и)')
    # part4 = part3[pos3:]
    part_last = part2.replace("[]","")
    return part_last

def parse_reward(link,soup):
    page_h1 = soup.find("div", class_="mw-parser-output")
    page_h1 = page_h1.text.strip()
    pos = page_h1.find('Награда[]')
    part1 = page_h1[pos:]
    pos2 = part1.find('П | Р')
    part2 = part1[:pos2]
    # pos3 = part3.find('Награда')
    # part4 = part3[pos3:]
    part_last = part2.replace("[]","")
    return part_last

def parse_implementation(link,soup):
    page_h1 = soup.find("div", class_="mw-parser-output")
    page_h1 = page_h1.text.strip()
    pos = page_h1.find('Награда[]')
    part1 = page_h1[pos:]
    pos2 = page_h1.find('\n')
    part2 = part1[pos2:]
    pos3 = part2.find('Список компонентов:[]')
    part3 = part2[:pos3]
    # pos3 = part3.find('Награда')
    # part4 = part3[pos3:]
    part_last = part3.replace("[]","")
    pos5 = part_last.find('»')
    part5 = part_last[pos5:]
    pos6 = part5.find("Выполнение")
    part6 = part5[pos6:]
    return part6

#print("Название квеста: " + parse_name_quest(link) + "\n")
#print(parse_target(link))
#print (parse_reward(link))
#print(parse_implementation(link))