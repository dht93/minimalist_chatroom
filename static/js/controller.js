var chat_beta = angular.module('myapp', []);

chat_beta.controller('my_controller', function($scope){
  var socket = io.connect('http://'+document.domain+':'+location.port + '/chat');

  $scope.messages=[];
  $scope.name='';
  $scope.text='';

  socket.on('connect', function(){
    console.log('Connected!');
  });
  //$scope.setName= function setName(){
  //  socket.emit('identify',$scope.name)
  //};
  socket.on('message',function(msg){
    console.log(msg);
    $scope.messages.push(msg);
    $scope.$apply();
  });
  $scope.send = function send(){
    console.log($scope.text);
    socket.emit('message',$scope.text,$scope.name);
    $scope.text='';
  };

  });
