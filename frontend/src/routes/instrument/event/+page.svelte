<script lang="ts">
	import URLLIST from '$lib/GLOBAL_URLS.json';
	import { page } from '$app/state';
	import { onMount } from 'svelte';

	let data = page.url.searchParams.get('id')
	let [id, idx] = data?.split("-");
	
	
</script>

<div class=container>
	<p>ID:{id} IDX:{idx}</p>
	
</div>

<style>
.container{
	margin-top: 2rem;
}
</style>