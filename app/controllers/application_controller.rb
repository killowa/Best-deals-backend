class ApplicationController < ActionController::API
    include Response
    # before_action :init_websites


    def index
      @websites = Website.all
      json_response(@websites)
    end

    rescue_from ActiveRecord::RecordNotFound do |exception|
        json_response({ message: exception.message }, :not_found)
      end

end
