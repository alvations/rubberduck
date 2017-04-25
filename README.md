Rubberduck
====

Yet another Python API to DuckDuckGo Instant Answer API.


Install
====

```
pip install -U rubberduck
```

Usage / Options
====

```
Usage:
    rbd.py --help
    rbd.py QUERY...
    rbd.py [--disambiguate|--related|--json] [--url|--launch] [--save <outfile>] QUERY...
    rbd.py [--url|--launch] [--save <outfile>] [--bang <bang>] QUERY...

Option:
    -h --help               Show this screen.
    -m --disambiguate       Returns the disambiguated results.
    -r --related            Returns the related results.
    -u --url                Return the result URL.
    -l --launch             Open the result URL in a new browswer tab.
    -s --save <outfile>     Saves the JSON/HTML result to file.
    -b --bang <bang>        Returns the redirected page from DuckDuckGo !bang, see https://duckduckgo.com/bang.
    -j --json               Return the JSON responses from DuckDuckGo Instant Answer API.
```


OS Specific
====

**Linux**:

```
git clone https://github.com/alvations/rubberduck.git
cd rubberduck/
python rbd.py rubberduck           # Prints: Rubberduck is a fictional character in the DC Comics universe, an anthropomorphic duck. ...
python rbd.py rubber duck          # Prints: Your query was ambiguous, try the -m option or please be more specific ...
python rbd.py -m rubber duck       # Prints: A rubber duck is a toy shaped like a stylized duck, generally yellow with a flat base. ...
python rbd.py -u rubber duck       # Prints: https://en.wikipedia.org/wiki/Rubber_duck_(disambiguation)
python rbd.py -l rubber duck       # Launch a new tab in your browser to https://en.wikipedia.org/wiki/Rubber_duck_(disambiguation)
python rbd.py -l -m rubber duck    # Launch a new tabe in your browser to https://en.wikipedia.org/wiki/Rubber_duck
python rbd.py what is the day today?            # Prints today's date.
python rbd.py what is the meaning of life?      # Prints: The meaning of life ... pertains to the significance of living or existence in general. ...
python rbd.py -u -b wtionary rubberduck  # Prints: https://en.wiktionary.org/wiki/rubber_duck
python rbd.py -l -b wtionary rubberduck  # Launch a new tabe to https://en.wiktionary.org/wiki/rubber_duck
python rbd.py -l -b google what is the answer to life the universe and everything         # Launch a new tab to https://encrypted.google.com/search?hl=en&q=what%20is%20the%20answer%20to%20life%20the%20universe%20and%20everything
```

**Mac OSX**:

```
rbd rubberduck           # Prints: Rubberduck is a fictional character in the DC Comics universe, an anthropomorphic duck. ...
rbd rubber duck          # Prints: Your query was ambiguous, try the -m option or please be more specific ...
rbd -m rubber duck       # Prints: A rubber duck is a toy shaped like a stylized duck, generally yellow with a flat base. ...
rbd -u rubber duck       # Prints: https://en.wikipedia.org/wiki/Rubber_duck_(disambiguation)
rbd -l rubber duck       # Launch a new tab in your browser to https://en.wikipedia.org/wiki/Rubber_duck_(disambiguation)
rbd -l -m rubber duck    # Launch a new tabe in your browser to https://en.wikipedia.org/wiki/Rubber_duck
rbd what is the day today?            # Prints today's date.
rbd what is the meaning of life?      # Prints: The meaning of life ... pertains to the significance of living or existence in general. ...
rbd -u -b wtionary rubberduck  # Prints: https://en.wiktionary.org/wiki/rubber_duck
rbd -l -b wtionary rubberduck  # Launch a new tabe to https://en.wiktionary.org/wiki/rubber_duck
rbd -l -b google what is the answer to life the universe and everything         # Launch a new tab to https://encrypted.google.com/search?hl=en&q=what%20is%20the%20answer%20to%20life%20the%20universe%20and%20everything
```
