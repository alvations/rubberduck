# -*- coding: utf-8 -*-

"""
Usage:
    rubberduck.py --help
    rubberduck.py [--define|--answer|--json] [--ambiguous] [--url|--launch] [--save <outfile>] [--bang <bang>] QUERY...

Option:
    -h --help               Show this screen.
    -b --bang <bang>        Use DuckDuckGo !bang, see https://duckduckgo.com/bang.
    -d --define             Return the definition from API response.
    -a --answer             Return the answer from API response.
    -j --json               Return the JSON responses from DuckDuckGo Instant Answer API.
    -m --ambiguous          Returns ambiguous results from from API response.
    -u --url                Return the result URL.
    -l --launch             Open the result URL in a new browswer tab.
    -s --save <outfile>     Saves the result in an output file.

Try:

"""

from __future__ import print_function

import io
import json

from six import text_type
from docopt import docopt

import rubberduck

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Rubberduck (rbd.py) version 0.0.1')
    query = ' '.join(arguments['QUERY'])
    # By default, return the disambiguated result based on DuckDuckGo Instant API.
    skip_disambig = 0 if arguments['--ambiguous'] else 1
    # Redirect search result when !bang is used, unless we need to return --json
    bang = arguments['--bang']
    return_json = arguments['--json']
    no_redirect = 0 if bang and not return_json else 1  # Always redirect when DuckDuckGo bang is used.
    response = rubberduck.search(query, bang=bang, no_redirect=no_redirect,
                                 skip_disambig=skip_disambig)

    if bang:  # Note: that response is redirected when DuckDuckGo bang is used.
        if arguments['--url']:  # Prints the URL of the redirected page.
            print(response.url)
        elif arguments['--launch']:  # Launch the redirected page.
            webbrowser.open_new_tab(response.url)
        else:  # Prints the redirected HTML.
            result = response.content.decode('utf8')
            print (result)
    else:
        result = rubberduck.DuckDuckGoResult(response)
        if return_json:
            print (json.dump(result.json, indent=4, separators=(',', ': ')))


    if arguments['--save']:
        with io.open(arguments['--save'], 'w', encoding='utf8') as fout:
            print(result, file=fout)
