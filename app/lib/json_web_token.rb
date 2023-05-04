class JsonWebToken
  class << self
    def encode(payload)
      JWT.encode(payload, "Rails.application.credentials.secret_key_base")
    end

    def decode(token)
      return unless token
      body = JWT.decode(token, "Rails.application.credentials.secret_key_base")&.first
      HashWithIndifferentAccess.new body
    rescue JWT::DecodeError
      nil
    end
  end
end
