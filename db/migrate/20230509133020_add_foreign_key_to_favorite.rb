class AddForeignKeyToFavorite < ActiveRecord::Migration[7.0]
  def change
    add_foreign_key :favorites, :users 
    add_foreign_key :favorites, :products

  end
end
