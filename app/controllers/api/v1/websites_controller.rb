class Api::V1::WebsitesController < ApplicationController
  
    # GET all websites we are scraping
    def list_websites
      @websites = Website.all
      json_response(@websites)
    end
  end
  