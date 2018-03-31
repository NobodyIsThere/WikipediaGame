import argparse
import random
import re
import requests

def game(url):
    text = requests.get(url).text
    match = re.search(r'<div id="mw-normal-catlinks".*?<ul>(.*?)</ul>', text)
    matches = re.findall(r'<li>(.*?)</li>', match.group(1))
    random.shuffle(matches)
    print('<html><head>')
    print('<link rel="stylesheet" type="text/css" href="style.css">')
    print('</head><body>')
    print('<div><a href="lol">Categories</a>: <ul>')
    for match in matches:
        print('<li>{}</li>'.format(match))
    print('</ul></div>')
    print('</body></html>')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str)
    
    args = parser.parse_args()
    game(args.url)