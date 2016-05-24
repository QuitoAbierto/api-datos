require "minitest/autorun"
require 'capybara'
require 'capybara/dsl'
require 'capybara/cucumber'
require 'capybara-screenshot/cucumber'
require 'capybara/poltergeist'

World(MiniTest::Assertions)
MiniTest::Spec.new(nil)

Capybara.configure do |config|
  config.run_server = false
  config.default_driver = :poltergeist
  config.current_driver = :poltergeist
  config.javascript_driver = :poltergeist
  config.app_host = ENV['APP_HOST'] || 'http://web'
end

Capybara.save_and_open_page_path = "/tmp/screenshot"
