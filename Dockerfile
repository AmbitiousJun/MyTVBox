FROM nginx:1.21-alpine

WORKDIR /usr/share/nginx/html
USER root

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./ssl /etc/nginx/conf.d/ssl

COPY ./TVBox  /usr/share/nginx/html/TVBox

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]