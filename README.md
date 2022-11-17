# JSON Collect
This tool exports a JSON file from an API's response (`export-response`) and/or exports a CSV listing all the URLs in the returned data (`export-urls`). The latter command depends on instructions in the file `navigate_json.py`, which navigate the JSON's various keys and extract an array of the desired data, i.e. URLs.

```python
article.get("parent", {}).get("child", {}).get("url", {}) for entry in data.get("data")]
```

```json
{
    "data": [
        {
            "irrelevant stuff": {
                "data": 4
            },
            "parent": {
                "child": {
                    "url": "url_1"
                }
            },
            "more irrelevant stuff": {
                "data": "True"
            }
        },
        {
            "another bit of irrelevant stuff": {
                "data": 3
            },
            "parent": {
                "child": {
                    "url": "url_2"
                }
            },
            "and some more irrelevant stuff": {
                "data": "False"
            }
        }
    ]
}
```

The only required argument is a URL pointing to the API. I recommend storing this information in its own text file and passing it to the program via the bash command `$(cat textfile )`. By default, the command `export-urls` will remove every piece of data extracted from the source that is not a URL, according to [URAL](https://github.com/medialab/ural). However, this flag can be turned off with the option `--no-verify`, which is especially useful in case you want to modify the path in `navigate_json.py` and export a CSV of data that are not URLs.

---

## Python
version 3.10

---

## Dependencies
click, requests, ural

---
## Syntax

1. To simply get a formatted JSON file of data returned from the API, use this command. An example file `public.source.txt` is in this repository to get you started.
```bash
python main.py $(cat path/to/source.txt) export-response --outfile /path/to/outfile.json
```

2. To navigate the JSON data and export a CSV file of URLs, use this command. The flag `--verify` is activated by default and doesn't need to be specified. But if you would like to export an array of data in a CSV file that is not necessarily URLs (and would not pass URAL's verification), you can turn off that step with the flag `--no-verify`.
```bash
python main.py $(cat path/to/source.txt) export-urls --verify --outfile /path/to/outfile.csv
```

