  // code for sidepane

  function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

// end of side pane code



// tab change start here
/*
const tabs = document.querySelectorAll(".tab");
const tabsContant = document.querySelectorAll(".tab-contant");

function showTab(index) {
  tabs.forEach((tab) => {
    tab.classList.remove("active");
  });
  tabs[index].classList.add("active");

  // Add animation using CSS transitions
  tabsContant.forEach((contant) => {
    contant.style.transition = "width 0.3s ease-in-out"; // Transition animation
    contant.style.maxWidth = 300; // Initially hide all content
  });
  tabsContant[index].style.maxWidth = tabsContant[index].scrollWidth + "px"; // Expand selected content
}

showTab(0); // Show the first tab initially

tabs.forEach((tab, index) => {
  tab.addEventListener("click", () => {
    showTab(index);
  });
});*/

// tabc chnage end
function showTab(a){
  
  if(a==0){
    document.getElementById("fan").style.width="100%";
    document.getElementById("motor").style.width="0px";
    document.getElementById("power").style.width="0px";
    
    /*document.getElementById("fan").style.opacity="1";
    document.getElementById("motor").style.opacity="0";
    document.getElementById("power").style.opacity="0";*/
  }
  else if(a==1){
    document.getElementById("fan").style.width="0";
    document.getElementById("motor").style.width="100%";
    document.getElementById("power").style.width="0px";

    /*document.getElementById("fan").style.opacity="0";
    document.getElementById("motor").style.opacity="1";
    document.getElementById("power").style.opacity="0";*/
  }
  else{
    document.getElementById("fan").style.width="0px";
    document.getElementById("motor").style.width="0px";
    document.getElementById("power").style.width="100%";

    /*document.getElementById("fan").style.opacity="0";
    document.getElementById("motor").style.opacity="0";
    document.getElementById("power").style.opacity="1";*/
  }

}


function additemActive(){
  const additem=document.querySelector('.additem');
  additem.style.display="flex";
}

function additemDeactive(){
  const additem=document.querySelector('.additem');
  additem.style.display="none";
}

function discountamt(){
  const discount=document.querySelector('.DISCOUNT');
  const total=document.querySelector('.BILLAMOUNT');
  console.log(discount,total);
}