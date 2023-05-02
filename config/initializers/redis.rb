# frozen_string_literal: true

REDIS_CACHE = Redis.new(url: ENV['DEVELOPMENT_REDIS_URL'])
