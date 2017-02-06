Rubberduck
====

Yet another Python API to DuckDuckGo Instant Answer API.


Install
====

```
pip install -U rubberduck
```

Usage
====

```
rbd.py rubberduck           # Prints: Rubberduck is a fictional character in the DC Comics universe, an anthropomorphic duck. ...
rbd.py rubber duck          # Prints: Your query was ambiguous, try the -m option or please be more specific ...
rbd.py -m rubber duck       # Prints: A rubber duck is a toy shaped like a stylized duck, generally yellow with a flat base. ...
rbd.py -u rubber duck       # Prints: https://en.wikipedia.org/wiki/Rubber_duck_(disambiguation)
rbd.py -l rubber duck       # Launch a new tab in your browser to https://en.wikipedia.org/wiki/Rubber_duck_(disambiguation)
rbd.py -l -m rubber duck    # Launch a new tabe in your browser to https://en.wikipedia.org/wiki/Rubber_duck
rbd.py what is the day today?            # Prints today's date.
rbd.py what is the meaning of life?      # Prints: The meaning of life ... pertains to the significance of living or existence in general. ...
python rbd.py -u -b wtionary rubberduck  # Prints: https://en.wiktionary.org/wiki/rubber_duck
python rbd.py -l -b wtionary rubberduck  # Launch a new tabe to https://en.wiktionary.org/wiki/rubber_duck
rbd.py -l -b google what is the answer to life the universe and everything         # Launch a new tab to https://encrypted.google.com/search?hl=en&q=what%20is%20the%20answer%20to%20life%20the%20universe%20and%20everything

```
