class AddSearchKeywordIdToProducts < ActiveRecord::Migration[7.0]
  def change
    add_reference :products, :search_keyword, foreign_key: true
  end
end
