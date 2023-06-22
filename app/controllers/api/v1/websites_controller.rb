class Api::V1::WebsitesController < ApplicationController
  
    # GET all websites we are scraping
    def index
      @websites = Website.all
      json_response(@websites)
    end
  end
  