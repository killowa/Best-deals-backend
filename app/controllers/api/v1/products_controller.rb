class Api::V1::ProductsController < ApplicationController

    # filter, sort, paginate products (all optional)
    def index

      #example: http://localhost/...products?filter[price_eq]=100&filter[rating_gteq]=4.8&sort_column=price&sort_order=asc&page=1&per_page=10

      @search = Product.ransack(params[:filter])

      ## Default parameters
      # params[:sort_column] ||= 'price'
      params[:sort_order] ||= 'desc'
      params[:sort_column] ||= 'score'
      params[:page] ||= 1
      params[:per_page] ||= 10

      # Check if sort_column is valid
      if !Product.column_names.include?(params[:sort_column])
        return json_response({ error: "Invalid sort column" })
      end

      # Check if sort_order is valid
      if params[:sort_order] != "asc" && params[:sort_order] != "desc"
        return json_response({ error: "Invalid sort order" })
      end

      @search.sorts = ["#{params[:sort_column]} #{params[:sort_order]}"] if @search.sorts.empty?

      @products = @search.result.page(params[:page]).per(params[:per_page])

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

      # if search item already exists, must redirect to the index method
      if SearchKeyword.exists?(search_key: params[:search_key])
        
        # add ?filter[name_i_cont]=#{params[:search_key]} to the url
        @search = Product.ransack({ name_i_cont: params[:search_key] })
        # sort by score desc
        @search.sorts = ["score desc"]
        @products = @search.result.page(1).per(10)

        return json_response(@products)
      end

      ActiveRecord::Base.transaction do

        scraped_products = `python3 app/scrappers/main.py "#{params[:search_key]}"`

        # replace single quotes with double quotes
        scraped_products = scraped_products.gsub(/'/, '"')
        if scraped_products.empty?
          return json_response({ message: "No results found" })
        end
        @scraped_products = JSON.parse(scraped_products)

        # Create an array of Product objects from the parsed JSON data
        @scraped_products.each do |item|
          @new_scraped_product = Product.new(
            name: item['header'],
            price: item['price'],
            link: item['link'],
            rating: item['rate'],
            reviews_count: item['reviewsCount'],
            img_url: item['imageUrl'],
            source: item['source'],
            score: item['score'],
            search_keyword_id: @search_keyword.id
          )
          @new_scraped_product.save!
        end

        # Create a new search item in searches table
        @search_keyword = SearchKeyword.create!(search_key: params[:search_key], website_name: "all")
        @search_keyword.save!
    end
    Product.update_products_without_img_url(@search_keyword.id)

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
  