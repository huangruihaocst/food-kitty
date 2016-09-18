from django.shortcuts import render
import re
import json
import urllib.parse

__author__ = 'huang'


def search(request):
    return render(request, 'search.html', {})


def results(request):
    keywords = request.GET['keywords']
    words = re.split('[^-a-zA-Z0-9]', keywords)
    file = open('data.txt', 'r')
    entire = json.loads(file.read())
    item_list = []
    for food in entire:
        check = True
        for word in words:
            if not substring_of_element(word, food['keywords']):
                check = False
                break
        if check:
            temp_dict = dict()
            temp_dict['name'] = food['name']
            temp_dict['link'] = urllib.parse.quote('/FoodKitty/details/' + food['name'])
            temp_dict['first'] = food['content'][0]
            item_list.append(temp_dict)
    return render(request, 'results.html', {'entries': item_list, 'keywords': keywords})


def details(request, name):
    file = open('data.txt', 'r')
    entire = json.loads(file.read())
    content_list = []
    link = ''
    for food in entire:
        if food['name'] == name:
            content_list = food['content']
            link = food['link']
    return render(request, 'details.html', {'name': name, 'content': content_list, 'link': link})


def advanced(request):
    return render(request, 'advanced.html', {})


def advanced_search(request):
    keywords = request.GET['keywords']
    checkbox_list = list(request.REQUEST.getlist('checkbox_list'))
    select_beef = False
    select_chicken = False
    if '0' in checkbox_list:
        select_beef = True
    if '1' in checkbox_list:
        select_chicken = True
    words = re.split('[^-a-zA-Z0-9]', keywords)
    file = open('data.txt', 'r')
    entire = json.loads(file.read())
    item_list = []
    for food in entire:
        check = True
        if food['father'] == 'beef' and not select_beef:
            check = False
        if food['father'] == 'chicken' and not select_chicken:
            check = False
        for word in words:
            if not substring_of_element(word, food['keywords']):
                check = False
                break
        if check:
            temp_dict = dict()
            temp_dict['name'] = food['name']
            temp_dict['link'] = urllib.parse.quote('/FoodKitty/details/' + food['name'])
            temp_dict['first'] = food['content'][0]
            item_list.append(temp_dict)
    return render(request, 'results.html', {'entries': item_list, 'keywords': keywords})


def about(request):
    return render(request, 'about.html', {})


def for_help(request):
    return render(request, 'help.html', {})


def substring_of_element(word, my_list):
    for element in my_list:
        if element.find(word) != -1:
            return True
    return False
