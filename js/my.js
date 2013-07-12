/*jslint unparam: true */
/*global window, $ */
//$();

function BodyController($scope) {

    $scope.texts = ["a", "b", "c"];

    var url = '/upload';
    $('#fileupload').fileupload({
        url: url,
        dataType: 'json',
        done: function (e, data) {
            $scope.load(data);
            if (data.result.length != 0) {
                console.log("result" + data.result);
                $("#progress").addClass("progress-success");
                $("#result").show();
            } else {
                $("#progress").addClass("progress-danger");
                $("#file-type-error").show();
            }

            $("#upload-btn").hide();
            $("#progress").removeClass("active");
        },

        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            $('#progress .bar').css(
                'width',
                progress + '%'
                );
        }
    });

    $scope.load = function(data) {
        console.log("finish");
        $scope.texts = data.result;
        angular.forEach($scope.texts, function(t) {
            console.log("t" + t);
        });
        $scope.$apply();
    }
}
