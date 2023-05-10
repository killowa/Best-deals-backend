Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"

  namespace :api do
    namespace :v1 do
      resources :products
      resources :users, only: :create do
        collection do
          post 'login'
          post 'logout'
        end
      end
      # post "scrape", to: "websites#scrape"
      get "searches", to: "search_keywords#index"
      get "websites", to: "websites#list_websites"
      resources :favorites do
        collection do
          post 'create'
          get "favorites",to:"favorites#index"
          post 'destroy'
        end
      end
        end
  end

  # resources :products


end
