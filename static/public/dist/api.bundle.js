/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';

	$(function () {
	  var config = __webpack_require__(1);
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

/***/ },
/* 1 */
/***/ function(module, exports) {

	module.exports = {
	  api : {
	    host : 'http://quitoabierto.org:5000/'
	  }
	};


/***/ }
/******/ ]);