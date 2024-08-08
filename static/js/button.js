document.addEventListener('DOMContentLoaded', (event) => {
    const buttons = document.querySelectorAll('.button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            buttons.forEach(btn => btn.classList.remove('active'));

            button.classList.add('active');
        })
    })
})


document.addEventListener('DOMContentLoaded', (event) => {
    const buttonLuxury = document.getElementById('luxury');
    const buttonSignature = document.getElementById('signature');

    const luxuryContainer = document.getElementById('luxury-container');
    const signatureContainer = document.getElementById('signature-container');

    buttonLuxury.addEventListener('click', () => {
        luxuryContainer.classList.add('active');
        signatureContainer.classList.remove('active');
    });

    buttonSignature.addEventListener('click', () => {
        luxuryContainer.classList.remove('active');
        signatureContainer.classList.add('active');
    });

});


