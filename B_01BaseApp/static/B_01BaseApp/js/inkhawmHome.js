window.addEventListener('scroll', function() {
    var elements = document.querySelectorAll('.fade-in');
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      var position = element.getBoundingClientRect();
      // If the element is in the viewport
      if (position.top < window.innerHeight) {
        element.classList.add('active');
      }
    }
  });

  function calculateSumMt() {
    // matthaia
    var a = parseInt(document.getElementById("matgrp").value);
    var b = parseInt(document.getElementById("matmem").value);
    
    if (!isNaN(a) && !isNaN(b)) {
        document.getElementById("mattotal").value = a + b;
        // document.getElementById("gtotal").value =  parseInt(document.getElementById("mattotal").value);
    };
  };

  function calculateSumMk() {
    // marka
    var c = parseInt(document.getElementById("margrp").value);
    var d = parseInt(document.getElementById("marmem").value);
    
    if (!isNaN(c) && !isNaN(d)) {
        document.getElementById("martotal").value = c + d;
        // document.getElementById("gtotal").value =  parseInt(document.getElementById("mattotal").value)+parseInt(document.getElementById("martotal").value);
    };
};

function calculateSumLk() {
    // luka
    var e = parseInt(document.getElementById("lukagrp").value);
    var f = parseInt(document.getElementById("lukamem").value);
    
    if (!isNaN(e) && !isNaN(f)) {
        document.getElementById("lukatotal").value = e+f;
        // document.getElementById("gtotal").value =  parseInt(document.getElementById("mattotal").value)+parseInt(document.getElementById("martotal").value)+parseInt(document.getElementById("lukatotal").value);
    };
};

function calculateSumJh() {
    // johana
    var e = parseInt(document.getElementById("johanagrp").value);
    var f = parseInt(document.getElementById("johanamem").value);
    
    if (!isNaN(e) && !isNaN(f)) {
        document.getElementById("johanatotal").value = e+f;
        // document.getElementById("gtotal").value =  parseInt(document.getElementById("mattotal").value)+parseInt(document.getElementById("martotal").value)+parseInt(document.getElementById("lukatotal").value)+parseInt(document.getElementById("johanatotal").value);
    };
};

function sum() {
    // Leader leh secy.
    var ls = parseInt(document.getElementById("leadrSecy").value);
    if (!isNaN(ls)) {
        document.getElementById("gtotal").value =  parseInt(document.getElementById("mattotal").value)+parseInt(document.getElementById("martotal").value)+parseInt(document.getElementById("lukatotal").value)+parseInt(document.getElementById("johanatotal").value)+parseInt(document.getElementById("leadrSecy").value);
    };
};

function sumChhimtu() {
    // Leader leh secy.
    alert('chhimtu');
    var ls = parseInt(document.getElementById("chhimtu1_no_id").value);
    alert(ls);
    if (!isNaN(ls)) {
        alert('chhimtu inside nana');
        alert(`Total so far is: ${document.getElementById("gtotal").value}`);
    //     document.getElementById("gtotal").value =  parseInt(document.getElementById("mattotal").value)+parseInt(document.getElementById("martotal").value)+parseInt(document.getElementById("lukatotal").value)+parseInt(document.getElementById("johanatotal").value)+parseInt(document.getElementById("leadrSecy").value)+parseInt(document.getElementById("chhimtu1_no_id").value);
    };
};

    // Get the toggle button and input field
    const toggleBtn = document.getElementById("toggle-input");
    const inputField = document.getElementById("chhimtu1_id");
    const inputField2 = document.getElementById("chhimtu1_no_id");
    // const inputField = document.getElementById("my-input");

    // Add event listener to toggle button
    toggleBtn.addEventListener("change", function () {
      if (this.checked) {
        // Enable input and change placeholder
        inputField.disabled = false;
        inputField.required = true;
        // inputField.placeholder = "Input is enabled";
        inputField2.disabled = false;
        inputField2.placeholder = "Input is enabled";
      } else {
        // Disable input and change placeholder
        inputField.disabled = true;
        // inputField.required = false;
        inputField.placeholder = "Input is disabled";
        inputField2.disabled = true;
        inputField2.placeholder = "Input is disabled";
      }
    });


    function addChhimtu(arg){
      alert("Hellow from add button"+arg);
      document.getElementById("addchhimtu").innerHTML = "buttonAddClicked";
  }