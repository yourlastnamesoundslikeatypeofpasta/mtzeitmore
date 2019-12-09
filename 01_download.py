import art
import colorful
import csv
import loguru
import requests
import os


def download_episode(url, title):
    split_name = url.rsplit('/', 1)
    file_name = 'htm/' + split_name[-1]
    r = requests.get(url, allow_redirects=True)
    if not os.path.exists('htm/'):
        os.mkdir('htm/')
    open(file_name, 'wb').write(r.content)
    # description = parse_episode(file_name)
    description = parse_episode(file_name).rstrip()
    loguru.logger.debug("Title: {title}", title=title)
    loguru.logger.debug("Description: {title}", title=description)
    new_row = title + '|' + url + '|' + description + '|' + file_name + '\n'
    loguru.logger.debug(new_row)
    return new_row


def explore_episodes():
    opener_row = 'title|url|description|file_name\n'
    with open('output.csv', 'w') as f:
        f.write(opener_row)
    thefilepath = 'tdz-episodes.psv'
    csv_count = int(len(open(thefilepath).readlines()))
    episode_count = str(csv_count -1)
    print(colorful.coral(episode_count))
    input_file = csv.DictReader(open("tdz-episodes.psv"), delimiter="|")
    for row in input_file:
        title = row['Title']
        url = row['URL']
        new_row = download_episode(url, title)
        with open('output.csv', 'a+') as f:
            f.write(new_row)


def parse_episode(file_name):
    with open(file_name, 'r') as episode_file:
        data = episode_file.readlines()
        description_text = get_description(data)
    return description_text


def get_description(data):
    description_text = str()
    # GREP command for f in $(ls -1 *htm) ; do grep description $f | grep '<meta name="description" content"' ; done
    key_starter = '<meta name="description" content="'
    for line in data:
        if key_starter in line:
            split_up = line.split('"')
            description_text = split_up[3]
    return description_text


def show_art():
    mt_zeitmore = "ATOP MOUNT ZEITMORE"
    banner = "#" * 20
    print(colorful.bold_coral(mt_zeitmore))
    print(colorful.coral(banner))
    print(" " * 20)
    mt_zeit_art00=art.text2art("Atop")
    mt_zeit_art01=art.text2art("Mount")
    mt_zeit_art02=art.text2art("Zeitmore")
    print(colorful.coral(mt_zeit_art00))
    print(colorful.coral(mt_zeit_art01))
    print(colorful.coral(mt_zeit_art02)) 


def main():
    # show_art()
    explore_episodes()


if __name__ == "__main__":
    main()
