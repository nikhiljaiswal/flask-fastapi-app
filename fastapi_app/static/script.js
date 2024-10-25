document.getElementById('animal-form').addEventListener('change', function() {
    const selectedAnimal = document.querySelector('input[name="animal"]:checked').value;
    
    fetch(`/animal?name=${selectedAnimal}`)
        .then(response => response.json())
        .then(data => {
            const img = document.getElementById('animal-image');
            img.src = data.image_url;
            img.hidden = false; // Show the image when animal is selected
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
        .then(response => response.json())
        .then(data => {
            document.getElementById('file-name').textContent = data.filename; // Match with FastAPI response
            document.getElementById('file-size').textContent = data.filesize; // Match with FastAPI response
            document.getElementById('file-type').textContent = data.filetype; // Match with FastAPI response

            const fileInfo = document.querySelector('.file-info');
            fileInfo.hidden = false; // Show file info only after a file is uploaded
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}
