<script lang="ts">
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import { page } from '$app/state';
	import { onMount } from 'svelte';

	let id = page.url.searchParams.get('id')
	
	let is_in = $state("Null")
	let issuer_name = $state("Null")

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
			issuer_name = d['issuerName']
			)
		)
	})
</script>


<div>
	<h1>{issuer_name}</h1>
	<h2>{is_in}</h2>
</div>

