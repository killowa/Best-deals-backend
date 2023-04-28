class Product < ApplicationRecord
    # belongs_to :website
    # after_create :create_search_keyword

    # define searchable attributes
    def self.ransackable_attributes(auth_object = nil)
        %w[id name price link rating reviews_count img_url source created_at updated_at]
    end

    # def self.ransack_error
    #     if params[:q].present?
    #       disallowed_attributes = params[:q].keys - self.ransackable_attributes
    #       if disallowed_attributes.present?
    #         return {
    #           errors: {
    #             message: "The following attributes are not allowed: #{disallowed_attributes.join(', ')}"
    #           }
    #         }
    #       end
    #     end
    # end
    # def create_search_keyword(search_keyword, website_name)
    #     SearchKeyword.create(search_key: search_keyword, website_name: website_name)
    # end

    # def save_with_keyword(search_keyword)
    #     self.search_keyword = search_keyword
    #     save!
        
    #     SearchKeyword.create(keyword: search_keyword)
    #   end


end
