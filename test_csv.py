#!/usr/bin/python2
# -*- coding: utf-8 -*-

import csv

Data = (
    (9,'Web clents adn server','base64,urllib'),
    (10,'Web Programing:CGI & WSGI','cgi,time,wsgire'),
    (13,'Web Services','urllib,twythen'),
)
print '*** WRITING CSV DATA'

with open('books.csv','w') as f:

    writer = csv.writer(f)
    # writer = csv.writerow(f, fieldnames=fieldnames)

    
    for record in Data:
        writer.writerow(record)
        

print '*** REVIEW OF SERVER DATA'

with open('books.csv','r') as f:
    reader = csv.reader(f)
    # print reader.line_num
    # for id,code,title,content in reader:
        # print id
        # print code
        # print title
        # print content
    for row in reader:
        print type(row)
        print row

if __name__ == '__main__':
    t = ('one','two','three')
    print ','.join(t)