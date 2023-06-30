class Api::V1::PasswordsController < ApplicationController
  skip_before_action :validate_request, :authenticate_request
    def forgot
      user = User.find_by(email: params[:email])
      if user
        otp = generate_otp
        otp_sent_at= Time.now
        session[:otp] = otp
        session[:otp_sent_at] = otp_sent_at
        UserMailer.forgot_password(user.email,user.username,otp).deliver_later
        render json: { message: 'If this user exists, we have sent you a password reset code.' }, status: :ok
 
      else
        render json: { error: 'User not found' }, status: :not_found
      end

    end

    def password_otp_valid?(otp_sent_at)
      (otp_sent_at + 1.hour.to_s) > Time.zone.now
    end
  
    def reset_password(password,user)
      user.password = password
      user.save!
    end

    def reset
      user = User.find_by(email: params[:email])
      otp = session[:otp]
      if reset_password(params[:password],user)&& password_otp_valid?(session[:otp_sent_at])
            render json: {
              alert: "Your password has been successfully reset!"
            }
            session[:user_id] = user.id
          else
            render json: { error: user.errors.full_messages }, status: :unprocessable_entity
          end
    end
    
    def validation
      user = User.find_by(email: params[:email])
      otp = session[:otp]
      if user.present? && otp == params[:otp] && password_otp_valid?(session[:otp_sent_at])
        render json: { message: 'Code valid.' }, status: :ok
        else
          render json: { error: ['Code invalid'] }, status: :not_found
        end
    end
    
   
   
    # def reset
    #   user = User.find_by(email: params[:email])
    #   otp = session[:otp]
    #   if user.present?
    #     if otp == params[:otp] && password_otp_valid?(session[:otp_sent_at])
    #       if reset_password(params[:password],user)
    #         render json: {
    #           alert: "Your password has been successfully reset!"
    #         }
    #         session[:user_id] = user.id
    #       else
    #         render json: { error: user.errors.full_messages }, status: :unprocessable_entity
    #       end
    #     else
    #       render json: { error: ['Link not valid or expired. Try generating a new link.'] }, status: :not_found
    #     end
    #   end
    # end
    
   

    private 

    def generate_otp
      # Generate a random OTP using a secure method, such as SecureRandom
      SecureRandom.random_number(100000..999999).to_s
    end

  end
  