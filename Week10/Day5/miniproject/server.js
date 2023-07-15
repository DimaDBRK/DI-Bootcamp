const Parser = require('rss-parser');
const parser = new Parser(); //inst of class

const url = 'https://thefactfile.org/feed/';

const express = require("express");
const ejs = require("ejs");

const bodyParser = require('body-parser')



const  app = express();



// create application/json parser
const jsonParser = bodyParser.json()

// create application/x-www-form-urlencoded parser
const urlencodedParser = bodyParser.urlencoded({ extended: false })

//set template engine
app.set('view engine', 'ejs');
app.use(express.json());


app.use('/', express.static(__dirname + "/public"));

app.get('/all', sendFeed);
app.get('/', renderAll);
app.get('/search', renderSearch);
app.post('/search/title', jsonParser, searchFeedTitle);
app.post('/search/category', jsonParser, searchFeedCategory);


app.listen(process.env.PORT || 3001, ()=> {
    console.log(`run in ${process.env.PORT || 3001}`);
})
let items = [];
let categories = [];
populateItems();

// for /
async function sendFeed(req, res) {
    const feed = await parser.parseURL(url);
    const title = feed.title;
    const description = feed.description;
    const items = feed.items;
    res.send({title, description, items})
}

// for search

async function populateItems() {
    const feed = await parser.parseURL(url);
    items = feed.items;
}

function renderAll(req, res) {
    res.render("index", {items})
}

function renderSearch(req, res) {
    res.render("search")
}

function searchFeedTitle(req, res) {
    const body = req.body;
    
    const title = body.title;
    console.log(title);
    res.render("search", {items: getFeedContainedTitle(title)})
}

function getFeedContainedTitle(title) {
    console.log("search for title")
    return items.filter((item) => item.title.toLowerCase().includes(title.toLowerCase()))
}


function searchFeedCategory(req, res) {
    const body = req.body;
    
    const category = body.category;
    console.log(category);
    console.log(getFeedContainedCategory(category));
    res.render("search", {items: getFeedContainedCategory(category)})
}

function getFeedContainedCategory(category) {
   
    return items.filter((item) => {
        return item.categories.some((categ) => categ.toLowerCase().includes(category.toLowerCase()))
    });
}

// //templates
// app.get('/', (req, res)=>{
//     let user = {
//         firstName: "Mary",
//         lastName: "Dada",
//     }
//     let login = false;

//     let students = {
//         stu1: 'mary',
//         stu2: 'kelly',
//         stu3: 'jordan',
//     }

//     let  arr = [
//         {id:1, name:"iPhone",price: 100},
//         {id:2, name:"aaa",price: 1100},
//         {id:3, name:"bbb",price: 1200},

//     ]
//     //send object to file
//     res.render('index', {
//         user,
//         login,
//         students,
//         arr
// }) //go to folder View  and looks. /partial/...-> in view file
//  })
// // default folder - views, all files ejs

// //add files
// app.get('/home', (req, res)=>{
//     res.render('home')
// })

// app.get('/about', (req, res)=>{
//     res.render('about')
// })
