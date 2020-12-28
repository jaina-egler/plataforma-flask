form.addEventListener('submit', function(event) {
    event.preventDefault();    // prevent page from refreshing
    const formData = new FormData(form);  // grab the data inside the form fields
    fetch('/', {   // assuming the backend is hosted on the same server
        method: 'POST',
        body: formData,
    }).then(function(response) {
        // do something with the response if needed.
        // If you want the table to be built only after the backend handles the request and replies, call buildTable() here.
    });
});