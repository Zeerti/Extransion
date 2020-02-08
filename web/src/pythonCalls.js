element = document.getElementById('start');
element.addEventListener('click', start);

registerNumber = document.getElementById('default');
loginCode = document.getElementById('input2');
iterations = document.getElementById('input3');
delay = document.getElementById('input4');

// default input2 input3


function start(event) {
    console.log(Number(registerNumber.value));
    console.log(loginCode.value);
    console.log(Number(iterations.value));
    if(Number(registerNumber.value) <= 0 || Number(registerNumber.value) >= 41) {
        eel.showPopup('alert', 'Invalid Input', `You input: ${registerNumber.value} for the register number.\nThis number cannot be any larger than 40 or less than 1\n\nPlease change your input and try again` )
    }
    if(loginCode.value === '' || loginCode.value === undefined || loginCode.value === null) {
        eel.showPopup('alert', 'Invalid Input', `Login code was left blank.\n\nPlease input a login code and try again`)
    }
    if(loginCode.value.length <= 3) {
        eel.showPopup('alert', 'Invalid Input', `Login code was not at least 4 digits long\n\nPlease input a valid login code and try again`)
    }
    if(loginCode.value.length >= 12) {
        eel.showPopup('alert', 'Invalid Input', `Login code was longer than 12 digits\n\nPlease input a valid login code and try again`)
    }

    // eel.execution(values)
}
