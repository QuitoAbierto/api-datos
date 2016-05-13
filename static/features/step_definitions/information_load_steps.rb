
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
end

Cuando(/^envío el formulario$/) do
  page.find('#submit').click
end

Entonces(/^veo un mensaje de confirmación$/) do
  message_box = page.find '#message-box'
  assert message_box.has_content?('Guardado exitosamente'), 'Message not shown!'
end
