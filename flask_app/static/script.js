// Handle animal selection and image display
document.querySelectorAll('input[name="animal"]').forEach(input => {
    input.addEventListener('change', () => {
        const selectedAnimal = document.querySelector('input[name="animal"]:checked').value;
        fetch(`/animal/${selectedAnimal}`)
            .then(response => response.json())
            .then(data => {
                const img = document.getElementById('animal-image');
                img.src = data.image_url;
                img.style.display = 'block';
            });
    });
});

// Handle file upload
document.getElementById('file-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file-input').files[0];
    const formData = new FormData();
    formData.append('file', fileInput);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const fileInfoDiv = document.getElementById('file-info');
        fileInfoDiv.innerHTML = `<p>File Name: ${data.filename}</p>
                                 <p>File Size: ${data.filesize} bytes</p>
                                 <p>File Type: ${data.filetype}</p>`;
    });
});
