// code for sidepane

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

// end of side pane code

// spares lookup page

function search_criteria(){
    const serach_criteria=document.querySelectorAll('.helo');
    var dropdown = document.getElementById("searchfilter");
    var selectedValue = dropdown.value;
    console.log(selectedValue)

}