# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from html.parser import HTMLParser
import codecs

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print ("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
f = codecs.open("test.html", 'r')
parser.feed(f.read())
#parser.feed('<html><head><title>Test</title></head>'
           # '<body><h1>Parse me!</h1></body></html>')