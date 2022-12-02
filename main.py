import csv
import json
import time

import click
import requests

from navigate_json import navigate_json

yellow = "\033[1;33m"
green = "\033[0;32m"
reset = "\033[0m"


class Source(object):
    def __init__(self, url):
        self.url = url
    
    def load_data(self):
        attempts = 0
        response = requests.models.Response()
        response.status_code = 400
        while response.status_code != 200 and attempts < 10 :
            print("Attempt {} to request data from {}.".format(attempts+1, self.url))
            response = requests.get(self.url)
            attempts += 1
            time.sleep(1)
        if response.status_code != 200:
            print("The request to the API was not successful. Try again later.")
        else:
            print(f"{green}Received good response from data source.{reset}")
            return json.loads(response.text)


@click.group()
@click.argument("data-source", type=str, required=True)
@click.pass_context
def cli(ctx, data_source):
    ctx.obj = Source(data_source)


@cli.command()
@click.option("--outfile", default="export.json")
@click.pass_obj
def export_json(source, outfile):
    data = source.load_data()
    with open(outfile, "w") as f:
        json.dump(data, f, indent=4)


@cli.command()
@click.option("--outfile", default="export.csv")
@click.pass_obj
def export_csv(source, outfile):
    data = source.load_data()

    # Modify the array created with json_path() as the JSON data structure changes.
    rows = navigate_json(data)

    with open(outfile, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "themes", "tags", "datePublished", "url", "ratingValue", "rating_alternateName"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    cli()
