<script lang="ts">
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import { onMount } from "svelte";
	

	type Props = {e_id:number, p_idx:number}
	let {e_id=$bindable(), p_idx=$bindable()} : Props = $props();

	let positionDate = $state('')
	let positionShortPercent = $state('')
	let positionShares = $state('')
	let positionHolder = $state('')


	async function fetchSelf(){
		let url = URLLIST['root'] + URLLIST['get_instrument'] + JSON.stringify(e_id) + '/' + JSON.stringify(p_idx);

		console.log(url, e_id, p_idx)
		let data = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR in underlyingPosition fetchSelf()"))
		
		positionDate = data['date'];
		positionShortPercent = data['shortPercent'];
		positionShares = data['shares'];
		positionHolder = data['positionHolder'];

		return data;
	
	}

	onMount(async() =>{
		await fetchSelf();
	})

</script>

<div class="container">
	<h1>TEXT</h1>
	<p>{positionDate}</p>
	<p>{positionShortPercent}</p>
	<p>{positionShares}</p>
	<p>{positionHolder}</p>
	<p>ID {e_id}  IDX {p_idx}</p>
</div>