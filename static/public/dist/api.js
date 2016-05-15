'use strict';

$(function () {
  var submitButton = $('#submit');
  var messageBox = $('#message-box');
  var nameField = $('#name-field');
  var descriptionField = $('#description-field');
  var alert = '<div class="alert alert-success alert-dismissible fade in" role="alert">\n                 <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n                   <span aria-hidden="true">×</span>\n                 </button>\n                 Guardado exitosamente\n               </div>';
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
        messageBox.html(alert);
      },
      error: function error() {
        console.log('ERROR');
      }
    });
  });
});