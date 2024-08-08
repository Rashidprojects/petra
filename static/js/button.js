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
    const buttonAll = document.getElementById('all');
    const buttonLuxury = document.getElementById('luxury');
    const buttonSingle = document.getElementById('single');
    const buttonDouble = document.getElementById('double');

    const allContainer = document.getElementById('all-container');
    const luxuryContainer = document.getElementById('luxury-container');
    const singleContainer = document.getElementById('single-container');
    const doubleContainer = document.getElementById('double-container');

    buttonAll.addEventListener('click', () => {
        allContainer.classList.add('active');
        luxuryContainer.classList.remove('active');
        singleContainer.classList.remove('active');
        doubleContainer.classList.remove('active');
    });

    buttonLuxury.addEventListener('click', () => {
        allContainer.classList.remove('active');
        luxuryContainer.classList.add('active');
        singleContainer.classList.remove('active');
        doubleContainer.classList.remove('active');
    });

    buttonSingle.addEventListener('click', () => {
        allContainer.classList.remove('active');
        luxuryContainer.classList.remove('active');
        singleContainer.classList.add('active');
        doubleContainer.classList.remove('active');
    });

    buttonDouble.addEventListener('click', () => {
        allContainer.classList.remove('active');
        luxuryContainer.classList.remove('active');
        singleContainer.classList.remove('active');
        doubleContainer.classList.add('active');
    });
});


