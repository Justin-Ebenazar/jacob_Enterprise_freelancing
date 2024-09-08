  // code for sidepane

  function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

// end of side pane code

//service page tab switch code

function showTab(a){
  const tabs = document.querySelectorAll(".tab");
  const tabsContent= document.querySelectorAll(".tab-content");
  
//changing the tab indicator style

  tabs.forEach((tab) => {
    tab.classList.remove("active");
  });
  tabs[a].classList.add("active");

  //changing tab content

  tabsContent.forEach((content) => {
    content.classList.remove("active");
  });
  tabsContent[a].classList.add("active");

}

//end of service page tab switch code

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
