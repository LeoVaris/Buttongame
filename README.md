# Buttongame
Simple online multiplayer game made using Django and Python. This project runs on a web server on Heroku. This project was made for [Vincit summer job search](https://koodarijahti.fi/)

## Features
This project fullfills all the requirements set by the challenge(excluding one problem, see below).
Additional features:
- Admin page. View and set the hidden number yourself. You can also modify your own coin count.
- Leaderboard. See the top 5 players! Also comes with a feature to prevent submitting multiple scores from one "account".

## How to use
You can try this app at: [Coming soon]
Ssh! Don't tell anyone but the admin page can be viewed at 

## Technical info
This project is made using Python and Django and is deployed using Heroku. The multiple score prevention is made by giving every player a unique uuid ```uuid.uuid()``` and when submitting a score the server removes any old submmissions with that uuid.
