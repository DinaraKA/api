const a = $('#input1');
const b = $('#input2');

function success(data) {
   let answer = `<p style="color:green">${data.answer}</p>`;
   $('.answer').append(answer);
   }

function error(data) {
    text = JSON.parse(data.responseText);
    let answer = `<p style="color:red">${text.error}</p>`;
    $('.answer').append(answer);
 }

function add(){
    $.ajax({
        url: "http://localhost:8000/add/",
        method: "POST",
        dataType:'json',
        contentType:'application/json',
        data: JSON.stringify({"A" : a.value, "B" : b.value}),
        success: success,
        error: error
    });
}
function subtract(){
    $.ajax({
        url: "http://localhost:8000/subtract/",
        method: "POST",
        dataType:'json',
        contentType:'application/json',
        data: JSON.stringify({'A' : a.value, 'B' : b.value}),
        success: success,
        error: error
    });
}

function multiply(){
    $.ajax({
        url: "http://localhost:8000/multiply/",
        method: "POST",
        dataType:'json',
        contentType:'application/json',
        data: JSON.stringify({'A' : a.value, 'B' : b.value}),
        success: success,
        error: error
    });
}

function divide(){
    $.ajax({
        url: "http://localhost:8000/divide/",
        method: "POST",
        dataType:'json',
        contentType:'application/json',
        data: JSON.stringify({'A' : a.value, 'B' : b.value}),
        success: success,
        error: error
    });
}