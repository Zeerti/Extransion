element = document.getElementById('start');
element.addEventListener('click', start);

function closeKeyboard() {
    keyboardElement = document.getElementById('keyboard');
    keyboardElement.className = 'hidden';
    formElement = document.getElementById("primary-form");
    formElement.className = "form";
}


function isKitchenChecked(){
    let isKitchen = document.getElementById('isKitchen');
    return isKitchen.checked;
}

function isSkippingClockin() {
    let isSkippingClockin = document.getElementById('skipClockin')
    return isSkippingClockin.checked
}

function validate_data() {
    registerNumber = document.getElementById('default');
    loginCode = document.getElementById('input2');
    iterations = document.getElementById('input3');
    delay = document.getElementById('input4');
    minimumOrderDelay = document.getElementById('input5');
    maximumOrderDelay = document.getElementById('input6');
    // default input2 input3
    
    registerValue = Number(registerNumber.value);
    loginValue = Number(loginCode.value);
    iterationsValue = Number(iterations.value);
    delayValue = Number(delay.value);
    minimumOrderDelay = Number(minimumOrderDelay.value);
    maximumOrderDelay = Number(maximumOrderDelay.value);


    // flag to return on if validated or not
    let validated = false;
    
    if(registerValue <= 0 || registerValue >= 41) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nRegister value was set above the maximum threshold, 40 \n\nPlease change your input and try again` );
        return validated;
    }
    else if(registerValue <= 0 || registerValue >= 41) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nRegister value was set below the minimum threshold, 1 \n\nPlease change your input and try again` );
        return validated;
    }
    else if(registerValue === '' || registerValue === undefined || registerValue === null) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nRegister value was left blank\n\nPlease input a register and try again` );
        return validated;
    }
    else if(loginValue === '' || loginValue === undefined || loginValue === null) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nLogin code was left blank.\n\nPlease input a login code and try again`);
        return validated;
    }
    else if(loginCode.value.length < 3) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nLogin code was not at least 3 digits long\n\nPlease input a valid login code and try again`);
        return validated;
    }
    else if(loginCode.value.length > 12) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nLogin code was longer than 12 digits\n\nPlease input a valid login code and try again`);
        return validated;
    }
    else if(iterationsValue === '' || iterationsValue === null || iterationsValue === undefined) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nIteration was left blank.\n\nPlease input a valid iteration and try again`);
        return validated;
    }
    else if(iterationsValue <= 0) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nIteration value was set below minimum threshold of 0\n\nPlease input a valid iteration and try again`);
        return validated;
    }
    else if(iterationsValue >= 10001) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nIteration was over 10000\n\nPlease input a valid iteration and try again`);
        return validated;
    }
    else if(delayValue === '' || delayValue === undefined || delayValue === null) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nDelay value was not set\n\nPlease input a valid delay value and try again`);
        return validated;
    }
    else if(delayValue < .25) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nDelay value was set below minimum threshold of .25\n\nPlease input a valid delay value and try again`);
        return validated;
    }
    else if(delayValue > 5) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nDelay value was set above the maximum threshold of 5\n\nPlease input a valid delay value and try again`);
        return validated;
    }
    else if(maximumOrderDelay < minimumOrderDelay) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nMaximum Order Delay was set to a lower number than the Minimum Order Delay\n\nPlease input a number greater than the Minimum Order Delay and try again` )
    }
    else if(minimumOrderDelay > maximumOrderDelay) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nMinimum Order Delay was set to a higher number than the Maximum Order Delay\n\nPlease input a number less than the Maximum Order Delay and try again` )
    }
    else if(maximumOrderDelay > 10000) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nMaximum Order Delay larger than 10000 seconds\n\nPlease input a number lower than 10001 and try again` );
    }
    else if(maximumOrderDelay < 2) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nMaximum Order Delay lower than 2 seconds\n\nPlease input a number higher than 2 and try again` );
    }
    else if(minimumOrderDelay > 9999) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nMinimum Order Delay larger than 9999 seconds\n\nPlease input a number lower than 10000 and try again` );
    }
    else if(minimumOrderDelay < 1) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\n\nMinimum Order Delay lower than 1 second\n\nPlease input a number greater than 1 and try again` );
    }
    else {
        validated = true;
        return validated;
    }


    // eel.execution(values)
}

function start() {
    closeKeyboard();
    let validated;

    // Execute kitchen
    // Check to make sure they don't check both boxes
    if(isKitchenChecked() === true && isSkippingClockin() === true) {
        eel.showPopup('alert', 'Invalid Option', `===ERROR===\n\nCannot check both option boxes.\n\nPlease select one or the other`);
        return null;
    } else if(isKitchenChecked()) {
        console.log("Beginning bumping")
        eel.showPopup('alert', 'Preparing to Start Test', `Minimize Extransion windows, then click OK to begin`);
        eel.bump()
        return null;
    }

    console.log("Validating");
    validated = validate_data()
    // check various flags to determine how to execute for register
    if(isSkippingClockin()) {
        if(validated){
            console.log('Starting "Skip Clockin/CD Assign" Sequence');
            eel.showPopup('alert', 'Preparing to Start Test', `Minimize Extransion window, then click OK to begin`);
            eel.assembly(loginCode.value, registerValue, iterationsValue, delay.value, true, minimumOrderDelay, maximumOrderDelay);
            return null;
        }
    } else if(isKitchenChecked() === false && validated){
        console.log("Starting Normal Sequence");
        eel.showPopup('alert', 'Preparing to Start Test', `Minimize Extransion window, then click OK to begin`);
        eel.assembly(loginCode.value, registerValue, iterationsValue, delay.value, false, minimumOrderDelay, maximumOrderDelay);
        return null
    }
}