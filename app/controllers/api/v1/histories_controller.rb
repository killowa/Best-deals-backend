
module Api
    module V1
        class Api::V1::HistoriesController < ApplicationController
            before_action :authenticate_request
            after_action :limit_histories
            MAX_HISTORIES = 100
            
            def index
                # show the history database table entries in descending order
                @histories = current_user.histories.order(created_at: :desc)
                render json: @histories
            end
            
            
            def create
                if !params[:product_id]&.present?
                    return json_response({ error: "Please enter product id" })
                end
                # find the product with the given ID, and deletes the user's previous record of that product if it exists.
                @product = Product.find(params[:product_id])
                old_record = current_user.histories.where(product_id: @product.id).last
                old_record.destroy if old_record.present?
                
                # create a new history record for the user with the current product ID
                @history = current_user.histories.new(
                    product_id: params[:product_id]
                )
                if @history.save
                    render json: @history, status: :created
                else
                    render json: @history.errors, status: :unprocessable_entity
                end
            end
            

            private
            

            def limit_histories
                count = current_user.histories.count
                if count > MAX_HISTORIES
                    oldest_history = current_user.histories.order(created_at: :asc).first
                    oldest_history.destroy
                end
            end

            
        end
    end
end



