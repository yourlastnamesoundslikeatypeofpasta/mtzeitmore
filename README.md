# Mount Zeitmore | mtzeitmore.com

I set out to find a programmatic approach to answering the question 'What faces should there be on Mount Zeitmore?'. This repository contains a few of the many possible answers to this question.

## Process
  1. Run `00_generate.sh` to generate a list of episodes from the [TDZ Archive page](https://www.dailyzeitgeist.com/podcasts/tdz-archive.htm)
  2. Run `01_download.py` to download all linked pages and parse the results for the description data
  3. Upload the resulting `output.csv` to Google Sheets
  4. Count the number of appearances by any given host with a formula like `=COUNTIF(Sheet1!C:C, "*Billy Wayne Davis*")`
  5. Download this sheet, see `faces-mount-zeitmore.csv`

## Approach
This approach to the question looks to fill each of the four slots on Mount Rushmore. Regular hosts and super producers are not eligible to be faces on Mount Zeitmore. (They are givens and with only four slots, that would make this exercise much less fun.) The four people who appeared on The Daily Zeitgeist most frequently (whether as a guest or a guest co-host) are the faces on Mount Zeitmore. 

Currently, that list gives us these four:


  * Jamie Loftus
  * Laci Mosley
  * Billy Wayne Davis
  * Edgar Momplaisir

## Color Scheme 
The color palette extracted from the TDZ logo is:

  * dark blue: `#272C49`
  * light blue: `#51C6D8`
  * yellow: `#EDE077`

## Results
The results of this work are online at [www.mtzeitmore.com](https://www.mtzeitmore.com).

In the process of doing this work, I assembled the description for every episode and made word clouds out of the text. 

![Word Cloud](https://www.mtzeitmore.com/word-clouds/episodes/1920.jpg)

## Tools
The following tools were super helpful:
 
  * [ColourLovers.com](https://www.colourlovers.com) for generating beautiful patterns based on the color palette
  * [WordClouds.com](https://wordclouds.com) for creating beautiful word clouds

## Links
  * [/r/thedailyzeitgeist on Reddit](https://www.reddit.com/r/thedailyzeitgeist/)
  * [@dailyzeitgeist on Twitter](https://twitter.com/dailyzeitgeist)

## Songs we rode out on
Someone awesome has a [running playlist on Spotify](https://open.spotify.com/playlist/5K7ntTVOZGb92O62OfIcLg?) of songs that Miles chose to ride out on.
