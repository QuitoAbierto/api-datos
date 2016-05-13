require "minitest/autorun"
require 'capybara'
require 'capybara/dsl'
require 'capybara/cucumber'

World(MiniTest::Assertions)
MiniTest::Spec.new(nil)

Capybara.configure do |config|
  config.run_server = false
  config.default_driver = :selenium
  config.app_host = ENV['APP_HOST'] || 'http://localhost:3000'
end
