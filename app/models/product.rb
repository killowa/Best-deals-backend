class Product < ApplicationRecord
    has_many :histories
    has_many :users, through: :histories
    
    def self.products_without_img_url
        where(img_url: "")
      end
    def self.product_with_img_url
        where.not(img_url: "").first
    end
    def self.update_products_without_img_url
        product_with_img_url = product_with_img_url()
        products_without_img_url.each do |product|
          product.update(img_url: product_with_img_url.img_url)
        end
    end
    # belongs_to :website
    # after_create :create_search_keyword

    # define searchable attributes
    def self.ransackable_attributes(auth_object = nil)
        %w[id name price link rating reviews_count img_url source score created_at updated_at]
    end
    has_many :wish_lists
    has_many :users, through: :wish_lists
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
