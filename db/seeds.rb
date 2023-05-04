# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)

@jumia = Website.create(name: "Jumia", url: "https://www.jumia.com.eg/catalog/?q=")
@amazon = Website.create(name: "Amazon", url: "https://www.amazon.eg/-/en/")
@noon = Website.create(name: "Noon", url: "https://www.noon.com/egypt-en/")