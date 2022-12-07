FROM tomcat:9.0

WORKDIR /usr/local/tomcat
USER root

COPY ./TVBox  /usr/local/tomcat/webapps/TVBox

EXPOSE 8080

CMD ["catalina.sh", "run"]