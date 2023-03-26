class ApplicationController < ActionController::API
    include Response
    before_action :init_websites


    def init_websites
      # This method will be called before any other actions in the controller

      # Create entries for every website in the database
      # This is so that we can easily add more websites to scrape from
      # in the future
      @websites = Website.all
      if @websites.length == 0
        @jumia = Website.create(name: "Jumia", url: "https://www.jumia.com.eg/catalog/?q=")
        @amazon = Website.create(name: "Amazon", url: "https://www.amazon.eg/-/en/")
        @noon = Website.create(name: "Noon", url: "https://www.noon.com/egypt-en/")
      end
    end

    rescue_from ActiveRecord::RecordNotFound do |exception|
        json_response({ message: exception.message }, :not_found)
      end

end
