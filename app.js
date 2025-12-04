document.getElementById('form-matric').addEventListener("submit", checkForm);

function checkForm(event) {
    event.preventDefault();
    const el = document.getElementById('form-matric');

    const a = Number(el.a.value);
    const b = Number(el.b.value);
    const c = Number(el.c.value);
    const d = Number(el.d.value);
    const e = Number(el.e.value);
    const f = Number(el.f.value);
    const g = Number(el.g.value);
    const h = Number(el.h.value);
    const i = Number(el.i.value);

    const sum = (a * e * i) + (b * f * g) + (d * h * c) - (c * e * g) - (a * h * f) - (d * b * i);

    var file = "";
    if (a == "" || b == "" || c == "" || d == "" || e == "" || f == "" || g == "" || h == "" || i == "") {
        file = "Заполните все поля";
    }
    if (file != "") {
        document.getElementById('error').innerHTML = file;

    } else {
        document.getElementById('result').innerHTML = "Результат: " + sum;
    }
}