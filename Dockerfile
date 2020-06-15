FROM nginx
COPY ./*.png /usr/share/nginx/html/
COPY ./index.html /usr/share/nginx/html/

