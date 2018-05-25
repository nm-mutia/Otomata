from html.parser import HTMLParser

total = 0
startag = 0
endtag = 0
datax = 0
comment = 0
decl = 0
attrb = 0

class MyHTMLParser(HTMLParser):
    def handle_decl(self, data):
        print("Decl \t\t:", data)
        global decl
        decl = decl + 1
        
    def handle_starttag(self, tag, attrs):
        print ("Start tag \t:", tag)
        global startag
        global attrb
        startag = startag + 1
        for attr in attrs:
            print("attr\t\t:", attr)
            attrb = attrb + 1

    def handle_endtag(self, tag):
        print ("End tag \t:", tag)
        global endtag
        endtag = endtag + 1

    def handle_data(self, data):
        if data == '\n' :
            return
        elif not data.strip():
            return
        else :
            print("Some data \t:", data)
            global datax
            datax = datax + 1
            
    def handle_comment(self, data):
        print("Comment \t:", data)
        global comment
        comment = comment + 1

           

parser = MyHTMLParser()
f = open("test.html", 'r') 
parser.feed(f.read())

total = decl + startag + attrb + datax + endtag + comment

print ('\n')
print (' - decl tag : ', decl)
print (' - start tag : ', startag)
print (' - attr : ', attrb)
print (' - data : ', datax)
print (' - end tag : ', endtag)
print (' - comment : ', comment)
print (' - total : ', total)
        
        
        
        
        
        