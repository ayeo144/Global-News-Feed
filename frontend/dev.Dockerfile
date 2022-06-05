FROM nginx:stable-alpine

RUN apk add --update nodejs npm

COPY . /usr/share/nginx/html
COPY /configs/nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]