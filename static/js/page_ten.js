document.addEventListener('DOMContentLoaded', function() {
    const optionContainers = document.querySelectorAll('.option-container-page10');

    const updateStatusAndSquare = function(radio) {
        const quizForm = radio.closest('.quiz-form3-1');

        const previousSquares = quizForm.querySelectorAll('.square');
        previousSquares.forEach(square => {
            square.classList.remove('selected');
        });

        const previousStatusIndicator = quizForm.querySelector('.status-indicator');
        if (previousStatusIndicator) {
            previousStatusIndicator.style.backgroundColor = '';
        }

        const clickedSquare = radio.closest('.option-container-page10').querySelector('.square');
        if (clickedSquare) {
            clickedSquare.classList.add('selected');
        }

        const statusIndicator = quizForm.querySelector('.status-indicator');
        if (statusIndicator) {
            statusIndicator.style.backgroundColor = '#FFA500';
        }

        const hiddenInput = quizForm.querySelector('input[name^="answer_"]');
        hiddenInput.value = radio.value;
    };

    const handleOptionClick = function() {
        const radio = this.querySelector('input[type="radio"]');
        if (radio) {
            radio.checked = true;
            updateStatusAndSquare(radio);
        }
    };

    optionContainers.forEach(container => {
        const square = container.querySelector('.square');
        const radio = container.querySelector('.options-radio-page10');

        if (square) {
            square.addEventListener('click', handleOptionClick);
        }

        if (radio) {
            radio.parentElement.addEventListener('click', handleOptionClick);
        }
    });
});