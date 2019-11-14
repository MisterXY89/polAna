

const mercury = require('@postlight/mercury-parser');

let urls = [
		"https://www.breitbart.com/clips/2019/11/05/espaillat-sondlands-revised-testimony-is-a-smoking-gun/",
		"https://www.nytimes.com/2019/11/05/us/politics/impeachment-trump.html"
		];


urls.forEach(url => {
	mercury.parse(url).then(result => {
		console.log(result);
		console.log(result["title"]);
	});
});