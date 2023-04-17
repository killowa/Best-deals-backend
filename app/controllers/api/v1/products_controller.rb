class Api::V1::ProductsController < ApplicationController

    # GET all products
    def index
      # @products = Product.all
      # @products = { "products": "Dell G15 laptop"}
      @products = Product.all
      json_response(@products)
    end
  
    # GET a single product
    def show
      @product = Product.find(params[:id])
      json_response(@product)
    end
  
    # POST a new product
    def create
      if !params[:search_key]&.present?
        return json_response({ error: "Please enter a search item" })
      end
  
      # Create a new search item in searches table
      @search_keyword = SearchKeyword.create(search_key: params[:search_key], website_name: "all")
      @search_keyword.save!
  
      scraped_products = `python3 app/scrappers/main.py "#{params[:search_key]}"`
      # binding.pry

      # replace single quotes with double quotes
      scraped_products = scraped_products.gsub(/'/, '"')
      if scraped_products.empty?
        return json_response({ message: "No results found" })
      end
      @scraped_products = JSON.parse(scraped_products)

      # Create an array of Product objects from the parsed JSON data
      @scraped_products.each do |item|
        # binding.pry
        @new_scraped_product = Product.new(
          name: item['header'],
          price: item['price'],
          link: item['link'],
          rating: item['rate'],
          # score: item['score'],
          reviews_count: item['reviewsCount'],
          img_url: item['imageUrl'],
          source: item['source']
        )
        @new_scraped_product.save!
      end

  
      json_response(@scraped_products)
    end
  
    # def update
    #     @product = Product.find(params[:id])
    #     @product.update(product_params)
    # end
  
    # def destroy
    #     @product = Product.find(params[:id])
    #     @product.destroy
    # end
  
    # def product_params
    #   params.permit(:name, :price, :link, :img_url)
    # end
  end
  