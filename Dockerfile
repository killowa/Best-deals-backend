FROM ruby:3.0.2

WORKDIR /app

# Install Systen packages
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y vim
RUN apt install python3
RUN apt install python3-pip

COPY Gemfile Gemfile.lock ./

COPY . .

EXPOSE 3000
