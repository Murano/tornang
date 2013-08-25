chat.controller('ChatCtrl', ['$scope', function($scope){
    $scope.SendMessage = function(item){
        $scope.result = item;
    }
}]);