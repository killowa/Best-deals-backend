class Favorite < ApplicationRecord
    belongs_to :user
    belongs_to :product
    validates :product_id, uniqueness: {  message: "previously added!" }

end
