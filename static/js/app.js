chat = angular.module("chat", ['ngResource', "ui.compat"])

chat.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});