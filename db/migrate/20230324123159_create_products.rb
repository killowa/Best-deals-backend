class CreateProducts < ActiveRecord::Migration[7.0]
  def change
    create_table :products do |t|
      t.string :name
      t.float :price
      t.string :link
      t.float :rating
      t.integer :reviews_count
      t.string :img_url

      t.timestamps
    end
  end
end
