function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }
  function navigation(){
  const tabs = document.querySelectorAll('.tab');
  const tabSelect = document.querySelectorAll('.tab-selected');
  const hp=document.querySelector('.motorexclusive');
  const fab=document.querySelector('.fanexclusive');
  const powerb=document.querySelector('.powerexclusive');
  const formTitle=document.querySelector('.form-title')

  function showTab(index) {
    tabs.forEach((tab) => {
        tab.classList.remove('active');
    });
    tabs[index].classList.add('active');
    console.log("God is Good");
    
    hp.style.display
    if (tabs[index].textContent == 'Fan') {
        /*formTitle.textContent = 'Fan Detail Entry';*/
        hp.style.display='table-row';
        fab.style.display='none';
        powerb.style.display='none';
    } 
    else if (tabs[index].textContent == 'Fan') { 
        /*formTitle.textContent = 'Fan Detail Entry';*/
        fab.style.display = 'table-row';
        hp.style.display = 'none';
        powerb.style.display = 'none';
    } else{
        /*formTitle.textContent = 'PowerTools Detail Entry';*/
        powerb.style.display = 'table-row';
        hp.style.display = 'none';
        fab.style.display = 'none';
    }
}

  // Initial active tab
  /*showTab(0);*/

  tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => {
      showTab(index);
  });
  });
}
