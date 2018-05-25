# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from html.parser import HTMLParser
import codecs

operator = ['+', '-', '*', '**', '/',
            '//', '%', '@', '<<', '>>',
            '&', '|', '^', '~','<','>',
            '<=','>=','==','!=']

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_decl(self, data):
        print("Decl \t\t:", data)
        
    def handle_starttag(self, tag, attrs):
        print ("Start tag \t:", tag)
        for attr in attrs:
            print("attr\t\t:", attr)

    def handle_endtag(self, tag):
        print ("End tag \t:", tag)

    def handle_data(self, data):
        if data == '\n' :
            return
        elif not data.strip():
            return
        else :
            print("Some data \t:", data)
            
    def handle_comment(self, data):
        print("Comment \t:", data)


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
f = codecs.open("test.html", 'r')
parser.feed(f.read())
#parser.feed('<html><head><title>Test</title></head>'
           # '<body><h1>Parse me!</h1></body></html>')