
function check()
{
    var data1 = document.getElementById('parts').value; 
    var data2 = document.getElementById('lifespan').value; 
    var data3 = document.getElementById('percent').value;  
    var data4 = document.getElementById('text-title').value;
    var data5 = document.getElementById('text-body').value;
    var data6 = document.getElementById('text-body1').value;
   
    if(data3 > 10)
    {
        document.getElementById('text-body1').innerHTML='Shred';
    }
    else if(data3 < 3)
    {
        document.getElementById('text-body1').innerHTML='Refurbish';
    }
    else
    {
        document.getElementById('text-body1').innerHTML='Disassemble';
    }
    document.getElementById('text-title').innerHTML=data1;
    document.getElementById('text-body').innerHTML='Lifespan :' + data2 + 'years.';
    return false;
}
var form = document.getElementById("formId");
function handleForm(event) { event.preventDefault(); } 
form.addEventListener('submit', handleForm);