class SearchKeyword < ApplicationRecord
    has_many :products
    validates :search_key, uniqueness: { scope: :website_name, case_sensitive: false }

end
