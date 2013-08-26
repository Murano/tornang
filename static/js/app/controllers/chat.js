chat.controller('ChatCtrl', ['$scope', '$http','$timeout', 'NewMessage', function($scope, $http, $timeout, NewMessage){
    $scope.result = [];
    $scope.cursor = 0;
    $scope.SendMessage = function(){
        NewMessage.save({
            body: $scope.item
        }, function(r){
            $scope.item = null;
        });
    };

    var poller = function() {
        $http.get('/a/message/updates/' + $scope.cursor).then(function(response) {
            $scope.result.push(response.data.messages[0]);
            $scope.cursor = response.data.messages[0].id;
            $timeout(poller, 1000);
        });

    };
    poller();
}]);
