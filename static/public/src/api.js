$( () => {
  let submitButton = $('#submit')
  let messageBox = $('#message-box')
  let nameField = $('#name-field')
  let descriptionField = $('#description-field')
  let successAlert = `<div class="alert alert-success alert-dismissible fade in" role="alert">
                 <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                   <span aria-hidden="true">×</span>
                 </button>
                 Guardado exitosamente
               </div>`
  submitButton.on('click', () => {
    let data = {
      name: nameField.val(),
      description: descriptionField.val()
    }
    $.ajax({
      url: 'http://api:5000/api/recurso',
      method: 'POST',
      data: JSON.stringify(data),
      contentType: "application/json",
      success: () => {
        nameField.val('')
        descriptionField.val('')
        messageBox.html(successAlert)
      },
      error: () => {
        console.log('ERROR')
      }
    })
  })
})
