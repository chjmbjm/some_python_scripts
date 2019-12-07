#!/usr/bin/env python3

import requests
import sys
import bs4
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
URL = 'https://ketqua.net'


__doc__ == '''
Requirement:
Check if two last digits of input numbers are match with two last digits of
lottery result on ketqua.net.
If no input numbers match, print all lottery result.

Command: python3 bingo.py [NUMBER 1] [NUMBER 2] ...
'''


ids = [
    'rs_0_0',
    'rs_1_0',
    'rs_2_0', 'rs_2_1',
    'rs_3_0', 'rs_3_1', 'rs_3_2', 'rs_3_3', 'rs_3_4', 'rs_3_5',
    'rs_4_0', 'rs_4_1', 'rs_4_2', 'rs_4_3',
    'rs_5_0', 'rs_5_1', 'rs_5_2', 'rs_5_3', 'rs_5_4', 'rs_5_5',
    'rs_6_0', 'rs_6_1', 'rs_6_2',
    'rs_7_0', 'rs_7_1', 'rs_7_2', 'rs_7_3'
]

kqxs = '''
Giải đặc biệt: {}
Giải nhất: {}
Giải nhì: {} {}
Giải ba: {} {} {} {} {} {}
Giải bốn: {} {} {} {}
Giải năm: {} {} {} {} {} {}
Giải sáu: {} {} {}
Giải bảy: {} {} {} {}
'''


def lottery_result():
    result = []

    r = requests.get(URL)

    soup = bs4.BeautifulSoup(r.text, 'lxml')

    table = soup.find('table', id='result_tab_mb')

    for id in ids:
        for col in table.findAll('td', attrs={'id': id}):
            result.append(col.text)

    return result


def check_lotto(input_data, lottery_result):
    lotto_list = [lotto[-2:] for lotto in lottery_result]

    result = []

    for number in input_data:
        if number.isdigit():
            if number[-2:] in lotto_list:
                result.append(number)

    return result


def main():
    if len(sys.argv) < 1:
        print('You did not give any number')
    else:
        input_data = sys.argv[1:]
        lottery = lottery_result()
        result = check_lotto(input_data, lottery)
        print('Các số đã chọn:', input_data)
        if result:
            print('Trúng lô:', result)
        else:
            print('Bạn đã tạch lô hôm nay')
            print(kqxs.format(*lottery))


if __name__ == '__main__':
    main()
