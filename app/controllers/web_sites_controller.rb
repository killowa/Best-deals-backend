class WebSitesController < ApplicationController
  def scrap
    if params[:search_keys]&.empty?
      render json: {error: I18n.t('error.missing_param')}, status: :unprocessable_entity
    else
      @best_products = `python3 app/scrappers/main.py "#{params[:search_keys]}"`
      render json: @best_products, status: :ok
    end
  end
end
