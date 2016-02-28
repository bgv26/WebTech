if [ ! -d "public" ]; then
    mkdir public
    mkdir public/{img,css,js}
fi
if [ ! -d "uploads" ]; then
    mkdir uploads
fi
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
