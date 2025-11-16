<script>
    import { draw, fly, slide } from "svelte/transition"; 
    import { onMount } from "svelte";
    import { base } from "$app/paths";

    let toggle = $state(false);


    onMount(function() {
        setTimeout(function() {
            toggle = true;
        }, 100)
    })
</script>
<style>
    h1, h2, h4 {
        text-align: center;
    }
</style>
{#if toggle}
    <br><br><br>
    <div id="actionContainer">
        <h1 transition:fly={{y:500, duration:1000}} class="action" style:font-weight="900">PLAYER 2 WINS</h1>
        <h2 transition:fly={{y:500, duration:1000, delay:1000}} class="action" style:font-weight="700">GAME OVER</h2>
        <h4 transition:slide={{duration:1000, delay:2000}}>Well done!</h4>
    </div>
{/if}