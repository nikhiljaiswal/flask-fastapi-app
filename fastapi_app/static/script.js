document.getElementById('animal-form').addEventListener('change', function() {
    const selectedAnimal = document.querySelector('input[name="animal"]:checked').value;
    
    fetch(`/animal?name=${selectedAnimal}`)
        .then(response => response.json())
        .then(data => {
            const img = document.getElementById('animal-image');
            img.src = data.image_url;
            img.hidden = false; // Show the image when an animal is selected
        })
        .catch(error => {
            console.error('Error fetching animal image:', error);
        });
});

function uploadFile() {
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // Log the data received from the server
            document.getElementById('file-name').textContent = data.filename || 'No filename returned';
            document.getElementById('file-size').textContent = data.filesize || 'No filesize returned';
            document.getElementById('file-type').textContent = data.filetype || 'No filetype returned';

            const fileInfo = document.querySelector('.file-info');
            fileInfo.hidden = false; // Show file info after a successful upload
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to upload file. Please try again.'); // User feedback for upload failure
        });
    } else {
        alert('Please select a file to upload.'); // User feedback for no file selected
    }
}
