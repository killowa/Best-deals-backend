class WebSitesController < ApplicationController
  def scrap
    @best_products = `python3 app/scrappers/main.py`

    render json: @best_products
  end
end
