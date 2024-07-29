
// Quote Read Status - one by ID
function updateQuoteReadStatus(checkbox, quoteId) {
    const form = document.getElementById(`read-form-${quoteId}`);
    const formData = new FormData(form);
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            checkbox.style.display = 'none';
            var span = document.createElement('span');
            span.className = 'read-indicator';
            checkbox.parentNode.appendChild(span);
        } else {
            alert('Failed to update status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// ALl quotes together mark as read

function markAllAsRead() {
    const form = document.getElementById('mark-all-read-form');
    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the UI to reflect the changes
            document.querySelectorAll('input[type="checkbox"][name="quote_ids"]').forEach(checkbox => {
                checkbox.style.display = 'none';
                var span = document.createElement('span');
                span.className = 'read-indicator';
                checkbox.parentNode.appendChild(span);
            });
        } else {
            alert('Failed to update status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// FindDealers Read Status - one by ID
function updateFindDealerReadStatus(checkbox, findDealerId) {
    const form = document.getElementById(`read-form-findDealer-${findDealerId}`);
    const formData = new FormData(form);
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            checkbox.style.display = 'none';
            var span = document.createElement('span');
            span.className = 'read-indicator';
            checkbox.parentNode.appendChild(span);
        } else {
            alert('Failed to update status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


// ALl quotes together mark as read

function markAllFindDealerAsRead() {
    const form = document.getElementById('mark-all-find-dealer-read-form');
    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the UI to reflect the changes
            document.querySelectorAll('input[type="checkbox"][name="find_dealer_ids"]').forEach(checkbox => {
                checkbox.style.display = 'none';
                var span = document.createElement('span');
                span.className = 'read-indicator';
                checkbox.parentNode.appendChild(span);
            });
        } else {
            alert('Failed to update status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// NewDealers Read Status - one by ID
function updateNewDealerReadStatus(checkbox, newDealerId) {
    const form = document.getElementById(`read-form-newDealer-${newDealerId}`);
    const formData = new FormData(form);
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            checkbox.style.display = 'none';
            var span = document.createElement('span');
            span.className = 'read-indicator';
            checkbox.parentNode.appendChild(span);
        } else {
            alert('Failed to update status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


// ALl quotes together mark as read

function markAllNewDealerAsRead() {
    const form = document.getElementById('mark-all-find-dealer-read-form');
    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the UI to reflect the changes
            document.querySelectorAll('input[type="checkbox"][name="find_dealer_ids"]').forEach(checkbox => {
                checkbox.style.display = 'none';
                var span = document.createElement('span');
                span.className = 'read-indicator';
                checkbox.parentNode.appendChild(span);
            });
        } else {
            alert('Failed to update status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}