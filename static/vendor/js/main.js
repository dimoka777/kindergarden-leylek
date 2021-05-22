let checkInInput = document.getElementById('id_child_birthday');
checkInInput.value = new Date().toJSON().slice(0, 10);
checkInInput.min = new Date(Date.now() - 1000 * 60 * 60 * 24 * 365 * 5).toJSON().slice(0, 10);
checkInInput.max = new Date(Date.now() - 1000 * 60 * 60 * 24 * 365 * 2).toJSON().slice(0, 10);

let date_