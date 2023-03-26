Rails.application.routes.draw do
  get 'web_sites/scrap'
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"

  namespace :api do
    namespace :v1 do
      resources :products
      # post "scrape", to: "websites#scrape"
      get "searches", to: "search_keywords#index"
      get "websites", to: "websites#list_websites"
    end
  end

  # resources :products


end
