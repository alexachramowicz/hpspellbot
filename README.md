# hpspellbot
[python 3.8.5](https://www.python.org/downloads/release/python-385/)

**hpspellbot** is a Twitterbot that generate new Harry Potter spells!

It generates the spell names by randomizing latin words into singles or doubles. It generates the spell effect using [markovify](https://github.com/jsvine/markovify) to build a chain on existing Harry Potter spell effects. The resulting effects should be unique.

Uses [Tweepy](https://www.tweepy.org/) to access the Twitter API.

### Data Credit

https://www.pojo.com/harry-potter-spell-list/

https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset?select=Spells.csv

https://petscan.wmflabs.org/?language=la&project=wiktionary&categories=Lingua%20Latina&ns%5B0%5D=1&sortby=title&interface_language=en&active_tab=tab_output&&doit=
