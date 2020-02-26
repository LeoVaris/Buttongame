# Buttongame
Simple online multiplayer game made using Django and Python. This project runs on a web server on Heroku. This project was made for [Vincit summer job search](https://koodarijahti.fi/)

## Features
This project fullfills all the requirements set by the challenge(excluding one problem, see below).
Additional features:
- Admin page. View and set the hidden number yourself. You can also modify your own coin count.
- Leaderboard. See the top 5 players! Also comes with a feature to prevent submitting multiple scores from one "account".

## Known problems
When developing this app, all testing was done using localhost. After deploying to Heroku I found out that the leaderboards are quite buggy(even after changing the region to EU) and change from browser load to another. All actions should be done slowly to avoid any further issues. Also the global counter for every player isn't 100% synced all the time. For better testing use localhost. With localhost I found that the cookies are deleted when close the browser(not a tab). So they are saved only when the same window is open.

## How to use
You can try this app at: https://buttongame-varis-eu.herokuapp.com/<br/>
Don't tell anyone but the admin page can be viewed at /superadmin

## Run locally
### Clone
You can clone this project using ```https://github.com/LeoVaris/Buttongame.git```
### Install Django
```pip install Django```
### Run app
Navigate to the folder and run:
```python manage.py runserver```<br/>
And then go to your browser and use address 
```localhost:8000```

## Technical info
- This project is made using Python and Django and is deployed using Heroku. 
- Game state is saved using browser cookies. 
- The multiple score prevention is made by giving every player a unique uuid ```uuid.uuid()``` and when submitting a score the server removes any old submmissions with that uuid.
