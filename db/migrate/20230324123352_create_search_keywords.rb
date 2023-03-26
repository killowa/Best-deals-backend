class CreateSearchKeywords < ActiveRecord::Migration[7.0]
  def change
    create_table :search_keywords do |t|
      t.string :search_key
      t.string :website_name

      t.timestamps
    end
  end
end
