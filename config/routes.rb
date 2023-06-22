Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"

  namespace :api do
    namespace :v1 do
      resources :products, :histories, :favorites
      resources :websites, only: :index
      resources :users, only: :create do
        collection do
          post 'login'
          post 'logout'
        end
      end

      get "searches", to: "search_keywords#index"
      get "websites", to: "websites#list_websites"
      resources :favorites do
        collection do
          post 'create'
          get "favorites",to:"favorites#index"
          post 'destroy'
        end
      end
       
      resources :ratings do
        collection do
          post 'create'
          get 'ratings', to: 'ratings#index'
        end
      end

      resources :histories do
          collection do
          get 'histories', to: 'histories#index'
          post 'create'
          end
        end
      end
  end

end
