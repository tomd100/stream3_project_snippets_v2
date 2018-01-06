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
    var selected_value = sub_selected.value;
    var selected_text = sub_selected.options[sub_selected.selectedIndex].text;
    
    var sub_type = document.getElementById('sub_type');
    
    var sub_para = document.getElementById('sub_selection_para');
    var sub_button = document.getElementById('sub_selection_button');
    var sub_form = document.forms['subscription_form'];
    
    
    if (selected_value == '') 
        sub_button.disabled = true;
    else {
        sub_button.disabled = false;
        sub_form.elements['description'].value = selected_text;
        if (selected_value == 1) {
            sub_form.elements['type'].value = '1';
        }else{
            sub_form.elements['type'].value = '2';
            }
        }
    return
}

function showCheckout(screen_id){
    var select = document.getElementById('select');
    var checkout = document.getElementById('checkout');
    if (screen_id == 1){
        select.style.display = 'none';
        checkout.style.display = 'block';
    } else {
        select.style.display = 'block';
        checkout.style.display = 'none';
    }
    return
}

// -----------------------------------------------------------------------------

