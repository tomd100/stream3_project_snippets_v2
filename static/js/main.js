// -----------------------------------------------------------------------------
// Video Functions




// -----------------------------------------------------------------------------
// Snippet Controls

function controlToggle(){
    var list_div = document.getElementById('snippet_list_div')
    var control_div = document.getElementById('snippet_control_div')
    resetVideo()
    
    if (list_div.classList.contains('tmp')){
        list_div.classList.remove('tmp');
        control_div.classList.add('tmp');
        
        list_div.style.display = 'none';
        control_div.style.display = 'block'
    }else{
        control_div.classList.remove('tmp');
        list_div.classList.add('tmp');
        
        control_div.style.display = 'none';
        list_div.style.display = 'block'
    }
    return 
}

// -----------------------------------------------------------------------------
// subscription form

function subText() {

    var sub_selected = document.getElementById('id_select_sub');
    
    var sub_para = document.getElementById('sub_selection_para');
    var sub_button = document.getElementById('sub_selection_button');
    
    var selected_value = sub_selected.value;
    var selected_text = sub_selected.options[sub_selected.selectedIndex].text;
    
    var sub_form = document.forms['subscription_form'];
    
    console.log(selected_text)
    
    if (selected_value != '') {
        sub_form.elements['type'].value = 'Month';
    }else{
        console.log('none...')
        sub_form.elements['type'].value = 'none';
    }
    return
}

function showCheckout(){
    var select = document.getElementById('select');
    var checkout = document.getElementById('checkout');
    select.style.display = 'none';
    checkout.style.display = 'block';
    return
}

// -----------------------------------------------------------------------------

