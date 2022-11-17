import csv
import json
import time

import click
import requests
import ural

from navigate_json import json_path

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
def export_response(source, outfile):
    data = source.load_data()
    with open(outfile, "w") as f:
        json.dump(data, f, indent=4)


@cli.command()
@click.option("--outfile", default="urls.csv")
@click.option("--verify/--no-verify", is_flag=True, default=True)
@click.pass_obj
def export_urls(source, outfile, verify):
    data = source.load_data()

    # Modify the array created with json_path() as the JSON data structure changes.
    urls = [url.replace(" ","") for url in json_path(data) if url]

    if verify:
        urls = [url for url in urls if ural.is_url(url)]

    with open(outfile, "w") as f:
        writer = csv.writer(f)
        for url in urls:
            writer.writerow([url])


if __name__ == "__main__":
    cli()
