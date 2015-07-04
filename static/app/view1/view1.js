'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope', '$http', function($scope, $http) {
  $http.defaults.headers.common['Authorization'] = 'Token c2366049741f8e192089d3cd4b8e91ebc6556151';
    $http.get('http://127.0.0.1:8000/brownetapi/usuarios/').
      success(function(data){
        $scope.usuarios = data;
      }).error(function(data, status, headers,config){
          $scope.error = status;
      });
  }]);