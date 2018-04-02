#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

import json
import sys
import csv

# Input file path of log file to be parsed
input_file = "log/file/path"

def main():
    """ This funtion takes in a json file and parses
        the api_key, status and time_iso elements
        from the log data and writes to a csv.
     """ 
    csv_list = []
    with open(input_file) as f:
        for line in f:
            try:
                message_data = json.loads(json.loads(line)['_source']['message'])
                my_data = {'response_time':  message_data['response_time'],
                           'api_key': message_data['api_key'],
                           'status': message_data['status'],
                           'time_iso': message_data['time_iso']}
                csv_list.append(my_data)
            except:
                pass

    with open("csv_output.csv", "w") as g:
        fieldnames = ['api_key', 'status',  'response_time', 'time_iso']
        writer = csv.DictWriter(g, fieldnames=fieldnames)
        writer.writerows(csv_list)

if __name__ == "__main__":
    main()

