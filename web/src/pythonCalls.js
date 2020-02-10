element = document.getElementById('start');
element.addEventListener('click', start);




function isKitchenChecked(){
    isKitchen = document.getElementById('isKitchen');
    return isKitchen.checked;
}

function validate_data(event) {
    registerNumber = document.getElementById('default');
    loginCode = document.getElementById('input2');
    iterations = document.getElementById('input3');
    delay = document.getElementById('input4');
    // default input2 input3
    
    registerValue = Number(registerNumber.value);
    loginValue = Number(loginCode.value);
    iterationsValue = Number(iterations.value);
    delayValue = Number(delay.value);


    // flag to return on if validated or not
    let validated = false;
    
    if(registerValue <= 0 || registerValue >= 41) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nRegister value was set above the maximum threshold, 40 \n\nPlease change your input and try again` );
        return validated;
    }
    else if(registerValue <= 0 || registerValue >= 41) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nRegister value was set below the minimum threshold, 1 \n\nPlease change your input and try again` );
        return validated;
    }
    else if(registerValue === '' || registerValue === undefined || registerValue === null) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nRegister value was left blank\n\nPlease input a register and try again` );
        return validated;
    }
    else if(loginValue === '' || loginValue === undefined || loginValue === null) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nLogin code was left blank.\n\nPlease input a login code and try again`);
        return validated;
    }
    else if(loginCode.value.length < 3) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nLogin code was not at least 3 digits long\n\nPlease input a valid login code and try again`);
        return validated;
    }
    else if(loginCode.value.length > 12) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nLogin code was longer than 12 digits\n\nPlease input a valid login code and try again`);
        return validated;
    }
    else if(iterationsValue === '' || iterationsValue === null || iterationsValue === undefined) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nIteration was left blank.\n\nPlease input a valid iteration and try again`);
        return validated;
    }
    else if(iterationsValue <= 0) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nIteration value was set below minimum threshold of 0\n\nPlease input a valid iteration and try again`);
        return validated;
    }
    else if(iterationsValue >= 10001) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nIteration was over 10000\n\nPlease input a valid iteration and try again`);
        return validated;
    }
    else if(delayValue === '' || delayValue === undefined || delayValue === null) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nDelay value was not set\n\nPlease input a valid delay value and try again`);
        return validated;
    }
    else if(delayValue < .25) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nDelay value was set below minimum threshold of .25\n\nPlease input a valid delay value and try again`);
        return validated;
    }
    else if(delayValue > 5) {
        eel.showPopup('alert', 'Invalid Input', `===ERROR===:\nDelay value was set above the maximum threshold of 5\n\nPlease input a valid delay value and try again`);
        return validated;
    } else {
        validated = true;
        return validated;
    }


    // eel.execution(values)
}

function start() {
    console.log("Kitchen: ",isKitchenChecked(),"\nValid: ", validate_data())
    if(isKitchenChecked()){
        console.log("Bumping it up yo")
        eel.bump()
    } else {
        console.log("Validating");
        validated = validate_data()
    }
    
    if(validated) {
        console.log("STARTING THINGS");
        eel.showPopup('alert', 'Things would run here', `Minimize Extransion window, then click OK to begin`);
        eel.assembly(loginCode.value, registerValue, iterationsValue, delay.value)
    }
}