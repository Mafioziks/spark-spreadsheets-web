# --------------------------------- Apache Spark Setup ----------------------------------------

# TODO: check out this image and base on it clean apache spark setup
ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Toms Teteris <toms.teteris@inbox.eu>"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Spark dependencies
# Default values can be overridden at build time
# (ARGS are in lower case to distinguish them from ENV)
ARG spark_version="3.0.1"
ARG hadoop_version="2.7"
ARG openjdk_version="8"

ENV APACHE_SPARK_VERSION="${spark_version}" \
    HADOOP_VERSION="${hadoop_version}"

WORKDIR /tmp

# download and clean up spark checksum
RUN wget -q "https://downloads.apache.org/spark/spark-${spark_version}/spark-${spark_version}-bin-hadoop${hadoop_version}.tgz.sha512" \
    && cat "spark-${spark_version}-bin-hadoop${hadoop_version}.tgz.sha512" | tr -d '[:space:]' > spaceless_hash \
    && awk "{gsub(\"spark-${spark_version}-bin-hadoop${hadoop_version}.tgz:\", \"\");print}" spaceless_hash > spark_checksum \
    && rm spaceless_hash

RUN apt-get -y update && \
    apt-get install --no-install-recommends -y \
    "openjdk-${openjdk_version}-jre-headless" \
    ca-certificates-java && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# scala instalation

ARG scala_version=2.11.12
ENV SCALA_VERSION="${scala_version}"
RUN wget -q "https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" \
    && tar xzf "scala-${SCALA_VERSION}.tgz" -C /usr/local --owner root --group root --no-same-owner \
    && rm "scala-${SCALA_VERSION}.tgz" \
    && ln -s "/usr/local/scala-${SCALA_VERSION}" /usr/local/scala

ENV SCALA_HOME="/usr/local/scala"
ENV PATH=$PATH:$SCALA_HOME/bin

# Spark installation

# Using the preferred mirror to download Spark
# hadolint ignore=SC2046
RUN wget -q $(wget -qO- https://www.apache.org/dyn/closer.lua/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz\?as_json | \
    python -c "import sys, json; content=json.load(sys.stdin); print(content['preferred']+content['path_info'])") && \
    echo $(cat ./spark_checksum)" *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
    tar xzf "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -C /usr/local --owner root --group root --no-same-owner && \
    rm "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

RUN rm spark_checksum

WORKDIR /usr/local

# Configure Spark
ENV SPARK_HOME=/usr/local/spark
ENV SPARK_OPTS="--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info" \
    PATH=$PATH:$SPARK_HOME/bin

RUN ln -s "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" spark && \
    # Add a link in the before_notebook hook in order to source automatically PYTHONPATH
    mkdir -p /usr/local/bin/before-notebook.d && \
    ln -s "${SPARK_HOME}/sbin/spark-config.sh" /usr/local/bin/before-notebook.d/spark-config.sh

# Fix Spark installation for Java 11 and Apache Arrow library
# see: https://github.com/apache/spark/pull/27356, https://spark.apache.org/docs/latest/#downloading
RUN cp -p "$SPARK_HOME/conf/spark-defaults.conf.template" "$SPARK_HOME/conf/spark-defaults.conf" && \
    echo 'spark.driver.extraJavaOptions="-Dio.netty.tryReflectionSetAccessible=true"' >> $SPARK_HOME/conf/spark-defaults.conf && \
    echo 'spark.executor.extraJavaOptions="-Dio.netty.tryReflectionSetAccessible=true"' >> $SPARK_HOME/conf/spark-defaults.conf

USER $NB_UID

# Install pyarrow
RUN conda install --quiet --yes --satisfied-skip-solve \
    'pyarrow=2.0.*' && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

WORKDIR $HOME

# ------------------------------------- Livy Setup --------------------------------------------
ARG livy_version=0.7.0

# setting environment variables for Livy
ENV HADOOP_CONF_DIR=/etc/hadoop/conf
ENV LIVY_VERSION="${livy_version}"

# downloading livy
# TODO: Move installation to /usr/local dir as is for other items
RUN wget -q "https://ftp.heanet.ie/mirrors/www.apache.org/dist/incubator/livy/$LIVY_VERSION-incubating/apache-livy-$LIVY_VERSION-incubating-bin.zip" \
    && unzip "apache-livy-$LIVY_VERSION-incubating-bin.zip"

# Set Livy conf dirrectory
ENV LIVY_CONF_DIR="/home/jovyan/apache-livy-$LIVY_VERSION-incubating-bin/conf"

RUN mkdir -m 777 -p "$LIVY_CONF_DIR"

# make configuration changes for livy
RUN echo "livy.server.port = 8998" >> "$LIVY_CONF_DIR/livy.conf" \
    && echo "livy.spark.version = ${APACHE_SPARK_VERSION}" >> "$LIVY_CONF_DIR/livy.conf" \
    && echo "livy.spark.scala-version = ${SCALA_VERSION}" >> "$LIVY_CONF_DIR/livy.conf"

# make configuration changes for log4j
RUN echo "log4j.rootCategory=INFO, console" >> "$LIVY_CONF_DIR/log4j.properties" \
    && echo "log4j.appender.console=org.apache.log4j.ConsoleAppender" >> "$LIVY_CONF_DIR/log4j.properties" \
    && echo "log4j.appender.console.target=System.err" >> "$LIVY_CONF_DIR/log4j.properties" \
    && echo "log4j.appender.console.layout=org.apache.log4j.PatternLayout" >> "$LIVY_CONF_DIR/log4j.properties" \
    && echo "log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n" >> "$LIVY_CONF_DIR/log4j.properties" \
    && echo "log4j.logger.org.eclipse.jetty=WARN" >> "$LIVY_CONF_DIR/log4j.properties"


# run livy
# TODO: in CMD or in runner bash script add this as one of commands to run else this will not start
RUN "./apache-livy-$LIVY_VERSION-incubating-bin/bin/livy-server" start

# expose livy port
EXPOSE 8998/tcp
