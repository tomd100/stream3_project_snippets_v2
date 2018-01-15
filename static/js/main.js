// -----------------------------------------------------------------------------
// Video Functions

function setVideoSubTitle(sub_title){
    if(sub_title == 'all') {
        video_sub_title = 'all videos'
    } else if(sub_title == 'no-category') {
            video_sub_title = 'no category set'
        } else {
            video_sub_title = sub_title;
        }
    localStorage.setItem("video_sub_title", video_sub_title);
}

function videoReturn(){
    var video_url = localStorage.getItem("video_url");
    window.location.href = video_url;
    return
}

function getVideoTitle(){
    var url = document.getElementById("id_url").value
    var yt_id = verifyURL(url)
    if (yt_id == '-1') {
        alert("Please enter a valid YouTube URL")
        return
    }
    var url= 'http://www.youtube.com/watch?v=' + yt_id

    $.getJSON('https://noembed.com/embed',
        {format: 'json', url: url}, 
        function (data) {
            if(data.title == undefined) {
                alert("This url does not allow automatic title retrieval. Please enter manually.")
            } else {
                document.getElementById("id_title").value = data.title;
            }
        });
    return
}

function verifyURL(url) {
    yt_url = url.split("v=", 2);
    if(yt_url.length != 2) {
        yt_url = url.split("/youtu.be/", 2)
        if(yt_url.length != 2) {
            return -1
        }
    }
    yt_url = yt_url[1].split("?",1)
    yt_url = yt_url[0].split("&",1)
    yt_id = yt_url[0]
    return  yt_id.toString();
}


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

