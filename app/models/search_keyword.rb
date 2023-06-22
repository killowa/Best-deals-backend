class SearchKeyword < ApplicationRecord
    has_many :products
    validates :search_key, uniqueness: { case_sensitive: false, message: "previously searched!" }

end
