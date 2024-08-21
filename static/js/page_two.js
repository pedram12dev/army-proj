document.addEventListener('DOMContentLoaded', function() {
    const changeStatusIndicator = (input) => {
        const questionContainer = input.closest('div[id^="quiz-form2-div"]');
        const indicator = questionContainer.querySelector('.status-indicator');
        if (indicator) {
            if (input.value.trim() === "" || input.value === "disabled") {
                indicator.style.backgroundColor = 'white'; 
            } else {
                indicator.style.backgroundColor = 'orange';
            }
        }
    };

    const inputs = document.querySelectorAll('.input-page2');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            changeStatusIndicator(this);
        });
    });

  
    const selects = document.querySelectorAll('.select-options');
    selects.forEach(select => {
        select.addEventListener('change', function() {
            changeStatusIndicator(this);
        });
    });

//    const nextBtn = document.getElementById('next-btn');
//    nextBtn.addEventListener('click', function(event) {
//        event.preventDefault();
//        if (validateForm()) {
//            window.location.href = './page_three.html';
//        }
//    });

//    const prevBtn = document.getElementById('prev-btn');
//    prevBtn.addEventListener('click', function(event) {
//        event.preventDefault();
//        window.location.href = './page_one.html';
//    });


});