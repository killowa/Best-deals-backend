class AddUserToHistories < ActiveRecord::Migration[7.0]
  def change
    add_reference :histories, :user
  end
end
