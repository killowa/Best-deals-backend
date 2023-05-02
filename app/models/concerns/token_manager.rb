module TokenManager
  extend ActiveSupport::Concern
  included do
    def auth_token(ttl_in_days = 14)
      token = JsonWebToken.encode({ user_id: id })
      return token if REDIS_CACHE.get(token)

      REDIS_CACHE.set(token, token, ex: days_to_seconds(ttl_in_days))
      token
    end
  end

  def days_to_seconds(days)
    days * 60 * 60 * 24
  end
end
