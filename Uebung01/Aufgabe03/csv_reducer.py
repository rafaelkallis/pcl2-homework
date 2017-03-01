# Rafael Kallis 14-708-887

import csv
import re
import datetime


# Takes a file and parses its content into a string
def file_to_string(filename):
    file = open(filename, mode='r')
    content = file.read()
    file.close()
    return content


# Writes a given dictionary list to a file
def dict_list_to_csv(dict_list, filename):
    file = open(filename, mode='w')
    fieldnames = ['cdatetime', 'address', 'district', 'crimedescr']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict_list)
    file.close()
    return


# Maps the csv into a list of rows
def to_row_list(text=''):
    return re.split(pattern='\n', string=text)


# Maps a csv file's content into a dictionary list
def csv_to_dict_list(filename):
    csv_text = file_to_string(filename)
    csv_rows = to_row_list(csv_text)
    csv_reader = csv.DictReader(csv_rows)
    return list(csv_reader)


# Fragments the dictionary list vertically
def vertical_fragment_dict_list(dict_list):
    return list(map(lambda dict: {
        'cdatetime': dict['cdatetime'],
        'address': dict['address'],
        'district': dict['district'],
        'crimedescr': dict['crimedescr']
    }, dict_list))


# Checks if the given datetime is between 2:00 and 13:00
def is_datetime_between_two_and_thirteen_o_clock(datetime_):
    two_o_clock = datetime.time(2, 0)
    thirteen_o_clock = datetime.time(13, 0)
    return two_o_clock < datetime_.time() < thirteen_o_clock


# Filters all entries in the dictionary list which have a timestamp not between 2:00 and 13:00
def filter_time(dict_list):
    return list(filter(lambda dict: is_datetime_between_two_and_thirteen_o_clock(
        datetime.datetime.strptime(dict['cdatetime'], '%m/%j/%y %H:%M')), dict_list))


# Filters all entries in the dictionary list which have a crime description containing the word "BURGLARY"
def filter_crime(dict_list):
    return list(filter(lambda dict: True if "BURGLARY" in dict['crimedescr'] else False, dict_list))


# Reads a csv file and writes modified content
def modify_csv_file(filename):
    dict_list = csv_to_dict_list(filename)
    dict_list_fragment = vertical_fragment_dict_list(dict_list)
    filtered_time = filter_time(dict_list_fragment)
    filtered_crime = filter_crime(filtered_time)
    dict_list_to_csv(filtered_crime, filename)
    return
