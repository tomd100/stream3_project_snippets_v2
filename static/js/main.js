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
// Video and Snippet list toggles


function changeListItems(to_list, list_num) {
    var default_list = 'default_list' + list_num;
    var from_list = getCurrentList(list_num);
    var to_list = to_list + list_num;
    
    if (from_list != default_list && from_list == to_list) {
        to_list = default_list;
    }
    
    if (to_list != default_list) {
        var to_menu_element = document.getElementById(to_list + '_menu')
        var to_menu_text = to_menu_element.innerHTML
        to_menu_element.innerHTML = 'Un ' + to_menu_text;
    } 
    
    if (from_list != default_list) {
        var from_menu_element = document.getElementById(from_list + '_menu')
        var from_menu_text = from_menu_element.innerHTML
        from_menu_element.innerHTML = from_menu_text.substring(3, from_menu_text.length)
    } 
    
    from_list_items = document.getElementsByClassName(from_list)
    to_list_items = document.getElementsByClassName(to_list)
    
    for (var i = 0; i < from_list_items.length; i ++) {
        from_list_items[i].style.display = 'none';
        from_list_items[i].classList.remove("tmp");
        
        to_list_items[i].style.display = 'block';
        to_list_items[i].classList.add("tmp");
    
    }
}

function getCurrentList(list_num) {
    if (document.getElementsByClassName('default_list' + list_num)[0].classList.contains('tmp')){
        return 'default_list' + list_num;
    } else if (document.getElementsByClassName('edit_list' + list_num)[0].classList.contains('tmp')) {
        return 'edit_list' + list_num;
    } else {
        return 'delete_list' + list_num;
    }
}


// -----------------------------------------------------------------------------
// Snippet Controls

function controlToggle(){
    
    var list_div = document.getElementById('snippet_list_div')
    var control_div = document.getElementById('snippet_control_div')
    
    // this can be replaced with a toggle class method
    if (list_div.classList.contains('tmp')){
        list_div.classList.remove('tmp');
        control_div.classList.add('tmp');
        document.getElementById("play_snippet").disabled=true;
        document.getElementById("edit_snippet").disabled=true;
        
        list_div.style.display = 'none';
        control_div.style.display = 'block'
    }else{
        control_div.classList.remove('tmp');
        list_div.classList.add('tmp');
        
        control_div.style.display = 'none';
        list_div.style.display = 'block'
        document.getElementById("play_snippet").disabled=false;
        document.getElementById("edit_snippet").disabled=false;
    }
    return 
}

// -----------------------------------------------------------------------------
// subscription form

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

