'use strict';

$(function () {
  var submitButton = $('#submit');
  var messageBox = $('#message-box');
  var nameField = $('#name-field');
  var descriptionField = $('#description-field');
  submitButton.on('click', function () {
    var data = {
      name: nameField.val(),
      description: descriptionField.val()
    };
    $.ajax({
      url: 'http://192.168.99.100:5000/api/recurso',
      method: 'POST',
      data: JSON.stringify(data),
      contentType: "application/json",
      success: function success() {
        nameField.val('');
        descriptionField.val('');
        messageBox.text('Guardado exitosamente');
      },
      error: function error() {
        console.log('ERROR');
      }
    });
  });
});