
<script lang="ts">
	import AggEvent from './agg_event.svelte';
	import { onMount } from 'svelte';
	import URLLIST from '$lib/GLOBAL_URLS.json';

	let {self_id} = $props();
	let is_in = $state("ISIN:");
	let issuer = $state("Issuer:");
	let event_count = $state(-1);
	let events = $state([])

	// From the backend we can fetch the instrument data that this component is assigned to display
	async function fetch_self(id:number): Promise<JSON>{
		let url = URLLIST['root'] + URLLIST['get_id'] + `${id}`
		let data = await fetch(url)
		.then(d => d.json())
		.catch(e => console.error("ERROR in instrument -> fetch_self()"))
		
		return data
	}

	onMount(() => {
		fetch_self(self_id)
			.then(d => {
				is_in = d[Object.keys(d)[0]]
				issuer = d[Object.keys(d)[1]]
				let json_events = d[Object.keys(d)[2]]
				event_count = json_events.length;
				json_events.forEach(element => {
					events.push(element)
				});
			})
			.catch(d => "error")
		
	})

</script>

<div>
	<h1>
		{self_id}
	</h1>
	<p>
		ISIN: {is_in}
	</p>
	<p>
		Issuer: {issuer}
	</p>
	<details title="Short Events">
		<summary>Events</summary>
			<h3>{event_count} EVENTS</h3>
			{#each {length : event_count}, id}
				<p>Date: {events[id]['date']}<br>Short %: {events[id]['shortPercent']}<br>Shares: {events[id]['shares']} </p>
				<details title="Underlying Positions">
					<summary>Positions</summary>
				</details>
			{/each}
		</details>
</div>