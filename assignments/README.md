# **Web Services and Applications Assignment Repoistory**

This repository contains code and resources relate to the assignments carried out for the Web Services and Applications Assignment Repository. 

## **Table of Contents:**
- [Task Two Assignment](assignment02-carddraw.py)
- [Task Three Assignment](assignment03-cso.py)
- [Task Four Assignment](assignment04-github.py)

## **Assignments Overview:**
### **Task Two - Drawing Cards:**
File: [Drawing Cards Script File](assignment02-carddraw.py)
Interact with the [Deck of Cards API](https://deckofcardsapi.com/) to: 
- Shuffle a new deck. 
- Draw five cards. 
- Print each card's value and suit. 
- Detect poker-style patterns: pairs, triples, straight (including Ace-low), and flush. 
Dependencies: `requests` and Python's standard library. 

### **Task Three - CSO:**
File:[CSO Script File](assignment03-cso.py)
Fetch the **"Exchequer Account (Historical Series)"** dataset (Table Code: FIQ02) from the CSO PxStat API and writes in JSON‑stat format and save it to `cso.json`. 
- Uses the JSON-stat RESTful endpoint. 
- Writes raw JSON to disk without further processing. 
Dependencies: `requests`, `json`. 

### **Task Four - Github Text Replacement:** 
File: [Github Script File](assignment04-github.py)
This script: 
- Authenticates to GitHub using our tokem from `config.py`.
- Lists repository contents to confirm file path. 
- Retrieves `assignments/assignments04-andrew.txt`. 
- Replaces all instances of "Andrew! with "Bree". 
- Commits and pushes the changes back to the repository. 

#### Usage: 
1. Create `config.py` in the same folder: 
    ```python 
    config = {
        "githubkey": <YOUR_PERSON_ACCESS_TOKEN>"
    }
2. Install PyGithub.
    `pip install PyGithub`
3. Run the script.
    `python assignment04-github.py`

## **References:**
### Task Two - Drawing Cards: 
- Deck of Card API: Following API structure to shuffle deck and draw cards - https://deckofcardsapi.com/
- Collections Library (Counter): Used `Counter` to count occurrences of card values and detect pairs/triples - https://docs.python.org/3/library/collections.html#collections.Counter
- Sorting & Checking Consecutive Numbers: Used sorting to arrange card values for straight detection. Used a loop to check if values are consistent. - https://realpython.com/python-sort/
- Set in Python: Used `set(suits)` to check if all suits are the same/flush. - https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

### Task Three - CSO:
- CSO Records: Details of Records available through this search - https://data.cso.ie/?utm_
- CSO PxStat API: JSON-stat endpoint for FI02 - https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en 

### **Task Four - Github Text Replacement:** 
- PyGithub: Python client for GitHub API - https://pygithub.readthedocs.io/en/stable/introduction.html#very-short-tutorial
- GitHub RESTful API: Update file - https://docs.github.com/en/rest/repos?apiVersion=2022-11-28#update-file 