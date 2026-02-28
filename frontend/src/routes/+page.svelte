<script lang="ts">
	import { onMount } from "svelte";
	onMount(() =>{
		var response = fetch("http://localhost:8000/")
	})

	async function Test(){
		// The data gets returned as an array with length 1,
		// so we need to 
		let data = await GetInstruments();
		console.log(data);
		
	}

	async function GetInstruments(){
		var url = "http://localhost:8000/instruments";
		try {
			let response = await fetch(url);
			if (!response.ok) {
				throw new Error(`Response status: ${response.status}`);
			}
			let result = response.json();
			return result;

		} catch {
			console.error("API Error fetching instrument data in GetInstruments()");
 		}
	}
	
</script>

<div id="dataContainer">

</div>

<button onclick={Test}>
Load Data
</button>