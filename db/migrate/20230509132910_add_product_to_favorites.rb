class AddProductToFavorites < ActiveRecord::Migration[7.0]
  def change
    add_reference :favorites, :product
  end
end
