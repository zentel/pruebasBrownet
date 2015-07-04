'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.view1',
  'myApp.version',
  'myApp.newUser'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/new', {
    templateUrl: 'view1/new_user.html',
    controller: 'NewUserCtrl'
  });
  $routeProvider.otherwise({redirectTo: '/view1'});
}]);
