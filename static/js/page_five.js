document.addEventListener('DOMContentLoaded', function() {
    const radioButtons = document.querySelectorAll('.options-radio');

    const handleSquareClick = function() {
        const radio = this.nextElementSibling; 
        if (radio) {
            radio.checked = true; 
            updateStatusAndSquare(radio);
        }
    };

    const updateStatusAndSquare = function(radio) {
        const optionContainer = radio.closest('.option-container');

        if (!optionContainer) {
            console.error("Option container not found");
            return; 
        }

        const statusIndicator = optionContainer.parentElement.querySelector('.status-indicator');
        const squares = optionContainer.parentElement.querySelectorAll('.square'); 

        squares.forEach(square => {
            square.style.backgroundColor = ''; 
        });

        const clickedSquare = radio.previousElementSibling; 
        if (clickedSquare) {
            clickedSquare.style.backgroundColor = 'gray';
        }

        if (statusIndicator) {
            statusIndicator.style.backgroundColor = '#FFA500';
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


});