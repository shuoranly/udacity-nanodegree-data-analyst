#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def convertPhone(phone):
    # First step i'm going to remove all non number characters
    phone = re.sub('\D', '', phone)
    if len(phone) == 10:
        phone = "+38" + phone
    elif len(phone) == 7:
        phone = "+38044" + phone
    elif len(phone) == 12:
        phone = "+" + phone
    elif len(phone) == 11:
        phone = "+3" + phone
    elif len(phone) == 9:
        phone = "+380" + phone

    if len(phone) == 13:
        phone = phone[0:4] + ' ' + phone[4:6] + ' ' + phone[6:9] + '-' + phone[9:11] + '-' + phone[11:13]
    return phone

def key_type(element, keys):
    if element.tag == "tag" and 'k' in element.attrib:
        if element.attrib['k'] in ['phone', 'contact:phone']:
            s = re.split('[,;]', element.attrib['v'])
            data = []
            for i in s:
                data.append(convertPhone(i)) 
            print data
            print s
    return keys



def process_map(filename):
    data = {}
    for _, element in ET.iterparse(filename):
        data = key_type(element, data)

    return data



def test():
    keys = process_map('map')
    pprint.pprint(keys)

if __name__ == "__main__":
    test()