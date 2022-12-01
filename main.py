# from lxml import etree
#
#
# def parse_book_xml(xml_file):
#     with open(xml_file) as fobj:
#         xml = fobj.read()
#     root = etree.fromstring(xml)
#     book_dict = {}
#     books = []
#
#     for book in root.getchildren():
#         for elem in book.getchildren():
#             if elem.text:
#                 text = elem.text
#             else:
#                 text = ''
#             if elem.tag == 'author':
#                 last_name, first_name = text.split(',')
#                 print(elem.tag + ':', first_name, last_name)
#             else:
#                 print(elem.tag+': '+text)
#             book_dict[elem.tag] = text
#         if book.tag == 'book':
#             books.append(book_dict)
#             book_dict = {}
#
#
# parse_book_xml('books.xml')
#

# #-------- Configuration -------------

# from configparser import ConfigParser
#
# config = ConfigParser()
#
# config['DEFAULT'] = {
#     'title': 'Hello World',
#     'compression': 'yes',
#     'compression_level': 9,
# }
# config['database'] = {}
# database = config['database']
# database['host'] = '127.0.0.1'
# database['user'] = 'username'
# database['pass'] = 'password'
# database['keep-alive'] = 'no'
#
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)
#

# #-------- Threading -------------
#
# import datetime
# import threading
#
#
# def get_cubic(num):
#     print(datetime.datetime.now())
#     print(num * num * num)
#
#
# def get_inverse(num):
#     print(datetime.datetime.now())
#     print(1 / num)
#
#
# get_cubic(10)
# get_inverse(10)
#
#
# t1 = threading.Thread(target=get_cubic, args=(10,))
# t2 = threading.Thread(target=get_inverse, args=(10,))
#
# t2.start()
# t1.start()
#
# t2.join()
# t1.join()
#
# print('Done!')




