element = document.getElementById('start');
element.addEventListener('click', start);

registerNumber = document.getElementById('default');
loginCode = document.getElementById('input2');
iterations = document.getElementById('input3');

// default input2 input3

function start(event) {
    console.warn(registerNumber.value, loginCode.value, iterations.value);
    eel.order(iterations.value);
}
