var sata;
fetch('../get/logistics')
    .then(response => response.json())
    .then(data => window.localStorage.setItem('logistics', JSON.stringify(data)))
    .catch(error => console.error(error));
let data = JSON.parse(window.localStorage.getItem('logistics'));
var count = data.length;
var da = "";
for (var i = 0; i < count; i++) {

    let ht = `<tr>
        <td>`+ data[i].s_no + `.</td>
        <td>`+ data[i].state_from + `</td>
        <td>`+ data[i].state_to + `</td>
        <td>`+ data[i].purpose + `</td>
        <td>`+ data[i].quantity + `</td>
      </tr>`;
    da += ht;
}
document.getElementById("t_body").innerHTML += da;