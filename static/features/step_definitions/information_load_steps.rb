require_relative '../helpers/wait'

Dado(/^que ingreso a la aplicación$/) do
  page.visit '/'
end

Cuando(/^estoy en la página de inicio$/) do
end

Entonces(/^veo un mapa$/) do
  page.find '#my-map'
end

Cuando(/^lleno el formulario con los siguientes datos:$/) do |table|
  data = table.hashes[0]
  fill_in 'name-field', :with => data['nombre']
  fill_in 'description-field', :with => data['descripción']
  lat, long = data['ubicación'].split(',')
  execute_script("selectedLocation = {lat: #{lat}, long: #{long}}")
end

Cuando(/^envío el formulario$/) do
  page.click_link('submit')
end

Entonces(/^veo el mensaje "([^"]*)"$/) do |message|
  wait_for_ajax
  message_box = page.find '#message-box'
  assert message_box.has_content?(message), 'Message not shown!'
end
