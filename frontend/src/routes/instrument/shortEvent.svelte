<script lang="ts">
	import UnderlyingPosition from './underlyingPosition.svelte';
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import { onMount } from "svelte";
	

	type Props = {i_id:number, e_idx:number}
	let {i_id, e_idx} : Props = $props();

	let positionDate = $state('')
	let positionShortPercent = $state('')
	let positionShares = $state('')
	let positionsCount = $state(-1)


	async function fetchSelf(){
		let url = URLLIST['root'] + URLLIST['get_instrument'] + JSON.stringify(i_id) + '/' + JSON.stringify(e_idx);
		let data = await fetch(url)
			.then(d => d.json())
			.catch(e => console.error("ERROR in underlyingPosition fetchSelf()"))
		
		positionDate = data['date'];
		positionShortPercent = data['shortPercent'];
		positionShares = data['shares'];
		
		return data;
	}

	async function fetchPositionsCount(){
		let url = URLLIST['root'] + URLLIST['get_instrument'] + JSON.stringify(i_id) + '/' + JSON.stringify(e_idx) + "/positionCount";
		let result = await fetch(url)
			.then(d => d.text())
			.then(s => parseInt(s))
			.catch(e => console.error("ERROR can't fetch position count"))
		
		positionsCount = result
		
	}

	onMount(async() =>{
		await fetchSelf();
		await fetchPositionsCount();
	})

</script>


<div class="container">
	<p>{positionDate}</p>
	<p>{positionShortPercent}</p>
	<p>{positionShares}</p>
	{#each {length: positionsCount}, idx}
		<UnderlyingPosition i_id={i_id} e_idx={e_idx} up_id={idx}/>
	{/each}
</div>	
