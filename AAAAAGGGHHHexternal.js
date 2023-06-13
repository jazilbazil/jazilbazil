function appear()
{
    document.getElementById('myImg').style.display = 'block';

    let myRed = document.getElementById("mycolor").value;
    let myBlue = document.getElementById("mycolon").value;
    let myGreen = document.getElementById("mycola").value;
    
    if(myRed > 255)
    {
        document.getElementById('mycolor').value = 255;
        myRed = 255;
    }
    if(myBlue > 255)
    {
        document.getElementById('mycolon').value = 255;
        myBlue = 255;
    }
    if(myGreen > 255)
    {
        document.getElementById('mycola').value = 255;
        myGreen = 255;
    }
    
    else{
        document.getElementById('tester').style.backgroundColor = `rgb(${myRed}, ${myBlue}, ${myGreen})`;

    }


}
