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
#     return books
#
#
# my_books = parse_book_xml('books.xml')
