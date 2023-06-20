class Api::V1::FavoritesController < ApplicationController
     before_action :authenticate_request

    def index
      @favorites = current_user.favorites
      render json: @favorites
    end

    def create
        if !params[:product_id]&.present?
            return json_response({ error: "Please enter a product id" })
          end
      @favorite = current_user.favorites.new(product_id: params[:product_id])

      if @favorite.save
        render json: @favorite, status: :created
      else
        render json: @favorite.errors, status: :unprocessable_entity
      end
    end

    def destroy
      @favorite = current_user.favorites.find_by(product_id: params[:product_id])
      @favorite.destroy
      @favorites = current_user.favorites
      render json: @favorites
      
    end

    private

end
