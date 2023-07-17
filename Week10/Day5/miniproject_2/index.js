const Parser = require('rss-parser');
const parser = new Parser(); //inst of class

async function run() {
    const feed = await parser.parseURL('https://thefactfile.org/feed/');
    
    feed.items.forEach(item => {
      
      console.log(item.title + ':' + item.link)
    });
}

run();