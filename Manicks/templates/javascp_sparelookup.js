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