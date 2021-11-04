window.addEventListener('load', () => {
    var customAmountRadioButton = document.getElementById('inlineRadio3');
    var customAmountField = document.getElementById('amount');

    customAmountRadioButton.addEventListener("change", function(event) {
        if (event.target.checked) {
            customAmountField.disabled = false;

        } else {
            customAmountField.disabled = true;
        }
      });
  })