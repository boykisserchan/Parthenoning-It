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
    h1 {
        text-align: center;
    }
    #container {
        background-color: pink;
        padding: 20px;
        border-radius: 20px;
    }
    #container button {
        display: block;
        margin: 0 auto;
    }
</style>
{#if toggle}
    <br><br><br>
    <div id="actionContainer">
        <h1 transition:fly={{y:500, duration:1000}} class="action" style:font-weight="900">DETATCH THE USB DRIVE</h1>
        <br>
        <div transition:slide={{y:500, duration:1000, delay:1000}} id="container">
            <h2 ><button onclick={() => {window.location.href = base + "/timer"}}>Continue</button></h2>
        </div>
    </div>
{/if}