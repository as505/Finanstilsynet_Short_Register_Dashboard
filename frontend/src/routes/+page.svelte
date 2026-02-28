<script lang="ts">
	import { onMount } from "svelte";
	import URLLIST from '$lib/GLOBAL_URLS.json'

	let count = $state(-1)

	async function Get_num_instruments(): Promise<number>{
		let url = URLLIST['root'] + URLLIST['get_num_instruments'];
		let response = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR in Get_num_instruments()"))
		
		return response['count'];
	}

	async function buttonHandler(){
		count = await Get_num_instruments()
	}
	
</script>

<div class="instrumentBoxContainer">
	<button onclick={buttonHandler}>
		<h1> {count} </h1>
	</button>
</div>