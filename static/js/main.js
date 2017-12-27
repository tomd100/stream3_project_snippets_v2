// -----------------------------------------------------------------------------
// Snippet Controls


function snippetControl(){
    // document.getElementById('snippet_list_div').style.display = 'none';  
    // document.getElementById('snippet_control_div').style.display = 'block'; 
    
    console.log(document.getElementById('snippet_list_div').value)
    
    // $("#snippet_list_div").change(function () {
    //   var username = $(this).val();

    //   $.ajax({
    //     url: '/ajax/validate_username/',
    //     data: {
    //       'username': username
    //     },
    //     dataType: 'json',
    //     success: function (data) {
    //       if (data.is_taken) {
    //         alert("A user with this username already exists.");
    //       }
    //     }
    //   });

    // });    
    
    return false
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

