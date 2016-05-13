$( () => {
  let submitButton = $('#submit')
  let messageBox = $('#message-box')
  let nameField = $('#name-field')
  let descriptionField = $('#description-field')
  submitButton.on('click', () => {
    let data = {
      name: nameField.val(),
      description: descriptionField.val()
    }
    $.ajax({
      url: 'http://192.168.99.100:5000/api/recurso',
      method: 'POST',
      data: JSON.stringify(data),
      contentType: "application/json",
      success: () => {
        nameField.val('')
        descriptionField.val('')
        messageBox.text('Guardado exitosamente')
      },
      error: () => {
        console.log('ERROR')
      }
    })
  })
})
