import requests
from bs4 import BeautifulSoup

with open('main.html', 'r') as htmlFile:
    content = htmlFile.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card') #finds all divs with class 'card'
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print (f'{course_name} costs {course_price}.')
