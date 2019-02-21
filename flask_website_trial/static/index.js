'use strict';

var app = angular.module('myShoppingList', [
    'ngRoute',
]);

app.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '../static/partials/home.html',
                controller: 'myCtrl',
            }).
            when('/contact', {
                templateUrl: '../static/partials/contact.html',
                controller: 'myCtrl',
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);
// var app = angular.module('myShoppingList', ['ngRoute']); 

// app.config(function($routeProvider) {
//     $routeProvider
//     .when("/contact", {
//         templateUrl : "partials/contact.html",
//         controller : "myCtrl"
//     })
//     .otherwise({
//         redirectTo: '/'
//     });
// });

app.controller("myCtrl", function ($scope, $http) {


    $scope.test = "test from scope variable";
    //test
    $scope.name = function(ks){
        $scope.kulwisin = ks;
    };

    $scope.product_image = "http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg";
    $scope.products = ["Milk", "Bread", "Cheese"];
    $scope.students = [
        { name: "Steave", grade: "A" },
        { name: "Mark", grade: "C" },
        { name: "Robert", grade: "B" },
        { name: "Jenny", grade: "B" },
        { name: "James", grade: "A" }
    ];

    //This should be converted into GET request where REST provides the products information
    // $scope.test_new = [
    //     {
    //         "product_id": 1,
    //         "product_name": "one",
    //         "product_image": "/static/images/m1.png",
    //         "product_description": "description of product 1",
    //         "product_price": 132,
    //         "product_quantity": 100
    //     },
    //     {
    //         "product_id": 2,
    //         "product_name": "two",
    //         "product_image": "/static/images/m2.png",
    //         "product_description": "description of product 2",
    //         "product_price": 432,
    //         "product_quantity": 200
    //     },
    //     {
    //         "product_id": 1,
    //         "product_name": "one",
    //         "product_image": "/static/images/m3.png",
    //         "product_description": "description of product 1",
    //         "product_price": 132,
    //         "product_quantity": 100
    //     },
    //     {
    //         "product_id": 2,
    //         "product_name": "two",
    //         "product_image": "/static/images/m4.png",
    //         "product_description": "description of product 2",
    //         "product_price": 432,
    //         "product_quantity": 200
    //     },
    //     {
    //         "product_id": 1,
    //         "product_name": "one",
    //         "product_image": "/static/images/m5.png",
    //         "product_description": "description of product 1",
    //         "product_price": 132,
    //         "product_quantity": 100
    //     }

    // ];

    // 1'st API call-------------------------------------------
    $http.get('localhost:5000/getProducts').
    then(function(response) {
        $scope.test_new =response.data;
        $scope.test_new = $scope.test_new.items
        //console.log($scope.test_new)
    });

    $scope.myTxt = "Nothing submitted";
    $scope.myFunc = function (mail) {

        $scope.id = document.getElementById("txtEmail");

        $scope.myTxt = mail;
        alert("Message has been successfully sent");

    }

});
