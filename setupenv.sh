#!/bin/bash

echo "---- Daifuku .env Setup ----"

read -p "Your Discord bot token: " TOKEN
read -p "Your mysql host (defaults to localhost): " MYSQL_HOST
MYSQL_HOST=${MYSQL_HOST:-localhost}

read -p "Your mysql user (defaults to daifuku): " MYSQL_USER
MYSQL_USER=${MYSQL_USER:-daifuku}

read -s -p "Mysql user password: " MYSQL_PASSWORD
echo
read -p "Mysql db name (defaults to daifuku_db: " MYSQL_DB
MYSQL_DB=${MYSQL_DB:-daifuku_db}

# write to the .env
cat > .env <<EOF
DAIFUKU_TOKEN=$TOKEN
MYSQL_HOST=$MYSQL_HOST
MYSQL_USER=$MYSQL_USER
MYSQL_PASSWORD=$MYSQL_PASSWORD
MYSQL_DB=$MYSQL_DB
EOF

# Prepare the SQL
SQL="
CREATE DATABASE IF NOT EXISTS \`$MYSQL_DB\`;
CREATE USER IF NOT EXISTS '$MYSQL_USER'@'$MYSQL_HOST' IDENTIFIED BY '$MYSQL_PASSWORD';
GRANT ALL ON \`$MYSQL_DB\`.* TO '$MYSQL_USER'@'$MYSQL_HOST';
FLUSH PRIVILEGES;
"

echo "Setting up MySQL user and database..."
# execute with mysql cli
mysql -u root -p"$MYSQL_ROOTPW" -e "$SQL"

if [ $? -eq 0 ]; then
    echo "MySQL user/database setup successful!"
else
    echo "Error setting up MySQL user/database. Check your root password and MySQL installation."
fi

echo
echo ".env file created! Contents:"
echo "DAIFUKU_TOKEN=[hidden]"
echo "MYSQL_HOST=$MYSQL_HOST"
echo "MYSQL_USER=$MYSQL_USER"
echo "MYSQL_PASSWORD=[hidden]"
echo "MYSQL_DB=$MYSQL_DB"

# create systemd unit file
cat > daifuku.service <<EOF
[Unit]
Description=daifuku discord moderation bot
After=network.target mysql.service

[Service]
Type=simple
WorkingDirectory=$(pwd)
ExecStart=$(which python3) $(pwd)/bot.py
Restart=on-failure
Environment=\"DAIFUKU_TOKEN=\${DAIFUKU_TOKEN}\"
EnvironmentFile=$(pwd)/.env

[Install]
WantedBy=multi-user.target
EOF

echo
echo "systemd unit file 'daifuku.service' created in this directory."
echo "to enable it:"
echo "  sudo mv daifuku.service /etc/systemd/system/"
echo "  sudo systemctl daemon-reload"
echo "  sudo systemctl enable daifuku"
echo "  sudo systemctl start daifuku"
echo
echo "to view logs: sudo journalctl -u daifuku -f"