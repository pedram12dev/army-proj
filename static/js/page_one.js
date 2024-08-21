document.addEventListener('DOMContentLoaded', function() {


    const changeStatusIndicator = (input) => {
        const questionContainer = input.closest('.quiz-form');
        const indicator = questionContainer.querySelector('.status-indicator');

        if (indicator) {
            if (input.value.trim() === "" || input.value === "disabled") {
                indicator.style.backgroundColor = 'white';
            } else {
                indicator.style.backgroundColor = 'orange';
            }
        }
    };



    const inputs = document.querySelectorAll('.input-page1');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            changeStatusIndicator(this);
        });
    });

    const radioButtons = document.querySelectorAll('.options-radio-page1');

    const handleSquareClick = function() {
        const radio = this.nextElementSibling;
        if (radio) {
            radio.checked = true;
            updateStatusAndSquare(radio);
        }
    };

    const updateStatusAndSquare = function(radio) {
        const optionContainer = radio.closest('.option-container-page1');

        if (!optionContainer) {
            console.error("Option container not found");
            return;
        }

        const statusIndicator = optionContainer.closest('.quiz-form').querySelector('.status-indicator');

        const squares = optionContainer.parentElement.querySelectorAll('.square');

        squares.forEach(square => {
            square.style.backgroundColor = '';
        });

        const clickedSquare = radio.previousElementSibling;
        if (clickedSquare) {
            clickedSquare.style.backgroundColor = 'gray';

            if (statusIndicator) {
                statusIndicator.style.backgroundColor = '#FFA500';
            }
        }
    };

    const squares = document.querySelectorAll('.square');
    squares.forEach(square => {
        square.addEventListener('click', handleSquareClick);
    });

    radioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            updateStatusAndSquare(this);
        });
    });

    const daysAfterBackacheInput = document.getElementById('daysAfterBackache');

    const updateStatusIndicatorForTextArea = () => {
        const statusIndicator = document.querySelector('.status-indicator');
        if (daysAfterBackacheInput.value.trim() !== "") {
            statusIndicator.style.backgroundColor = '#FFA500';
        } else {
            statusIndicator.style.backgroundColor = 'white';
        }
    };

    daysAfterBackacheInput.addEventListener('input', updateStatusIndicatorForTextArea);

    const nextBtn = document.getElementById('next-btn');
    const prevBtn = document.getElementById('prev-btn');

    nextBtn.addEventListener('click', function() {
        const answers = {};
        const selectedAnswer = document.querySelector('.selected-answer').value;
        answers['martial_status'] = selectedAnswer;
        answers['daysAfterBackache'] = daysAfterBackacheInput.value;

    });

//    prevBtn.addEventListener('click', function() {
//        window.location.href = "{% url 'core:base_page' %}";
//    });
});
