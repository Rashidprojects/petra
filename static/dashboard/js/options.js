document.addEventListener('DOMContentLoaded', function () {
    // Get references to the dropdowns
    const doorType1 = document.getElementById('door_type_1');
    const doorType2 = document.getElementById('door_type_2');

    // Function to update door_type_2 options based on door_type_1 selection
    function updateDoorType2Options() {
        const selectedValue1 = doorType1.value;

        // Clear existing options in door_type_2
        doorType2.innerHTML = '<option value="">Select Door Type</option>';

        // Define possible options
        const options = [
            { value: 'Luxury', text: 'Luxury' },
            { value: 'Signature', text: 'Signature' },
            { value: 'None', text: 'None' }
        ];

        // Populate door_type_2 based on door_type_1 selection
        if (selectedValue1) {
            options.forEach(option => {
                // Add options based on the selection in door_type_1
                if (selectedValue1 === 'Luxury' && (option.value === 'Signature' || option.value === 'None')) {
                    const newOption = document.createElement('option');
                    newOption.value = option.value;
                    newOption.textContent = option.text;
                    doorType2.appendChild(newOption);
                } else if (selectedValue1 === 'Signature' && (option.value === 'Luxury' || option.value === 'None')) {
                    const newOption = document.createElement('option');
                    newOption.value = option.value;
                    newOption.textContent = option.text;
                    doorType2.appendChild(newOption);
                } else if (selectedValue1 === 'None' && option.value === 'None') {
                    const newOption = document.createElement('option');
                    newOption.value = option.value;
                    newOption.textContent = option.text;
                    doorType2.appendChild(newOption);
                }
            });
        }
    }

    // Event listener for when door_type_1 changes
    doorType1.addEventListener('change', updateDoorType2Options);

    // Initialize the door_type_2 dropdown when the page loads
    updateDoorType2Options();
});