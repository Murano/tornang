chat.factory("NewMessage", function($resource) {
    return $resource('/a/message/new');
});