class Api::V1::RatingsController < ApplicationController
    before_action :authenticate_request

    def index
      @ratings = current_user.ratings
      render json: @ratings
    end

    def create
        if !params[:rate]&.present?
            return json_response({ error: "Please enter a rate" })
          end
      @rating = current_user.ratings.new(rate: params[:rate])

      if @rating.save
        render json: @rating, status: :created
      else
        render json: @rating.errors, status: :unprocessable_entity
      end
    end

    private

end
