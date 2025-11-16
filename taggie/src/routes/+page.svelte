<script>
    import { draw, fly, slide } from "svelte/transition"; 
    import { onMount } from "svelte";
    import { base } from "$app/paths";

    let toggle = $state(false);
    let toggle2 = $state(false);

    import { page } from "$app/stores";

    onMount(function() {
        setTimeout(function() {
            toggle = true;
        }, 100)
        setTimeout(function() {
            toggle2 = true;
        }, 4500)
    })

    function startGame() {
        event.preventDefault(); // CRITICAL FUNCTION
        // startGame() will do all required processes to start the game and will then proceed to the timer
        window.location.href = base + "/detach";
    }
</script>
<style>
    #title {
        font-weight: 800;
        margin-top: 40px;
        user-select: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
    }
    h1, h2, h3 {
        text-align: center;
    }
    #player span {
        color: rgb(255, 255, 255);
        padding: 10px;
        border-radius: 20px;
        background-color: rgb(120, 68, 145);
        user-select: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
    }
    #gameController {
        display: block;
        margin: 0 auto;
        width: 200px;  
        height: 200px; 
    }
    #overlayPanel {
        position: fixed;
        top: -20px;
        bottom: -20px;
        left: 0px;
        right: 0px;
        background-color: rgb(146, 74, 86);
        background-image: repeating-linear-gradient(45deg, rgba(255,255,255,0.03) 0 10px,rgba(0,0,0,0.03) 10px 20px);
    }
    .rule {
        text-align: center;
        margin-bottom: 40px;
        div {
            background-color: rgb(99, 44, 74);
            padding: 10px;
            border-radius: 20px;
            max-width: 70%;
            margin-left: 15%;
            margin-right: 15%;
            box-shadow: 0px 7px 5px rgb(54, 13, 41);

            span.player {
                color: rgb(255, 93, 188);
            }
        }
    }
    #playButton {
        font-size: 30px;
    }
</style>
{#if toggle}
    <h1 transition:slide={{duration:1000}} id="title"><span style:color="rgb(255, 179, 217)">TAGGIE</span> THE GAME</h1>
    <br>
    <h2 transition:fly={{delay:500, y:200, duration:1000}} id="player"><span >Initializing Round</span></h2>
    <br>
<!-- License: CC Attribution. Made by Shannon E. Thomas: https://dribbble.com/shannonethomas -->
    <svg id="gameController" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
	    width="800px" height="800px" stroke="white"
        stroke-width="0.5" viewBox="-5 -5 40 40" xml:space="preserve">
        <style type="text/css">
            .stone_een{fill:none;}
        </style>
        <path transition:draw={{delay:2500, duration:2000}} class="stone_een" d="M26,17c0,0.551-0.449,1-1,1s-1-0.449-1-1s0.449-1,1-1S26,16.449,26,17z M20,17c-0.551,0-1,0.449-1,1
            s0.449,1,1,1s1-0.449,1-1S20.551,17,20,17z M9,12H7v2H5v2h2v2h2v-2h2v-2H9V12z M20,12c-0.551,0-1,0.449-1,1s0.449,1,1,1s1-0.449,1-1
            S20.551,12,20,12z M25,11c-0.551,0-1,0.449-1,1s0.449,1,1,1s1-0.449,1-1S25.551,11,25,11z M32,20c0,3.86-3.14,7-7,7
            c-2.714,0-5.17-1.581-6.319-4h-5.363C12.17,25.419,9.714,27,7,27c-3.86,0-7-3.14-7-7c0-0.521,0.063-1.058,0.188-1.59l2.128-9.259
            C3.124,6.668,5.408,5,8,5c1.713,0,3.308,0.723,4.449,2h7.102C20.692,5.723,22.287,5,24,5c2.592,0,4.876,1.668,5.684,4.151
            l2.127,9.255C31.937,18.942,32,19.479,32,20z M12,14c0-0.552-0.448-1-1-1h-1v-1c0-0.552-0.448-1-1-1H7c-0.552,0-1,0.448-1,1v1H5
            c-0.552,0-1,0.448-1,1v2c0,0.552,0.448,1,1,1h1v1c0,0.552,0.448,1,1,1h2c0.552,0,1-0.448,1-1v-1h1c0.552,0,1-0.448,1-1V14z M22,18
            c0-1.105-0.895-2-2-2s-2,0.895-2,2c0,1.105,0.895,2,2,2S22,19.105,22,18z M22,13c0-1.105-0.895-2-2-2s-2,0.895-2,2
            c0,1.105,0.895,2,2,2S22,14.105,22,13z M27,17c0-1.105-0.895-2-2-2s-2,0.895-2,2c0,1.105,0.895,2,2,2S27,18.105,27,17z M27,12
            c0-1.105-0.895-2-2-2s-2,0.895-2,2c0,1.105,0.895,2,2,2S27,13.105,27,12z"/>
    </svg>
{/if}
{#if toggle2}
    <div transition:fly={{y:2000, duration:1000}} id="overlayPanel">
        <br><br><br><br>
        <h1 style:font-weight=900>RULES</h1>
        <h3>(Do not detach the USB Stick)</h3>
        <br><br>
        <h2 class="rule"><div transition:fly={{duration:500, delay:1000}}>Taggie is a hide and seek/tag game involving two players.</div></h2>
        <h2 class="rule"><div transition:fly={{duration:500, delay:3000}}><span class="player">Player 1</span> uses this computer; <span class="player">Player 2</span> will use the USB stick.</div></h2>
        <h2 class="rule"><div transition:fly={{duration:500, delay:5000}}><span class="player">Player 2</span> must attempt to insert the USB stick into the port of the computer, and will have 2 minutes to do so.</div></h2>
        <h2 class="rule"><div transition:fly={{duration:500, delay:8000}}><span class="player">Player 1</span> must attempt to either hide the computer from <span class="player">Player 2</span> or run away from <span class="player">Player 2</span> with the computer.</div></h2>
        <h2 class="rule"><div transition:fly={{duration:500, delay:11000}}><span class="player">Player 1</span> cannot try to cover the port to prevent <span class="player">Player 2</span> from winning. <span class="player">Player 1</span> can move the laptop itself into a position that inhibits access.</div></h2>

        <br>
        <h3 id="playButton"><button onclick={() => {startGame();}} transition:slide={{duration:500, delay:13000}}>We understand the rules</button></h3>
    </div>
{/if}