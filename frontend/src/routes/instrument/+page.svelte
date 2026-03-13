<script lang="ts">
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import UnderlyingPosition from './underlyingPosition.svelte';
	import { page } from '$app/state';
	import { onMount } from 'svelte';



	let id:number = parseInt(page.url.searchParams.get('id'))
	let eventIDX = $state(0)
	
	let is_in = $state("Null")
	let issuer_name = $state("Null")
	let num_events = $state(-1)
	let eventList = $state([])

	


	async function fetch_instrument_data(){
		let url = URLLIST['root'] + URLLIST['get_instrument'] + id;
		let response = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR in Get_num_instruments()"))
		
		return response;
	}

	onMount(async () => {
		fetch_instrument_data().then((d) =>
			(
			is_in = d['isin'],
			issuer_name = d['issuerName'],
			num_events = d['events'].length,
			d['events'].forEach(e => {
				eventList.push(e)
			})
			)
		)
	})

	function handle_load_event(idx:number){
		eventIDX = idx
		console.log(eventIDX)
	}

</script>


<div class="pageLayout">
	<div class="header">
		<h1>{issuer_name}</h1>
		<h3>{is_in}</h3>
	</div>

	<div class="eventList">
		<h2>Short events</h2>
		{#each {length: num_events}, idx}
		<div>
			<!-- <a href="/instrument/event/?id={id}-{idx}">{eventList[idx]}</a> -->
			<button onclick={() => handle_load_event(idx)}>{eventList[idx]['date']}</button>
		</div>
		{/each}
	</div>

	<div class="eventInspectorPanel">
		<h2>Info</h2>
		{#key eventIDX}
		<UnderlyingPosition i_id={id} e_idx={eventIDX}/>
		{/key}
	</div>
</div>

<style>
.pageLayout{
	display: grid;
	grid-template-columns: 1fr 2fr;
	
}

.header{
	grid-column: 1;
}

.eventList{
	grid-column: 1;
}

.eventInspectorPanel{
	grid-column: 2;
}

</style>
