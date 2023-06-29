// // Exercises XP
// Daily Challenge : Creating Objects

// Instructions
// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)

class Video {
  constructor (title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }
// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
  watch() {
    const sentence = `${this.uploader} watched all ${this.time} of ${this.title}`;
    console.log(sentence);
  }

}

// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”

// Instantiate a new Video instance and call the watch() method.
const record1 = new Video("Good one", "Albert", 1000);
record1.watch()

// Instantiate a second Video instance with different values.
const record2 = new Video("Long video", "Dan", 10000);
record2.watch()

// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
// Think of the best data structure to save this information within the array.
// Bonus: Loop through the array to instantiate those instances.
const dataForVideo = [
  {title: "Hello", uploader: "Name1", time: 1000},
  {title: "Books", uploader: "Name2", time: 2000},
  {title: "Animals", uploader: "Name3", time: 3000},
  {title: "Birds", uploader: "Name4", time: 4000},
  {title: "Sea", uploader: "Name5", time: 5000}
];

const arr = []
dataForVideo.forEach((element, index) => {
  arr.push((new Video(element["title"], element["uploader"], element["time"])))
  arr[arr.length-1].watch();
  return arr
 
})

console.log(arr)
