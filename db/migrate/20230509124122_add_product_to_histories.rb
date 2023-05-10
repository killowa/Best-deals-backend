class AddProductToHistories < ActiveRecord::Migration[7.0]
  def change
    add_reference :histories, :product
  end
end
