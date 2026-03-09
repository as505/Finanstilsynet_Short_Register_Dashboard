<script lang="ts">
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import Instrument from "./instrument.svelte";
	import { onMount } from 'svelte';

	let count = $state(-1)

	async function Get_num_instruments(): Promise<number>{
		let url = URLLIST['root'] + URLLIST['get_num_instruments'];
		let response = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR in Get_num_instruments()"))
		
		return response;
	}

	onMount(async() => {
		count = await Get_num_instruments()
	})
	
</script>

<div class="instrumentBoxContainer">
	{#each {length: count}, id}
		<div class="Instrument Link">
			<a href="/instrument?id={id}">{id}</a>
		</div>
	{/each}
</div>