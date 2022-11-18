let isUserEligibleFalg = false;
function checkFormIsValid(q1, q2, q3, q4) {
    return q1 && q2 && q3 && q4;
}

function isUserEligible(q1, q2, q3, q4)
{
    return q1 == "Yes" && q2 == "No" && q3 == "No" && q4 == "No"
    
}



$(document).ready(function () {
    // $("#PreCheckPass").modal("show");
    $('.form-check-input').click(function () {
        let q1= $('input[name="q1"]:checked').val();
        let q2= $('input[name="q2"]:checked').val();
        let q3= $('input[name="q3"]:checked').val();
        let q4= $('input[name="q4"]:checked').val();
        var isEligible = checkFormIsValid(q1, q2, q3, q4)
        if(isEligible)
        {
            $('#submit-btn').prop('disabled', false);
        }
        isUserEligibleFalg = isUserEligible(q1, q2, q3, q4)
    });

});

function closePreCheckFailure()
{
    $("#PreCheckFailure").modal("hide"); 
}

function closePreCheckPass()
{
    $("#PreCheckPass").modal("hide");
}

function onSubmit()
{
    if(isUserEligibleFalg) {
        $('#PreCheckPass').modal('show');
    }
    else {
        $('#PreCheckFailure').modal('show');
    }
}
