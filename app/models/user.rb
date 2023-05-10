class User < ApplicationRecord
  has_many :histories
  has_many :products, through: :histories
  include TokenManager
  before_validation :downcase_email

  has_secure_password

  EMAIL_REGEX =  /\A([^-]+?)+@[a-z\d\-]+(\.[a-z]+)*\.[a-z]+\z/i
  PASSWORD_REGEX = /\A(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z\d])(?!.*\s).*\z/

  validates :username, :email, :password, presence: true

  validates :username, length: { minimum: 3, maximum: 30 }, uniqueness: { case_sensitive: false }

  validates :email, format: { with: EMAIL_REGEX }, uniqueness: true

  validates :password, length: { minimum: 8, maximum: 50 }

  validates :password, format: { with: PASSWORD_REGEX }
  
  has_many :favorites
  has_many :products, through: :favorites
  private

  def downcase_email
    self.email = email.downcase if email.present?
  end
end
