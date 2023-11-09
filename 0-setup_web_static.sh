#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static

# If not already installed, install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create relevant files and directories
sudo mkdir -p /data/web_static/shared/	
sudo mkdir -p /data/web_static/releases/test/
sudo echo "This is a fake HTML file, to test my Nginx configuration" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and update ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_text="server {
	listen 80;
	server_name _;
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}"

sudo echo "$config_text" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo service nginx restart

exit 0
