# frozen_string_literal: true

module Api
  module V1
    class UsersController < ApplicationController
      skip_before_action :validate_request, :authenticate_request, :only => [:create]

      def login
        user = User.find_by(email: params[:email].downcase)
        if user&.authenticate(params[:password])
          render json: { user: user, token: user.auth_token }, status: :ok
        else
          render json: { error: I18n.t('messages.authentication') }, status: :unprocessable_entity
        end
      end

      def logout
        if valid_token?
          render json: { message: I18n.t('messages.success', operation: 'Logged out') }, status: :ok
        else
          render json: { error: I18n.t('errors.authorization') }, status: :unprocessable_entity
        end
      end

      def valid_token?
        REDIS_CACHE.del(http_auth_header) == 1
      end

      def create
        user = User.new(user_params)
        user.password = params[:user][:password]
        if user.save
          render json: { message: I18n.t('messages.success') }, status: :created
        else
          render json: { error: user.errors.full_messages }, status: :unprocessable_entity
        end
      end

      private

      def user_params
        params.require(:user).permit(:email, :username)
      end
    end
  end
end
