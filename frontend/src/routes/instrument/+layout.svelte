<script lang="ts">
	let { children } = $props();

	
</script>

<nav>
	<a href="/">Back</a>
</nav>

{@render children()}


<style>
nav{
	display: flex;
	position: fixed;
	top: 0%;
	left: 0%;
	background-image: linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0.1));
	width: 15rem;
	height: 1.5rem;
	border-bottom-right-radius: 20rem;
}

a{
	text-align: center;
	color: white;
	padding-left: 1rem;
	margin-top: auto;
	margin-bottom: auto;
}
</style>
