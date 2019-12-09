#!/bin/bash

wget -O tdz-archive.htm https://www.dailyzeitgeist.com/podcasts/tdz-archive.htm
grep '<a href="https://www.dailyzeitgeist.com/podcasts/' tdz-archive.htm | wc -l
grep   '<a href="https://www.dailyzeitgeist.com/podcasts/' tdz-archive.htm  | cut -d'"' -f2 > episode-links.txt         # Links
grep  -A1  '<a href="https://www.dailyzeitgeist.com/podcasts/' tdz-archive.htm | grep "<p>" | sed 's/<[^>]*>/\n/g' | sed '/^[[:space:]]*$/d' > episode-titles.txt # Titles
wc -l episode-links.txt
wc -l episode-titles.txt 
paste -d '|' episode-titles.txt episode-links.txt >> tdz-episodes.psv
sed  -i '1 i\"Title"|"URL"' tdz-episodes.psv         
head -n4 tdz-episodes.psv
