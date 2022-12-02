# JSON Collect
This tool exports a JSON file from an API's response (`export-json`) and/or exports a CSV listing all the URLs in the returned data (`export-csv`). The only required argument is a URL pointing to the API.

---

## Python
version 3.10

---

## Dependencies
click, requests, ural

---
## Syntax

1. Get a formatted JSON file of data returned from the API:
```bash
python main.py $(cat path/to/source.txt) export-json --outfile path/to/outfile.json
```

2. Get a CSV file of key data returned from the API:
```bash
python main.py $(cat path/to/source.txt) export-csv --outfile path/to/outfile.csv
```

