
module Api
    module V1
        class Api::V1::HistoriesController < ApplicationController
            before_action :authenticate_request
            after_action :limit_histories
            MAX_HISTORIES = 8
            
            def index
                @histories = current_user.histories
                render json: @histories
            end
            
            
            def create
                if !params[:product_id]&.present?
                    return json_response({ error: "Please enter product id" })
                end

                

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



