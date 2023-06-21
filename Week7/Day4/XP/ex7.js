// XP
// Exercise 7 : My Book List
// Instructions

// 2. In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).
// 3. Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

const allBooks = [{
        'title':`The Best of America's Test Kitchen 2019`,
        'author':'Test Kitchen',
        'image':'http://books.google.com/books/content?id=nK1KEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api',
        'alreadyRead': true,
     },
     {
        'title':'NYC Angels: Making the Surgeon Smile',
        'author':'Lynne Marshall',
        'image':'http://books.google.com/books/content?id=aXqH7BPHTwoC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api',
        'alreadyRead': false,
    }]

    // 4. Requirements : All the instructions below need to be coded in the js file:
    // Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
const container = document.body.firstElementChild;

  // For each book :
    // You have to display the book’s title and the book’s author.
    // Example: HarryPotter written by JKRolling.
    // The width of the image has to be set to 100px.
for (let book of allBooks) {
    const newDiv = document.createElement("div");
    const text = document.createTextNode(`${book['title']} written by ${book['author']}`);
    const newImage = document.createElement("img");
    newImage.setAttribute("src",`${book['image']}`);
    newImage.setAttribute("alt",`book ${book['title']}`);
    newImage.style.width = "100px";
    newDiv.style.display = "flex";
    newDiv.appendChild(text);
    newDiv.appendChild(newImage);
    container.appendChild(newDiv);

// If the book is already read. Set the color of the book’s details to red.
    if (book['alreadyRead']) {
        newDiv.style.color = "red";
    }
   
}
  
