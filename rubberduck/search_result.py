# -*- coding: utf-8 -*-

from __future__ import print_function
import locale
from collections import namedtuple

try: # Try to use a faster json library.
    import ujson as json
except ImportError: # Otherwise, fall back on native json.
    import json

import requests
from six import text_type


def search(query, bang=None, **kwargs):
    params = { 'format': 'json', 'pretty': '1', 'no_html': '1',
               'no_redirect': '1', 'skip_disambig': '0'}
    bangcode = '!' + bang if bang else ''
    params.update(kwargs)
    if locale.getpreferredencoding(False).endswith('ASCII'):
        query = query.decode('utf8')
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


class DuckDuckGoJSON(object):
    def __init__(self, response):
        self.json = json.loads(response.content.decode('utf8'))
        self.pprint = json.dumps(self.json, indent=4)
        # Possible result types from DuckDuckGo API.
        self.response_types = {'A': 'article', 'D': 'disambiguation',
                               'C': 'category', 'N': 'name',
                               'E': 'exclusive', '': 'nothing'}
        # Result type.
        self.result_type = self.response_types[self.json['Type']]

        self.isambiguous = self.result_type == 'disambiguation'
        self.related_topics, self.ambiguous_topics =  parse_topics(self.json['RelatedTopics'])
        # Definitions.
        self.definition = self.json['Definition']
        self.definition_url = self.json['DefinitionURL']
        self.definition_source = self.json['DefinitionSource']
        # Abstract.
        self.abstract = self.json['AbstractText']
        self.abstract_url = self.json['AbstractURL']
        self.abstract_source = self.json['AbstractSource']
        self.abstract_heading = self.json['Heading']
        # Answer.
        self.answer = self.json['Answer']
        self.answer_type = self.json['AnswerType']
