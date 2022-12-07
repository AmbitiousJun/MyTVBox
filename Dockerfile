FROM nginx:1.21-alpine

WORKDIR /usr/share/nginx/html
USER root

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./TVBox  /usr/share/nginx/html/TVBox

EXPOSE 9000

CMD ["nginx", "-g", "daemon off;"]