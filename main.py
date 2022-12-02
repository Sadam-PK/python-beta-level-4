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


# --------------- QUESTION 3: THREADING --------------------
# You are required to conduct analysis on data obtained from a plant related to temperature readings.
# The file temperatures.csv contains the appropriate data required for this task.
# Write methods to generate:
#   1. Average time-lapse in readings
#   2. Average per hour temperature recording
#   3. Largest spike in data (percentage)
#   4. Overall deviation in the data

# Conduct the above calculations through two threads (each thread conducts two calculations). Measure uptime with
# and without threads. Log your results in section_four/temperature.txt using the appropriate library.

# SOLUTION STARTS HERE
# import time
# import datetime
# import threading
# import csv
#
# # read file from csv
# file = "/home/sadam/PycharmProjects/python-beta-level-4/temperature.csv"
# garbage_value = 'Ã¯Â»Â¿'
# data = {}
#
# # read data
# temp_list = []
# time_list = []
# with open(file, 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         time_check, temp = row
#         if garbage_value in time_check:
#             time_check = time_check.replace(garbage_value, '')
#         time_check = datetime.datetime.now()
#         temp = float(temp)
#         temp_list.append(temp)
#         time_list.append(time_check)
# f.close()
#
#
# # define method for time lapse
# def calculate_time_lapse(time_data):
#     assert type(time_data) == list
#     all_time_lapses = []
#     for ind in range(len(time_data)):
#         if ind == 0:
#             continue
#         lapse = (time_data[ind] - time_data[
#             ind - 1]).total_seconds()  # .total_seconds() gives the difference in seconds as a numeric value
#         all_time_lapses.append(lapse)
#     avg_time_lapse = sum(all_time_lapses) / len(all_time_lapses)
#     return avg_time_lapse
#
#
# # define method for largest spike in temperature
# def calculate_largest_spike(temperature_data):
#     pct_change = []
#     for ind in range(len(temperature_data)):
#         if ind == 0:
#             continue
#         diff = (temperature_data[ind] - temperature_data[ind - 1]) / temperature_data[ind - 1]
#         pct_change.append(diff)
#     return max(pct_change)
#
#
# # define method for calculating hourly temperature
# def calculate_hourly_temperature(time_data):
#     # for a datetime object x, x.hour gives the hour value. We collect together same hour temperature values and take
#     # average
#     time_in_hours = [time_val.hour for time_val in time_data]
#     unique_hours = set(time_in_hours)  # set() converts a list into a set of unique elements
#     avg_readings = []
#     for unique_hour in unique_hours:
#         hour_readings = []
#         for ind in range(len(time_in_hours)):
#             if time_in_hours[ind] == unique_hour:
#                 hour_readings.append(temp_list[ind])
#         avg = sum(hour_readings) / len(hour_readings)
#         avg_readings.append(round(avg, 2))  # rounding up to 2  decimal value for sake of ease of reading.
#     return avg_readings
#
#
# # define method for calculating standard deviation in temperature
# # the formula for deviation (standard deviation) is: square_root(sum((x - x_mean)^2)/total_obs)
# def calculate_deviation_temperature(temperature_data):
#     avg_temperature = sum(temperature_data) / len(temperature_data)
#     total_observations = len(temperature_data)
#     sq_diff = []
#     for value in temperature_data:
#         calc = (value - avg_temperature) ** 2
#         sq_diff.append(calc)
#     sum_squared_avg = sum(sq_diff) / total_observations
#     standard_deviation = sum_squared_avg ** 0.5
#     return standard_deviation
#
#
# # define method for first thread calculations
# def first_thread_function():
#     tl = calculate_time_lapse(time_list)
#     print('The time lapse is:', tl)
#     ls = calculate_largest_spike(temp_list)
#     print('The largest spike in temperature is:', ls)
#     return
#
#
# # define method for second thread calculations
# def second_thread_function():
#     av_temp = calculate_hourly_temperature(time_list)
#     print('Average hourly temperatures are ', av_temp)
#     std = calculate_deviation_temperature(temp_list)
#     print('Deviation in temperature is: ', std)
#     return
#
#
# def get_time(start, end):
#     return round(end - start, 10)
#
#
# def main():
#     # creating thread
#     start = time.time()
#     t1 = threading.Thread(target=first_thread_function)
#     t2 = threading.Thread(target=second_thread_function)
#     # # Starting the threads
#     t1.start()
#     t2.start()
#     # # waiting for each to finish
#     t1.join()
#     t2.join()
#     # # both threads completely executed
#     end = time.time()
#     print('With threading it took: {} seconds.'.format(get_time(start, end)))
#     start2 = time.time()
#     first_thread_function()
#     second_thread_function()
#     end2 = time.time()
#     print('Without threading it took: {} seconds'.format(get_time(start2, end2)))
#
#
# main()

# #---------- Numpy --------------

import numpy as np
#
# mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(f'Matrix = {mat}')
# print(f'Matrix size = {mat.shape}')
#
# new_mat = mat.reshape(1, 9)
# print(new_mat)
# print(f'Matrix size = {new_mat.shape}')
#
# trans_new_mat = new_mat.T
# print(trans_new_mat)
# print(trans_new_mat.T)
#
# diag = np.diag([1, 2, 3, 4])
# print(diag)
#
# identity = np.identity(10)
# print(identity)
#
# seq = np.arange(start=0, stop=11, step=2)
# print(seq)
#
# reshape_seq = seq.reshape(2, 3)
# print(reshape_seq)
#
# rand1 = np.random.rand(10)
# print(rand1)
#
# rand2 = np.random.rand(10, 10)
# print(rand2)
#
# new_arr = np.array([10, 2, 3, 6, 4, 30, 22])
# print(f'max in array is {max(new_arr)} is at index {new_arr.argmax()}')
# print('min in array is {} is at index {}'.format(new_arr.min(), new_arr.argmin()))

#
# import time
#
# my_mat = np.random.rand(100, 100)
# another_mat = np.random.rand(100, 100)
# start = time.time()
#
# dot_mod = my_mat.dot(another_mat)
# end = time.time()
#
# print(f'it took {round(end - start, 4)} seconds to calculate the dot product.')
