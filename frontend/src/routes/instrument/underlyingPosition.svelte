<script lang="ts">
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import { onMount } from "svelte";

	type Props = {i_id:number, e_idx:number, up_id:number}
	let {i_id, e_idx, up_id} : Props = $props();

	let date = $state('')
	let shortPercent = $state('')
	let shares = $state('')
	let positionHolder = $state('')


	async function fetchSelf(){
		let url = URLLIST['root'] + URLLIST['get_instrument'] + JSON.stringify(i_id) + '/' + JSON.stringify(e_idx) + "/" + JSON.stringify(up_id);
		let result = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR can't fetch position count"))
		
		date = result['date']
		shortPercent = result['shortPercent']
		shares = result['shares']
		positionHolder = result['positionHolder']
	}

	onMount(async() => fetchSelf())


</script>

<div>
	<p>{date}</p>
	<p>{shortPercent}</p>
	<p>{shares}</p>
	<p>{positionHolder}</p>
</div>