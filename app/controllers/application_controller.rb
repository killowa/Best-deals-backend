class ApplicationController < ActionController::API
  include Response
  before_action :validate_request, :authenticate_request, except: [:login]

  def current_user
    @current_user ||= authenticated_current
  end

  private

  def authenticate_request
    @current_user = authenticated_current
    render json: { error: I18n.t('errors.authorization') }, status: :unauthorized unless @current_user
    @current_user
  end

  def authenticated_current
    decoded_token = JsonWebToken.decode(http_auth_header)
    User.find(decoded_token[:user_id])
  end

  def validate_request
    render json: { error: I18n.t('errors.bad_request') }, status: :bad_request unless http_auth_header
  end

  def http_auth_header
    request.headers['Authorization']&.split(' ')&.last
  end

  def unauthorized
    render json: { error: I18n.t('errors.authorization') }, status: :unauthorized
  end


  def index
    # This method will be called before any other actions in the controller

    # Create entries for every website in the database
    # This is so that we can easily add more websites to scrape from
    # in the future
    @websites = Website.all
    json_response(@websites)
  end

  rescue_from ActiveRecord::RecordNotFound do |exception|
    json_response({ message: exception.message }, :not_found)
  end

end
