  //services page tab switch code 

  function navigation(page){
    console.log(page)
    const tabs = document.querySelectorAll('.tab');
    const tabSelect = document.querySelectorAll('.tab-selected');
    const fan_tab=document.querySelector('.service_table_fan');
    const motor_tab=document.querySelector('.service_table_motor');
    const powertool_tab=document.querySelector('.service-tab-powertools');
    
    const formTitle=document.querySelector('.form-title')

    function showTab(index) {
        tabs.forEach((tab) => {
        tab.classList.remove('active');
    });
    tabs[index].classList.add('active');

    if(page=='motor'){
        formTitle.textContent="Motor Details Entry";
        fan_tab.style.display='none';
        powertool_tab.style.display='none';
        motor_tab.style.display='block';
    }
    else if(page=='fan'){
        formTitle.textContent="Fan Details Entry";
        motor_tab.style.display='none';
        powertool_tab.style.display='none';
        fan_tab.style.display='block';
    }
    else{
        formTitle.textContent="PowerTools Details Entry";
        motor_tab.style.display='none';
        fan_tab.style.display='none';
        powertool_tab.style.display='block';
    }
    }

    showTab(0);
  
    tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        showTab(index);
    });
    });
  }

  navigation('fan')
