FROM ruby:3.0.2

WORKDIR /app

# Install Systen packages
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y vim
RUN apt install python3
RUN apt -y install python3-pip
# RUN apt -y install postgresql postgresql-client
RUN apt install sudo
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

COPY Gemfile Gemfile.lock requirments.txt ./

RUN bundle install
RUN pip install -r requirments.txt

COPY . .

# VOLUME /app

EXPOSE 80

# CMD ["rails", "s", "-b", "0.0.0.0"]
