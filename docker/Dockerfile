FROM ubuntu:16.04
LABEL MAINTAINER "Toms Teteris <toms.teteris@inbox.eu>"

# RUN apt-get update && apt-get install -y gnupg gnupg2 gnupg1
# RUN apt-get install --no-install-recommends -y software-properties-common dirmngr
# RUN apt-get install sudo
# Add R list
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
#     && add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/" \
#     && add-apt-repository ppa:xapienz/curl34 \
#     && apt policy curl
    
# TODO: Resolve libcurl3 requirement
# # packages
# RUN apt-get install software-properties-common -y
# RUN apt-add-repository ppa:webupd8team/java \
#     && apt-get update \
#     && apt-get install oracle-java8-installer -y

# RUN java -v
# RUN export JAVA_HOME=/usr/lib/jvm/java-8-oracle

RUN apt-get update && apt-get install -yq --no-install-recommends \
    wget \
    git \
    openjdk-8-jdk \
    maven \
    libjansi-java \
    libsvn1 \
    libcurl3 \
    libsasl2-modules \
    unzip

RUN apt-get --fix-broken install

# Overall ENV vars
ENV SPARK_VERSION="2.4.7" \
    MESOS_BUILD_VERSION="0.28.0-2.0.16" \
    # MESOS_BUILD_VERSION="1.9.0-2.0.1" \
    LIVY_BUILD_VERSION="livy-server-0.3.0-SNAPSHOT"

# Set install path for Livy
ENV LIVY_APP_PATH="/apps/livy" \
    LIVY_BUILD_PATH="/apps/build/livy" \
    HADOOP_CONF_DIR="/etc/hadoop/conf" \
    SPARK_HOME="/usr/local/spark"

# http://repos.mesosphere.com/ubuntu/pool/main/m/mesos/mesos_1.9.0-2.0.1.ubuntu1604_amd64.deb
# Set native Mesos library path
ENV MESOS_NATIVE_JAVA_LIBRARY /usr/local/lib/libmesos.so

# Mesos install
# RUN wget http://repos.mesosphere.com/ubuntu/pool/main/m/mesos/mesos_$MESOS_BUILD_VERSION.ubuntu1404_amd64.deb && \
#     dpkg -i mesos_$MESOS_BUILD_VERSION.ubuntu1404_amd64.deb && \
#     rm mesos_$MESOS_BUILD_VERSION.ubuntu1404_amd64.deb

# Spark ENV vars
ENV SPARK_VERSION_STRING spark-$SPARK_VERSION-bin-hadoop2.6
# https://ftp.heanet.ie/mirrors/www.apache.org/dist/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
ENV SPARK_DOWNLOAD_URL https://ftp.heanet.ie/mirrors/www.apache.org/dist/spark/spark-${SPARK_VERSION}/${SPARK_VERSION_STRING}.tgz
# ENV SPARK_DOWNLOAD_URL http://d3kbcqa49mib13.cloudfront.net/$SPARK_VERSION_STRING.tgz

# Download and unzip Spark
RUN wget $SPARK_DOWNLOAD_URL && \
    mkdir -p $SPARK_HOME && \
    tar xvf $SPARK_VERSION_STRING.tgz -C /tmp && \
    cp -rf /tmp/$SPARK_VERSION_STRING/* $SPARK_HOME && \
    rm -rf -- /tmp/$SPARK_VERSION_STRING && \
    rm ${SPARK_VERSION_STRING}.tgz

# Clone Livy repository
# RUN mkdir -p /apps/build && \
#     cd /apps/build && \
# 	git clone https://github.com/cloudera/livy.git && \
# 	cd $LIVY_BUILD_PATH && \
#     mvn -DskipTests -Dspark.version=$SPARK_VERSION clean package && \
#     unzip $LIVY_BUILD_PATH/assembly/target/$LIVY_BUILD_VERSION.zip -d /apps && \
#     rm -rf $LIVY_BUILD_PATH && \
# 	mkdir -p $LIVY_APP_PATH/upload
ARG livy_version=0.7.0
ENV LIVY_VERSION="${livy_version}"

# downloading livy
# TODO: Move installation to /usr/local dir as is for other items
RUN wget -q "https://ftp.heanet.ie/mirrors/www.apache.org/dist/incubator/livy/$LIVY_VERSION-incubating/apache-livy-$LIVY_VERSION-incubating-bin.zip" \
    && unzip "apache-livy-$LIVY_VERSION-incubating-bin.zip" \
    && mkdir -p /apps \
    # && ls -alt ./ \
    # && ls -alt /apps \
    && mv "./apache-livy-$LIVY_VERSION-incubating-bin" /apps/livy \
    && mkdir -p $LIVY_APP_PATH/upload \
    && mkdir -p ${LIVY_APP_PATH}/logs \
    && chmod 777 ${LIVY_APP_PATH}/logs
	
# Add custom files, set permissions
ADD entrypoint.sh .

RUN chmod +x entrypoint.sh

# Expose port
EXPOSE 8998

ENTRYPOINT ["/entrypoint.sh"]
