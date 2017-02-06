# -*- coding: utf-8 -*-

"""
Usage:
    rubberduck.py --help
    rubberduck.py QUERY...
    rubberduck.py [--disambiguate|--related|--answer|--define|--json] [--url|--launch] [--save <outfile>] QUERY...
    rubberduck.py [--url|--launch] [--save <outfile>] [--bang <bang>] QUERY...

Option:
    -h --help               Show this screen.
    -m --disambiguate       Returns the disambiguated results.
    -r --related            Returns the related results.
    -a --answer             Return the answer.
    -d --define             Return the definition.
    -u --url                Return the result URL.
    -l --launch             Open the result URL in a new browswer tab.
    -s --save <outfile>     Saves the JSON/HTML result to file.
    -b --bang <bang>        Returns the redirected page from DuckDuckGo !bang, see https://duckduckgo.com/bang.
    -j --json               Return the JSON responses from DuckDuckGo Instant Answer API.

Try:

"""

from __future__ import print_function

import io
import json
import sys
import webbrowser

from six import text_type
from docopt import docopt

import rubberduck

def print_ddg_results(ddg_results, topic_name=None):
    topic_name = topic_name if topic_name else ''
    print(topic_name, end='\n')
    for ddg_result in ddg_results:
        print ('\t'.join(['', ddg_result.url, ddg_result.text]), end='\n')
        yield '\t'.join([topic_name, ddg_result.url, ddg_result.text])


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Rubberduck (rbd.py) version 0.0.1')
    query = ' '.join(arguments['QUERY'])
    # By default, return the disambiguated result based on DuckDuckGo Instant API.
    skip_disambig = 1 if arguments['--disambiguate'] else 0
    # Redirect search result when !bang is used.
    bang = arguments['--bang']
    no_redirect = 0 if bang else 1  # Always redirect when DuckDuckGo bang is used.
    response = rubberduck.search(query, bang=bang, no_redirect=no_redirect,
                                 skip_disambig=skip_disambig)
    result = response_url = response.url

    # Handles !bang requests.
    if arguments['--bang']:
        if arguments['--url']:   # Prints the redirected page.
            print(response_url)
        elif arguments['--launch']:  # Launch the redirected page.
            webbrowser.open_new_tab(response_url)
            print (response_url)
        else:  # Prints the redirected page HTML.
            result = response.content.decode('utf8')
            print (result)
            print (response.url)

    # Handles define/answer/ambiguous requests.
    else:
        ddg_json = rubberduck.DuckDuckGoJSON(response)
        if arguments['--url']:   # Prints the redirected page.
            result = ddg_json.abstract_url if ddg_json.abstract_url else response_url
            print (result)
        # Returns the JSON from the API response.
        elif arguments['--json']:
            result = ddg_json.pprint
            print (result)
            print (ddg_json.isambiguous, ddg_json.result_type)
        # Returns related results.
        elif ddg_json.isambiguous:
            print ("Your query was ambiguous, try the -m option or please be more specific\n")
            topics = ddg_json.ambiguous_topics
            see_also = topics.pop('See also')
            result = []
            # Prints the ambiguous topics.
            for topic_name, ddg_results in sorted(topics.items()):
                result+=list(print_ddg_results(ddg_results, topic_name))
            # Prints the related topics.
            result+=list(print_ddg_results(ddg_json.related_topics, 'Related'))
            # Prints the "See also" topics.
            result+=list(print_ddg_results(see_also, 'See also'))
            # Cobine the results.
            result = '\n'.join(result)
        # Returns related results.
        elif arguments['--related']:
            topics = ddg_json.related_topics
            result = []
            for ddg_result in topics:
                print ('\t'.join([ddg_result.url, ddg_result.text]), end='\n')
                result.append('\t'.join([ddg_result.url, ddg_result.text]))
            result = '\n'.join(result)
        # Returns an answer, defintiion/abstract, or "no result found".
        else:
            results_priority = [ddg_json.answer, ddg_json.abstract, u'No result found']
            for result in results_priority:
                if result:
                    break
            print(result)

    if arguments['--save']:
        with io.open(arguments['--save'], 'w', encoding='utf8') as fout:
            fout.write(result)
