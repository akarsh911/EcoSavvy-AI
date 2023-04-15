
function check()
{
    const data1 = document.getElementById('parts'); 
    const data2 = document.getElementById('lifespan'); 
    const data3 = document.getElementById('percent');  
    const data4 = document.getElementById('text-title');
    const data5 = document.getElementById('text-body');
    const data6 = document.getElementById('text-body1');
    data4 += data1;
    data5 += data5 + 'Lifespan :' + data2 + 'years.';
    if(data3 > 10)
    {
        data6 += data6 + 'Shred';
    }
    else if(data3 < 3)
    {
        data6 += data6 + 'Refurbish';
    }
    else
    {
        data6 += data6 + 'Disassemble';
    }
}