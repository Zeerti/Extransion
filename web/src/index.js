// On Screen Keyboard for GUI so user can input variables


let Keyboard = window.SimpleKeyboard.default;

let selectedInput;

let mainKeyboard = new Keyboard(".registerKeyboard", {
  onChange: input => onChange(input),
  layout: {
    default: ["1 2 3", "4 5 6", "7 8 9", "{bksp}"],
  }
});

document.querySelectorAll(".input").forEach(input => {
  input.addEventListener("focus", onInputFocus);
  // Optional: Use if you want to track input changes
  // made without simple-keyboard
  input.addEventListener("input", onInputChange);
});

function onInputFocus(event) {
  selectedInput = `#${event.target.id}`;

  mainKeyboard.setOptions({
    inputName: event.target.id
  });
}

function onInputChange(event){
  mainKeyboard.setInput(event.target.value, event.target.id);
}

function onChange(input) {
  console.log("Input changed", input);
  document.querySelector(selectedInput || ".input").value = input;
}