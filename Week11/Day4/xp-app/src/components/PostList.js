import React from "react";
import posts from "./../data/data.json"

const  PostList = () => {
    // posts.map((item) => {
    //     console.log(item.title);
    //     console.log(item.content);
    // })
    // console.log(posts);
    return (
     <div>
        <h2>This is a title:</h2>
     {
       posts.map((item, index) => {
        return (
        <div  key={item.id}>
          <h2> {item.title} </h2>
          <p> {item.content} </p>
        </div>
         )
       }) 
        }

    </div>
    );
}

export default PostList;