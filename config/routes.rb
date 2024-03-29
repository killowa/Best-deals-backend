Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"

  namespace :api do
    namespace :v1 do
      resources :products, :histories, :ratings
      resources :websites, only: :index
      resources :users, only: :create do
        collection do
          post 'login'
          post 'logout'
        end
      end
      resources :passwords, only: [] do
        collection do
          post :forgot
          post :validation
          post :reset
        end
      end
      resources :favorites do
        collection do
          post 'destroy'
        end
      end

      get "searches", to: "search_keywords#index"

      end
  end

end
