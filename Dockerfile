# --------------------------------- Apache Spark Setup ----------------------------------------

# TODO: check out this image and base on it clean apache spark setup
FROM jupyter/pyspark-notebook:latest

# ------------------------------------- Livy Setup --------------------------------------------

# setting environment variables for Livy
ENV HADOOP_CONF_DIR=/etc/hadoop/conf

# downloading livy
RUN wget https://ftp.heanet.ie/mirrors/www.apache.org/dist/incubator/livy/0.7.0-incubating/apache-livy-0.7.0-incubating-bin.zip
RUN unzip apache-livy-0.7.0-incubating-bin.zip -d livy0.7.0

# make configuration changes for livy
RUN echo "livy.server.port = 8998" >> ./livy0.7.0/apache-livy-0.7.0-incubating-bin/conf/livy.conf


# run livy
# TODO: in CMD or in runner bash script add this as one of commands to run else this will not start
RUN ./livy0.7.0/apache-livy-0.7.0-incubating-bin/bin/livy-server start

# expose livy port
EXPOSE 8998/tcp



