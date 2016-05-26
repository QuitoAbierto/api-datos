'use strict';

$(function () {
  var config = require('./config.js');
  var submitButton = $('#submit');
  var messageBox = $('#message-box');
  var nameField = $('#name-field');
  var descriptionField = $('#description-field');
  var successAlert = '<div class="alert alert-success alert-dismissible fade in" role="alert">\n    <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n      <span aria-hidden="true">×</span>\n    </button>\n    Guardado exitosamente\n  </div>';
  var errorAlert = '<div class="alert alert-warning alert-dismissible fade in" role="alert">\n    <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n      <span aria-hidden="true">×</span>\n    </button>\n    Todos los campos son obligatorios\n  </div>';
  submitButton.on('click', function () {
    var name = nameField.val();
    var description = descriptionField.val();
    if (!!name && !!description && !!selectedLocation) {
      var data = {
        name: name,
        description: description,
        location: selectedLocation
      };
      $.ajax({
        url: config.api.host + 'api/recurso',
        method: 'POST',
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function success() {
          nameField.val('');
          descriptionField.val('');
          messageBox.html(successAlert);
        },
        error: function error() {
          console.log('Error accessing the API');
        }
      });
    } else {
      messageBox.html(errorAlert);
    }
  });
});