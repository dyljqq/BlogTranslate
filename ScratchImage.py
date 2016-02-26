#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'JQQ'

import urllib2
import urllib
import re
import os
from BeautifulSoup import BeautifulSoup

class Spider:

    def __init__(self):
        self.url = 'http://www.raywenderlich.com/113674/ios-animation-tutorial-getting-started'

    #获取网页内容
    def getPageContent(self):
        response = urllib2.urlopen(self.url)
        return response.read()

    def getImages(self):
        soup = BeautifulSoup(self.getPageContent())
        items = soup.findAll('img')
        index = 1
        pathName = "iOSAnimationTutorial"
        self.mkdir(pathName)

        for item in items:
            imageUrl = item.get('src')
            fTail = imageUrl.split('.').pop()
            pattern = re.compile('http', re.S)
            if (cmp(fTail, 'jpg') == 0 or cmp(fTail, 'png') == 0) and len(re.findall(pattern, imageUrl)) > 0:
                savePath = pathName + '/' + str(index) + '.' + fTail
                self.saveImageUrl(imageUrl)
            index = index + 1

    def saveImage(self, imageUrl, fileNamePath):
        try:
            u = urllib.urlopen(imageUrl)
            data = u.read()
            f = open(fileNamePath, "w+")
            f.write(data)
            f.close()
        except BaseException, e:
            print e

    def saveImageUrl(self, imageUrl):
        try:
            f = open("urls", "a")
            f.write(imageUrl + "\n")
            f.close()
        except BaseException, e:
            print e

    def mkdir(self, path):
        path = path.strip()
        isExist = os.path.exists(path)
        if not isExist:
            print "Not exist path:", path
            os.makedirs(path)
            return True
        else:
            print "Already Exist path:", path
            return False

spider = Spider()
spider.getImages()
