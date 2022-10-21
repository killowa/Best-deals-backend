class WebSitesController < ApplicationController
  def scrap
    @result = `python app/scrappers/amazon.py`

    p @result
  end
end
