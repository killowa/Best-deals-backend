class SearchKeyword < ApplicationRecord
    validates :search_key, uniqueness: { case_sensitive: false, message: "previously searched!" }

end
