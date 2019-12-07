#!/usr/bin/env python3
___doc___ = '''
Requirement: Get **N** top questions with highest vote of tag **LABEL**
on stackoverflow.com.
Print to the screen: question title, html url to the highest vote question

Link API: https://api.stackexchange.com/docs

Command: python3 stackoverflow.py N LABEL
'''


import requests
import sys


URL = 'https://api.stackexchange.com/2.2/questions'


def stackoverflow_top_question(*argv):
    result = []

    number = int(argv[0])
    tagged = argv[1]
    quota_remaining = 0

    pages = number // 100 + 1
    last_page_items = number % 100

    for page in range(1, pages + 1):
        if page < pages:
            pagesize = 100
        else:
            pagesize = last_page_items
        question_params = {"page": page,
                           "pagesize": pagesize,
                           "order": "desc",
                           "sort": "votes",
                           "tagged": tagged,
                           "site": "stackoverflow"}
        response = requests.get(URL, params=question_params)

        if response.status_code == 200:
            data = response.json()
            quota_remaining = data['quota_remaining']
            for item in data["items"]:
                title = item['title']
                question_id = item['question_id']
                votes = item['score']
                answer = best_answer(question_id)
                result.append((votes, title, answer))
        else:
            print('Status code: {}'.format(response.status_code))
            print(response.json())
            print(question_params)

        if page == pages:
            print("Quota remains: {}".format(quota_remaining))
    return result


def best_answer(question_id):
    answer_params = {"pagesize": 1,
                     "order": "desc",
                     "sort": "votes",
                     "site": "stackoverflow"}
    url = URL + '/{}/answers'.format(question_id)
    response = requests.get(url, params=answer_params).json()["items"]
    answer_id = response[0]['answer_id']
    answer = 'https://stackoverflow.com/a/{}'.format(answer_id)

    return answer


def main():
    if len(sys.argv) == 3 and sys.argv[1].isdigit():
        number = sys.argv[1]
        tagged = sys.argv[2]

        order = 1

        result = stackoverflow_top_question(*sys.argv[1:])
        print('{} top {} questions on Stackoverflow'.format(number, tagged))
        for votes, title, answer in result:
            print('{}. [{} votes] {}'.format(order, votes, title))
            print('Best answer: {}\n'.format(answer))
            order = order + 1
    else:
        print('Please give the correct command.')


if __name__ == '__main__':
    main()
