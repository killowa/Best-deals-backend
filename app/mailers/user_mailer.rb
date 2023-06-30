class UserMailer < ApplicationMailer
    def forgot_password(user_email,user_username, otp)
      @otp = otp
      @username=user_username
      mail to: user_email, subject: "Reset Your Password"
    end
  end
 