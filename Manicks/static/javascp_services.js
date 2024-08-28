  //services page tab switch code 

  // code for sidepane

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

// end of side pane code

tabs = document.querySelectorAll(".tab");
tabsContant = document.querySelectorAll(".tab-contant")

function showTab(index){
 tabs.forEach((tab)=>{
    tab.classList.remove("active");
 });
tabs[index].classList.add('active');

tabsContant.forEach((contant)=>{
  contant.style.display="none";
});
tabsContant[index].style.display="flex"
}
showTab(0);
tabs.forEach((tab,index)=>{
    tab.addEventListener("click",()=>{
        showTab(index);
    });
});

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

