'use strict';

angular.module('myApp.newUser', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/newUser', {
    templateUrl: 'view1/new_user.html',
    controller: 'NewUserCtrl'
  });
}])

.controller('NewUserCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
  $scope.usuario = { "nombre" : "","apellido" : "","edad" : ""};
  $scope.newUser = function(){
        var datos = {
                      nombre : $scope.usuario.nombre,
                      apellido : $scope.usuario.apellido,
                      edad : $scope.usuario.edad
                    }
        $http.defaults.headers.common['Authorization'] = 'Token c2366049741f8e192089d3cd4b8e91ebc6556151';
        $http.post('http://127.0.0.1:8000/brownetapi/usuarios/',datos).
          success(function(data){
            $location.path("/");  // Con el servicio "$location" redirecciona a la url "/"
          }).error(function(data, status, headers,config){
            $scope.error = status;
        });
  }  
  }]);