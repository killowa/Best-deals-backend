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
  
      # Check if the search item is already in the database
      @search_keyword = SearchKeyword.find_by(search_key: params[:search_key])
      
      if @search_keyword
        return json_response({ error: "This item has already been searched" })
      end
  
      scraped_jumia = `python3 app/scrappers/main.py "#{params[:search_key]}"`
      # binding.pry

      # replace single quotes with double quotes
      scraped_jumia = scraped_jumia.gsub(/'/, '"')
      if scraped_jumia.empty?
        return json_response({ message: "No results found" })
      end
      @jumia_products = JSON.parse(scraped_jumia)
  
      # render :text => @jumia_products.class



      # Create an array of Product objects from the parsed JSON data
      @jumia_products.each do |item|
        # binding.pry
        @new_jumia_product = Product.new(
          name: item['header'],
          price: item['price'],
          link: item['link'],
          rating: item['rate'],
          # score: item['score'],
          reviews_count: item['reviewsCount'],
          img_url: item['imageUrl'],
          source: item['source'],
        )
        @new_jumia_product.save!
      end


      # check if Porduct objects successfully created in database
      if @new_jumia_product.save
                # Create a new search item in searches table with source name
        @search_keyword = SearchKeyword.create(search_key: params[:search_key], website_name: "all")
      end

      # # Process and store the products in the database
      # @jumia_products.each do |jumia_product|
      #   @new_jumia_product = Product.new(name: jumia_product["name"], price: jumia_product["price"], link: jumia_product["link"], img_url: jumia_product["img"])
      #   @new_jumia_product.save
      # end
  
      # if @new_jumia_product.save
      #   # Create a new search item in searches table
      #   @search_keyword = SearchKeyword.create(search_key: params[:search_key], website_name: "Jumia")
      # end
  
  
    #   scraped_noon = `python3 app/scrapers/noon.py "#{params[:search_key]}"`
    #   @noon_products = JSON.parse(scraped_noon)
  
    #   # render :text => @jumia_products.class
  
    #   # Process and store the products in the database
    #   @noon_products.each do |noon_product|
    #     @new_noon_product = Product.new(name: noon_product["name"], price: noon_product["price"], link: noon_product["link"], img_url: noon_product["img"])
    #     @new_noon_product.save
    #   end
  
    #   if @new_noon_product.save
    #     # Create a new search item in searches table
    #     @search_keyword = SearchKeyword.create(search_key: params[:search_key], website_name: "Noon")
    #   end
  
  
      json_response(@jumia_products)
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
  