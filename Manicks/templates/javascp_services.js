  //services page tab switch code 

  function navigation(){
    const tabs = document.querySelectorAll('.tab');
    const tabSelect = document.querySelectorAll('.tab-selected');
    const motor_ignore=document.querySelector('.motor-ignore');
    const fan_ignore=document.querySelector('.fan-ignore');
    const powertool_ignore=document.querySelectorAll('.powertool-ignore');
    
    const formTitle=document.querySelector('.form-title')
  
    function showTab(index) {
        tabs.forEach((tab) => {
        tab.classList.remove('active');
    });
    tabs[index].classList.add('active');
    if (tabs[index].textContent == 'Motor'){
        formTitle.textContent='Motor Detail Entry'
        motor_ignore.style.display='table-row';
    }
    else{
        motor_ignore.style.display='none';
    }
    if (tabs[index].textContent == 'Fan'){
        formTitle.textContent='Fan Detail Entry';
        fan_ignore.style.display='table-row';
      }
      else{
          fan_ignore.style.display='none';
      }
    if (tabs[index].textContent == 'PowerTools'){
        formTitle.textContent='PowerTools Detail Entry'
        powertool_ignore.forEach((tool)=>{
          tool.style.display='table-row';
      });
      }
      else{
          powertool_ignore.forEach((tool)=>{
              tool.style.display='none';
          });
      }
    }
  
    // Initial active tab
    showTab(0);
  
    tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        showTab(index);
    });
    });
  }
  navigation();
  
  // service page tab switch code end