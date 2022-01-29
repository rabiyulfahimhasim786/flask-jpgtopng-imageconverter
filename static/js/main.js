"uase strict";

const selectionArea = document.querySelector("#select-area"),
    fileInput = document.querySelector(".file-input");

let preview = document.getElementById("file-preview");




selectionArea.addEventListener("click", () => {
    fileInput.click();
});

fileInput.onchange = ({
    target
}) => {
    let file = target.files[0];
    if (file.type == "image/jpeg") {
        let image_url = URL.createObjectURL(file);
        preview.src = image_url;
        selectionArea.style.display = "none";

    } else {
        alert("please select a jpg file");
        fileInput.value = null;
    }
}