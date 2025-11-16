<script>
    import { draw, fly, slide } from "svelte/transition"; 
    import { onMount } from "svelte";
    import { base } from "$app/paths";

    let phase = $state(0);
    let timer = $state(120);
    let timer2 = $state(7);

    onMount(function() {
        setTimeout(function() {
            phase = 1;
        }, 100)
        setTimeout(function() {
            phase = 2;
        }, 11000)
        setTimeout(function() {
            setInterval(() => {if (timer2 > 0) {
                timer2--;
            }}, 1000)
        }, 4000)
        setTimeout(function() {
            setInterval(() => {if (timer > 0) {
                timer--;
            }}, 1000)
        }, 12000);
    })

    $effect(function() {
        if (timer <= 0) {
            window.location.href = base + "/end/player1";
        }
    })

    function player1Loose() {
        window.location.href = base + "end/player2";
    }
</script>
<style>
    h2 {
        text-align: center;
    }
    .action {
        font-size: 80px;
    }
    #actionContainer {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    #timer {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        background-color: purple;
        width: 40%;
        padding-top: 36.25%;
        border-radius: 360px;
        #timer-title {
            font-size: 200px;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-weight: 900;
        }
        @media screen and (max-width: 1000px) {
            #timer-title {
                font-size: 100px;
            }
        }
    }
    #topBar {
        position: fixed;
        top: 10px;
        right: 10px;
        left: 10px;
        padding: 10px;
        border-radius: 20px;
        background-color: pink;
        text-align: center;

    }
</style>
{#if phase >= 1}
    <br><br><br>
    <div id="actionContainer">
        <h2 transition:fly={{y:500, duration:1000}} class="action" style:font-weight="400">RUN</h2>
        <h2 transition:fly={{y:500, duration:1000, delay:1000}} class="action" style:font-weight="700">HIDE</h2>
        <h2 transition:fly={{y:500, duration:1000, delay:2000}}  class="action" style:color="rgb(255, 0, 178)" style:font-weight="900">FIGHT</h2>
        <h4 transition:slide={{y:500, duration:1000, delay:3000}}>You have {timer2} seconds until Player 2 can begin.</h4>
    </div>
{/if}
{#if phase >= 2} 
    <div transition:fly={{y:-200, duration:1000}} id="topBar">
        <h3 style:color="black">Don't get caught!</h3>
    </div>
    <div id="timer" transition:slide>
        <h1 id="timer-title">{timer}</h1>
    </div>
{/if}