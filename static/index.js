const switcheroo = async () =>
	await fetch('/api')
		.then(r => r.json())
		.then(d => {
			document.getElementById('not-static').innerHTML = d.content;
		});

setTimeout(switcheroo, 3000);

export default {};
