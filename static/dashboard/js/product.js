const doorTypeOptions = {
    'luxury': ['single', 'double', 'none'],
    'single': ['double', 'none'],
    'double': ['none'],
    'none': []
};

function updateImageOptions() {
    const image1Type = document.getElementById('door_type_1').value;
    const image2Select = document.getElementById('door_type_2');
    const image3Select = document.getElementById('door_type_3');

    // Clear existing options
    image2Select.innerHTML = '';
    image3Select.innerHTML = '';

    // Populate options for Image 2
    const image2Options = doorTypeOptions[image1Type] || [];
    image2Options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option.charAt(0).toUpperCase() + option.slice(1);
        image2Select.appendChild(opt);
    });

    // Set default value for Image 2
    if (image2Options.length > 0) {
        image2Select.value = 'none';
    }

    // Call the function to update Image 3 options based on Image 2 selection
    updateImage3Options();
}

function updateImage3Options() {
    const image1Type = document.getElementById('door_type_1').value;
    const image2Type = document.getElementById('door_type_2').value;
    const image3Select = document.getElementById('door_type_3');

    // Clear existing options
    image3Select.innerHTML = '';

    // Determine options for Image 3
    let image3Options = doorTypeOptions[image1Type] || [];
    if (image2Type !== 'none') {
        image3Options = image3Options.filter(option => option !== image2Type);
    }

    image3Options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option.charAt(0).toUpperCase() + option.slice(1);
        image3Select.appendChild(opt);
    });

    // Set default value for Image 3
    if (image3Options.length > 0) {
        image3Select.value = 'none';
    }
}

// Initial population of Image 2 and 3 options
document.getElementById('door_type_1').addEventListener('change', updateImageOptions);
document.getElementById('door_type_2').addEventListener('change', updateImage3Options);

// Set default values and initialize options on page load
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('door_type_1').value = 'luxury';
    updateImageOptions();
});



