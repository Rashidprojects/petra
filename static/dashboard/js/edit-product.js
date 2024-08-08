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

    // Populate options for image2 based on image1
    if (image1Type && doorTypeOptions[image1Type]) {
        doorTypeOptions[image1Type].forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option.charAt(0).toUpperCase() + option.slice(1);
            image2Select.appendChild(opt);
        });
    }

    // Populate options for image3 based on image2
    const image2Type = document.getElementById('door_type_2').value;
    if (image2Type && doorTypeOptions[image2Type]) {
        doorTypeOptions[image2Type].forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option.charAt(0).toUpperCase() + option.slice(1);
            image3Select.appendChild(opt);
        });
    }

    // Set the default values from the hidden inputs
    document.getElementById('door_type_1').value = document.getElementById('door_type_1_default').value;
    document.getElementById('door_type_2').value = document.getElementById('door_type_2_default').value;
    document.getElementById('door_type_3').value = document.getElementById('door_type_3_default').value;
}

function updateImage2Options() {
    const image1Type = document.getElementById('door_type_1').value;
    const image2Select = document.getElementById('door_type_2');

    // Clear existing options
    image2Select.innerHTML = '';

    // Populate options for image2 based on image1
    if (image1Type && doorTypeOptions[image1Type]) {
        doorTypeOptions[image1Type].forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option.charAt(0).toUpperCase() + option.slice(1);
            image2Select.appendChild(opt);
        });

        // Trigger update for image3 options
        updateImage3Options();
    }
}

function updateImage3Options() {
    const image2Type = document.getElementById('door_type_2').value;
    const image3Select = document.getElementById('door_type_3');

    // Clear existing options
    image3Select.innerHTML = '';

    // Populate options for image3 based on image2
    if (image2Type && doorTypeOptions[image2Type]) {
        doorTypeOptions[image2Type].forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option.charAt(0).toUpperCase() + option.slice(1);
            image3Select.appendChild(opt);
        });
    }
}

// Attach event listeners
document.getElementById('door_type_1').addEventListener('change', updateImage2Options);
document.getElementById('door_type_2').addEventListener('change', updateImage3Options);

// Initialize options on page load
document.addEventListener('DOMContentLoaded', () => {
    updateImageOptions();
});
