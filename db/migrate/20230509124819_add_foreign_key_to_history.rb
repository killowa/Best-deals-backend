class AddForeignKeyToHistory < ActiveRecord::Migration[7.0]
  def change
    add_foreign_key :histories, :users
    add_foreign_key :histories, :products
  end
end
