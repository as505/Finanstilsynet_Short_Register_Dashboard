<script lang="ts">
	import { onMount } from "svelte";

	let {events} = $props();
	let event_count = $state(-1)

	onMount(() => {
		let jsonEvents:JSON = events[Object.keys(events)[0]];
		console.log(jsonEvents)
		event_count = Object.keys(jsonEvents).length;
	})
</script>

<div>
	{#each {length: event_count}}
		<p>A</p>
	{/each}
</div>