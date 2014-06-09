var app = angular.module('JobApp', []);

app.config(function($interpolateProvider) { 
    $interpolateProvider.startSymbol('{$'); 
    $interpolateProvider.endSymbol('$}');

});

app.run(function($rootScope, $http) {
    //$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


function ReportController($scope, $http) {

    $scope.searchQuery = function() {
        $scope.$apply(function() {
            console.log($scope.queryParams);
            $http({method: 'GET', url: '/api/v1.0/search/?'+$scope.queryParams}).
            success(function(data, status, headers, config) {
                $scope.results = data;                  //set view model
            }).
            error(function(data, status, headers, config) {
                $scope.results = data || "Busqueda Fallida";
                $scope.status = status;
            });
        });
    }
}
ReportController.$inject = ['$scope', '$http'];

ReportController.searchQuery();
