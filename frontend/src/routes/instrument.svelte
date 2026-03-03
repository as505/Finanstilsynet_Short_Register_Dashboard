
<script lang="ts">
	import { onMount } from 'svelte';
	import URLLIST from '$lib/GLOBAL_URLS.json';

	let {self_id} = $props();
	let is_in = $state("ISIN:");
	let issuer = $state("Issuer:");

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
</div>