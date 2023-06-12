class Rating < ApplicationRecord
    belongs_to :user
    validates :rate, presence: true, numericality: { only_integer: true, less_than_or_equal_to: 5 }
end
