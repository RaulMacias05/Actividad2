const inpcolor = document.getElementById("color");
const form = document.getElementById("idform");

inpcolor.addEventListener('change', function() {
    form.style.boxShadow = `0 0 1vh ${inpcolor.value}`;
});
