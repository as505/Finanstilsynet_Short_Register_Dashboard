<script lang="ts">
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import { onMount } from 'svelte';

	let count:number = $state(-1)
	let nameList:string[] = $state([])

	async function Get_num_instruments(): Promise<number>{
		let url = URLLIST['root'] + URLLIST['get_num_instruments'];
		let response = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR in Get_num_instruments()"))
		
		return response;
	}

	async function Get_instrument_names(): Promise<string[]> {
		let url = URLLIST['root'] + URLLIST['get_all']
		let response:string[] = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR cannot fetch instrument list"))
		return response
	}

	onMount(async() => {
		count = await Get_num_instruments()
		let list = await Get_instrument_names()
		list.forEach(name => {
			nameList.push(name)
		});
		

	})
	
</script>

<h1>Short Sale Issuers</h1>
<div class="instrumentBoxContainer">
	{#each {length: count}, id}
		<div class="Instrument Link">
			<a href="/instrument?id={id}">{nameList[id]}</a>
		</div>
	{/each}
</div>