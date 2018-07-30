console.log("switchurlupload loaded...");

function hideFileUpload() {
    console.log("hideFileUpload() exe...");
    document.getElementById('verify-by-upload').checked = false;
    document.getElementById('fileUploadBlock').style.display = 'none';
    document.getElementById('urlInputBlock').style.display = 'block';
}

function hideUrlInput() {
    console.log("hideUrlInput() exe...");
    document.getElementById('verify-by-url').checked = false;
    document.getElementById('urlInputBlock').style.display = 'none';
    document.getElementById('fileUploadBlock').style.display = 'block';
}
