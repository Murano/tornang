chat.controller('ChatCtrl', ['$scope', '$http','$timeout', 'NewMessage', '$anchorScroll', '$location',
    function($scope, $http, $timeout, NewMessage, $anchorScroll, $location){
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
            $scope.result = $scope.result.concat(response.data.messages);
            len = response.data.messages.length;
            $scope.cursor = response.data.messages[len-1].id;
            $location.hash(len);
            $anchorScroll();
            $timeout(poller, 1000);
        }, function(response){
            $timeout(poller, 3000);
        });

    };
    poller();
}]);
