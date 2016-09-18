import requests
import re
import json

__author__ = 'huang'

mainList = []

# list of beef
urlBeefList = 'https://en.wikipedia.org/wiki/List_of_beef_dishes'
urlBeef = 'https://en.wikipedia.org'
rawHtmlBeef = requests.get(urlBeefList).text
beefList = re.search('<div class="div-col columns column-width" .*?>(.*?)</div>', rawHtmlBeef, re.S)
beefListString = beefList.group(1)
beefEnterList = re.findall('<li>(.*?)</li>', beefListString, re.S)
beefLinkList = []
beefNameList = []
beefCount = 0
for i in beefEnterList:
    beefInfo = re.search('<a href="(.*?)" .*?>(.*?)</a>.*', i, re.S)
    beefLinkList.append(urlBeef + beefInfo.group(1))
    beefNameList.append(beefInfo.group(2))
    beefCount += 1
nameCount = 0
for url in beefLinkList:  # every kind of beef
    rawHtml = requests.get(url).text
    contentList = re.findall('<p>(.*?)</p>', rawHtml, re.S)
    words = []
    passages = []
    for content in contentList:
        pureContent = re.sub('<.*?>', '', content)
        pureContent = re.sub('\[\d+\]', '', pureContent)
        pureContent = '  ' + pureContent
        passages.append(pureContent)
        paragraph = re.split('[^-a-zA-Z0-9]', pureContent)
        paragraph = list(filter(lambda x: x != '', paragraph))
        words.extend(paragraph)
    keywords = []
    for i in words:
        if len(i) >= 3:
            temp = words[:]
            remains = list(filter(lambda x: x == i, temp))
            if len(remains) >= 3:
                keywords.append(i)
    keywords.append(beefNameList[nameCount])
    keywords = list(set(keywords))
    tempDictionary = dict()
    tempDictionary['name'] = beefNameList[nameCount]
    tempDictionary['link'] = beefLinkList[nameCount]
    tempDictionary['keywords'] = keywords
    tempDictionary['content'] = passages
    tempDictionary['father'] = 'beef'
    # print(tempDictionary)
    mainList.append(tempDictionary)
    nameCount += 1

# list of chicken
urlChickenList = 'https://en.wikipedia.org/wiki/List_of_chicken_dishes'
urlChicken = 'https://en.wikipedia.org'
rawHtmlChicken = requests.get(urlChickenList).text
chickenList = re.search('<div class="div-col columns column-width" .*?>(.*?)</div>', rawHtmlChicken, re.S)
chickenListString = chickenList.group(1)
chickenEnterList = re.findall('<li>(.*?)</li>', chickenListString, re.S)
chickenLinkList = []
chickenNameList = []
chickenCount = 0
for i in chickenEnterList:
    chickenInfo = re.search('<a href="(.*?)" .*?>(.*?)</a>.*', i, re.S)
    chickenLinkList.append(urlChicken + chickenInfo.group(1))
    chickenNameList.append(chickenInfo.group(2))
    chickenCount += 1
nameCount = 0
for url in chickenLinkList:  # every kind of chicken
    rawHtml = requests.get(url).text
    contentList = re.findall('<p>(.*?)</p>', rawHtml, re.S)
    words = []
    passages = []
    for content in contentList:
        pureContent = re.sub('<.*?>', '', content)
        pureContent = re.sub('\[\d+\]', '', pureContent)
        pureContent = '  ' + pureContent
        passages.append(pureContent)
        paragraph = re.split('[^a-zA-Z0-9\-]', pureContent)
        paragraph = list(filter(lambda x: x != '', paragraph))
        words.extend(paragraph)
    keywords = []
    for i in words:
        if len(i) >= 3:
            temp = words[:]
            remains = list(filter(lambda x: x == i, temp))
            if len(remains) >= 3:
                keywords.append(i)
    keywords.append(chickenNameList[nameCount])
    keywords = list(set(keywords))
    tempDictionary = dict()
    tempDictionary['name'] = chickenNameList[nameCount]
    tempDictionary['link'] = chickenLinkList[nameCount]
    tempDictionary['keywords'] = keywords
    tempDictionary['content'] = passages
    tempDictionary['father'] = 'chicken'
    # print(tempDictionary)
    mainList.append(tempDictionary)
    nameCount += 1

storeString = str(json.dumps(mainList))
file = open('data.txt', 'w')
file.write(storeString)
file.close()
