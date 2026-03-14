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

<div class="positionContainer">
	<div class="numberRing"></div>
	<p class="number">{up_id + 1}</p>
	<p>{date}</p>
	<p>{shortPercent}</p>
	<p>{shares}</p>
	<p>{positionHolder}</p>
</div>

<style>
	
.positionContainer{
	background-color: whitesmoke;
	display: grid;
	grid-template-columns: 3fr 0.5fr;
	border-radius: 0.2rem;
	border-style: solid;
	border-width: 0.1rem;
	padding: 1rem;
	width: 33%;
	aspect-ratio: 2;
	box-shadow: 0.5rem 0.2rem 0.05rem grey;
}

.numberRing{
	grid-column: 2;
	grid-row: 1;
	height: 50%;
	align-self: center;
	justify-self: center;
	aspect-ratio: 1;
	background-color: orange;
	border-style: solid;
	border-radius: 1000rem;
	border-width: 0.1rem;
}

.number{
	grid-column: 2;
	grid-row: 1;
	align-self: center;
	justify-self: center;
	color: whitesmoke;
}

p{
	grid-column: 1;
}

</style>