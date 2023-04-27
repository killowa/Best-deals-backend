class Product < ApplicationRecord
    # belongs_to :website
    # after_create :create_search_keyword

    # def create_search_keyword(search_keyword, website_name)
    #     SearchKeyword.create(search_key: search_keyword, website_name: website_name)
    # end

    # def save_with_keyword(search_keyword)
    #     self.search_keyword = search_keyword
    #     save!
        
    #     SearchKeyword.create(keyword: search_keyword)
    #   end


end
