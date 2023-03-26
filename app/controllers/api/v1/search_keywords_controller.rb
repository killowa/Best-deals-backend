class Api::V1::SearchKeywordsController < ApplicationController

    def index
        @search_keywords = SearchKeyword.all
        json_response(@search_keywords)
    end

end
