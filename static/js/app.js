chat = angular.module("chat", ['ngResource', "ui.compat"])

chat.config(function($interpolateProvider, $locationProvider) {
    $locationProvider.html5Mode(true);
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});