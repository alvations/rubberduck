# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import namedtuple

try: # Try to use a faster json library.
    import ujson as json
except ImportError: # Otherwise, fall back on native json.
    import json

import json as jason

import requests
from six import text_type




def search(query, bang=None, **kwargs):
    params = { 'format': 'json', 'pretty': '1', 'no_html': '1',
               'no_redirect': '1', 'skip_disambig': '0'}
    bangcode = '!' + bang if bang else ''
    params.update(kwargs)
    query = requests.utils.quote(text_type(query).encode('utf8'))
    url = 'http://api.duckduckgo.com/?q=' + '+'.join([bangcode, query])
    response = requests.get(url, params=params)
    return response


DuckduckgoResult = namedtuple('DuckduckgoResult', 'url, text')

def parse_results(results_json):
    for result in results_json:
        yield DuckduckgoResult(url=result['FirstURL'], text=result['Text'])

def parse_topics(topics_json):
    ambiguous_topics = {}
    related_topics = []
    for topic in topics_json:
        topic_name = topic.get('Name')
        if topic_name:
            ambiguous_topics[topic_name] = list(parse_results(topic['Topics']))
        else:
            related_topics.append(DuckduckgoResult(topic['FirstURL'], topic['Text']))
    return related_topics, ambiguous_topics


class Result(object):
    def __init__(self, response):
        self.json = json.loads(response.content.decode('utf8'))
        self.pprint = json.dumps(self.json, indent=4)
        # Definitions.

        # Abstract.

        # Possible result types from DuckDuckGo API.
        self.response_types = {'A': 'article', 'D': 'disambiguation',
                               'C': 'category', 'N': 'name',
                               'E': 'exclusive', '': 'nothing'}
        # Result type.
        self.result_type = self.response_types[self.json['Type']]

        self.isambiguous = self.result_type == 'disambugation'
        self.related_topics, self.ambiguous_topics =  parse_topics(self.json['RelatedTopics'])





r = search(u'카페', bang='!endic', no_redirect=0)
r = search('apple')
rr = Result(r)
print (rr.pprint)
print (rr.related_topics)
#print (r.content.decode('utf8'))

class Results2(object):
    def __init__(self, json):
        self.json = jsonlib.dumps(json, indent=2)
        self.type = {'A': 'article', 'D': 'disambiguation',
                     'C': 'category', 'N': 'name',
                     'E': 'exclusive', '': 'nothing'}[json['Type']]
        self.answer = Answer(json)
        self.result = Result(json.get('Results', None))
        self.abstract = Abstract(json)
        self.definition = Definition(json)
        self.redirect = Redirect(json)


class Result(object):
    def __init__(self, json):
        self.html = json[0].get('Result', '') if json else ''
        self.text = json[0].get('Text', '') if json else ''
        self.url = json[0].get('FirstURL', '') if json else ''


class Abstract(object):
    def __init__(self, json):
        self.html = json['Abstract']
        self.text = json['AbstractText']
        self.url = json['AbstractURL']
        self.source = json['AbstractSource']
        self.heading = json['Heading']


class Answer(object):
    def __init__(self, json):
        self.text = json['Answer']
        self.type = json['AnswerType']
        self.url = None


class Definition(object):
    def __init__(self, json):
        self.text = json['Definition']
        self.url = json['DefinitionURL']
        self.source = json['DefinitionSource']
