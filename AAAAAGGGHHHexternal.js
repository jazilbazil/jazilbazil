function appear()
{
    document.getElementById('myImg').style.display = 'block';

    let myRed = document.getElementById("mycolor").value;
    let myBlue = document.getElementById("mycolour").value;
    let myGreen = document.getElementById("mycolur").value;


    document.getElementById('tester').backgroundColor = `rgb(${myRed}, ${myBlue}, ${myGreen})`;
}
