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

// spares lookup page

function search_criteria(){
  const dates=document.querySelector('.dates');
  const search_box=document.querySelector('.search-dabba');
  var dropdown = document.getElementById("searchfilter");
  
  if(dropdown.value=="date"){
      dates.style.display='block';
      search_box.style.display='none';    
  }
  else{
      dates.style.display='none';
      search_box.style.display='block';
  }
}
search_criteria()

let listofelements=["python","pyth","py","javascript","java","script","scripter"];
const rpstat_searchbox=document.querySelector("spare_search_rpstat");

function search_filter_rps(){
  console.log("worling");

}
