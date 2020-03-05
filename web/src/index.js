// Javascript file  strictly controlling the way the GUI displays and looks
// On Screen Keyboard for GUI so user can input variables


let Keyboard = window.SimpleKeyboard.default;

let selectedInput;

let mainKeyboard = new Keyboard(".registerKeyboard", {
  onChange: input => onChange(input),
  layout: {
    default: ["1 2 3", "4 5 6", "7 8 9", "0 . {bksp}"],
  }
});

document.querySelectorAll(".input").forEach(input => {
  input.addEventListener("focus", onInputFocus);
  input.addEventListener("input", onInputChange);
  // input.addEventListener("blur", onFocusLoss);
});

closeNumpad = document.getElementById('close');
closeNumpad.addEventListener('click', onFocusLoss)



function onInputFocus(event) {
  keyboardElement = document.getElementById('keyboard');
  formElement = document.getElementById("primary-form");

  // formElement.className = "form displaced";
  keyboardElement.className = 'keyboard-wrapper';
  
  selectedInput = `#${event.target.id}`;

  mainKeyboard.setOptions({
    inputName: event.target.id
  });
}

function onFocusLoss(event) {
  keyboardElement = document.getElementById('keyboard');
  keyboardElement.className = 'hidden';
  formElement = document.getElementById("primary-form");
  formElement.className = "form";
}

function onInputChange(event){
  mainKeyboard.setInput(event.target.value, event.target.id);
}

function onChange(input) {
  console.log("Input changed", input);
  document.querySelector(selectedInput || ".input").value = input;
}