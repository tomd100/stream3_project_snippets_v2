
// -----------------------------------------------------------------------------
// YouTube JS

var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
    
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.

var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
    
    height: '390',
    width: '640',
    
    videoId: videoid,
    playerVars: {
        'rel': 0, 
        // 'autohide': 2, 
        'color': 'red', 
        // 'controls': 0, 
        'disablekb': 0,  
        // 'enablejsapi': 1, 
        'fs': 1,
        'hl': 'en',
        'iv_load_policy': 1,  
        'autoplay': 0,  
    },
    events: {
        // 'onReady': initialize,
        'onReady': onPlayerReady,
        // 'onStateChange': onPlayerStateChange
      }
    });
}
    

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    // event.target.stopVideo
    initialize()
    player.addEventListener('onStateChange', onPlayerStateChange);
}

function onPlayerStateChange(event){
    console.log("Player State Change")
}
// -----------------------------------------------------------------------------

var time_update_interval

function initialize(){

    // Update the controls on load
    // updateTimerDisplay();
    // updateProgressBar();

    // Clear any old interval.
    clearInterval(time_update_interval);

    // Start interval to update elapsed time display and
    // the elapsed part of the progress bar every second.
    time_update_interval = setInterval(function () {
        checkLoopStatus();
        // updateTimerDisplay();
        // updateProgressBar();
    }, 1000)
}

function checkLoopStatus() {
    var loop = document.getElementById('snippet_loop').checked;
    var start = parseFloat(document.getElementById('id_start').value);
    var end = parseFloat(document.getElementById('id_end').value);
    var current = (player.getCurrentTime());
    
    if (loop) {
        if (end <= start) {
            alert('Cannot loop: end time less than start time')
            document.getElementById('snippet_loop').checked = false
        } else if (current >= end){
            player.seekTo(start)
        }
    }
}

function updateTimerDisplay(){
    // Update current time text display.
    
    $('#current-time').text( Number((player.getCurrentTime()).toFixed(0)) );
    $('#duration').text(formatTime( player.getDuration() ));
}

function formatTime(time){
    time = Math.round(time);

    var minutes = Math.floor(time / 60),
    seconds = time - minutes * 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;

    return minutes + ":" + seconds;
}

// This function is called by initialize()
function updateProgressBar(){
    // Update the value of our progress bar accordingly.
    $('#progress-bar').val((player.getCurrentTime() / player.getDuration()) * 100);
}

// function resetProgressBar(){
//     // Reset the progress bar to the beginning
//     $('#progress-bar').val(0);
// }

$('#progress-bar').on('mouseup touchend', function (e) {

    // Calculate the new time for the video.
    // new time in seconds = total duration in seconds * ( value of range input / 100 )
    var newTime = player.getDuration() * (e.target.value / 100);

    // Skip video to new time.
    player.seekTo(newTime);

});

    
// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
    // if (event.data == YT.PlayerState.PLAYING && !done) {
    //   setTimeout(stopVideo, 4000);
      // done = true;
    // }
}    

// -----------------------------------------------------------------------------
// Functions

function resetVideo(){
    player.seekTo(0);
    player.stopVideo();
    document.getElementById('video_speed').checked = true;   
    player.setPlaybackRate(1)
    var play_btn = document.getElementById('play_btn')
    if(play_btn.textContent == 'Pause'){
        play_btn.textContent = 'Play'
        play_btn.classList.toggle('tmp');
    }
}

// function pauseVideo() {
//     var current = player.getCurrentTime()
//     player.pauseVideo();
//     player.seekTo(current);
// }

function playSnippet() {
    var start = parseFloat(document.getElementById('id_start').value)
    var current = player.getCurrentTime()
    if (start <= 0){
        start = 0.01
    }
    if (current > start){
        player.seekTo(current);
    }else{
        player.seekTo(start);
    }
    player.playVideo();
}

function jumpBack(dir){
    var seconds = parseFloat(document.getElementById('id_jump').value)
    var current, back, fwd;
    current = player.getCurrentTime();
    end = player.getDuration();
    if(dir == 0){
        if (current - seconds >= 0) {
            back = current - seconds;
            player.seekTo(back);
        } else {
            player.seekTo(0.1);
        }
    } else {
        if (current + seconds < end){
            fwd = current + seconds;
            player.seekTo(fwd);
        } else {
            player.seekTo(end);
        } 
    }
}    

function playRestart(){
    var start = parseFloat(document.getElementById('id_start').value)
    player.seekTo(start);
}

function setMarker(type) {
    // var start = parseFloat(document.getElementById('id_start').value)
    // var end = parseFloat(document.getElementById('id_end').value)
    var current = Number((player.getCurrentTime()).toFixed(1));
    var tag;
    if (type == 0){
        tag = document.getElementById('id_start')
    }else{
        tag = document.getElementById('id_end')
    }
    tag.setAttribute('value', current)
    tag.value = current
}

function setSpeed(val) {
    player.setPlaybackRate(val)
}

// -----------------------------------------------------------------------------
// Button Toggle

function togglePlay(){
    var play_btn = document.getElementById('play_btn');
    play_btn.classList.toggle("tmp");
    if(play_btn.classList.contains("tmp"))
    {
        play_btn.textContent = 'Pause'
        player.playVideo();
        // playSnippet()
    } else {
        play_btn.textContent = 'Play'
        player.pauseVideo();
    }
}


