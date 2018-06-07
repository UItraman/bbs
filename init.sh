ln -s /var/www/bbs/config/supervisor.conf /etc/supervisor/conf.d/bbs.conf

ln -s /var/www/bbs/config/nginx.conf /etc/nginx/sites-enabled/bbs

pip3 install -r requirements.txt
