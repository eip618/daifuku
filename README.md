# daifuku discord moderation bot

daifuku is a modular async discord moderation bot written with discord.py 
uses mysql for storage and cogs for extension

# warning

daifuku is a work in progress, is not feature-complete and i take no responsibility if bad things happen, though i am acting in good faith.

## features

- async discord.py and aiomysql
- basic moderation features
- modular cog system
- easy environment setup script

## setup

### 1. clone the repo

```
git clone https://github.com/eip618/daifuku.git
cd daifuku
```

### 2. install requirements

```
pip install discord.py aiomysql python-dotenv
```

currently, daifuku also expects a #mods channel, a Probation role, and a #probation channel

### 3. configure environment

run the setup script  
it will prompt for your discord bot token and mysql details

```
bash setupenv.sh
```

this creates a `.env` file  
never commit your real `.env` to github

if you want to set it up manually, copy `.env.example` to `.env` and edit

```
DAIFUKU_TOKEN=your-token
MYSQL_HOST=localhost
MYSQL_USER=daifuku
MYSQL_PASSWORD=your-password
MYSQL_DB=daifuku_db
```

### 4. run the bot

once the service unit is installed (see below),
```
systemctl restart daifuku
```

if config is correct, bot connects and announces itself in any `#mods` channel

### 5. systemd file

the setup script will generate a daifuku.service file in your project folder.
to run the bot automatically at boot and keep it running:

```
sudo mv daifuku.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable daifuku
sudo systemctl start daifuku
```
to see the bot logs in realtime:
```
sudo journalctl -u daifuku -f
```

to stop or restart the service:

```
sudo systemctl stop daifuku
sudo systemctl restart daifuku
```

## adding commands

drop new python files into the `cogs` folder  
each cog needs an async setup function

see `general.py` for an example

## troubleshooting

- check you are using python 3.8 or newer
- make sure all requirements are installed
- check mysql access and permissions
- check bot permissions for the target channel

## license

see license.txt for apache 2.0 details

## security

keep your `.env` file private  
rotate your token and password if they leak

