class SearchKeyword < ApplicationRecord
    validates :search_key, uniqueness: { case_sensitive: false, message: "search key previously searched" }

end
