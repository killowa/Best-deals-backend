class AddUserToFavorites < ActiveRecord::Migration[7.0]
  def change
    add_reference :favorites, :user
  end
end
