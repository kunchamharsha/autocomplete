app.controller('search',function($http,$scope){
    $scope.jobtitle=''
    
    $scope.searchnames=function(){
        return $http({url:'/api/search',method:'GET',params:{'searchterm':$scope.jobtitle}}).then(function(response,status){
            $scope.names=response.data
        });
    }
});