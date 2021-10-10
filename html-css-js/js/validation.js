const form = document.querySelector("form");
const inputCheckbox = form.querySelectorAll("input[name=section]");
const submitButton = form.querySelector("submitButton");

function checkCheckbox(theForm) {
    if (
        theForm.section1.checked ==false &&
        theForm.section2.checked ==false &&
        theForm.section3.checked ==false &&
        theForm.section4.checked ==false) {
            alert("Wybierz conajmniej jedną sekcje");
            return false;
        } else {
            return true
        }
}