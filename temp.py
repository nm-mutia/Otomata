# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from html.parser import HTMLParser
import codecs

reserve = ['false','class','finally','is','return'
           ,'none','continue','for','lambda','try'
           ,'true','def','from','nonlocal','while'
           ,'and','del','global','not','with','as'
           ,'elif','if','or','yield','assert','else'
           ,'import','pass','break','except','in','raise']

operator = ['+', '-', '*', '**', '/',
            '//', '%', '@', '<<', '>>',
            '&', '|', '^', '~','<','>',
            '<=','>=','==','!=']

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Encountered a start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print ("Encountered an end tag :", tag)

    def handle_data(self, data):
        if data == reserve :
            print("Reserved Word : ", data)
        elif data == operator :
            print("Operator : ", data)
        else :
            print("Encountered some data  :", data)



# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
f = codecs.open("test.html", 'r')
parser.feed(f.read())
#parser.feed('<html><head><title>Test</title></head>'
           # '<body><h1>Parse me!</h1></body></html>')