var sata;
fetch('../get/inventory')
    .then(response => response.json())
    .then(data => window.localStorage.setItem('inventory', JSON.stringify(data)))
    .catch(error => console.error(error));
let data = JSON.parse(window.localStorage.getItem('inventory'));
var count = data.length;
var da = "";
for (var i = 0; i < count; i++) {

    let ht = `<tr>
        <td>`+ data[i].s_no + `.</td>
        <td>`+ data[i].state + `</td>
        <td>`+ data[i].maximum_capacity + `</td>
        <td>`+ data[i].current_ewaste + `</td>
      </tr>`;
    da += ht;
}
document.getElementById("t_body").innerHTML += da;