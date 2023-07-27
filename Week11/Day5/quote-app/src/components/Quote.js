import React from "react";
import {useState, useRef, useEffect } from "react";
import quotes from "../data/QuotesDatabase.js";
import '../App.css';

const randomFromArr = (arr, prevIndex) => {
    let index = -1;
    do {
        index = Math.floor(Math.random()*(arr.length));
    } while (index === prevIndex);
    const val = arr[index]
    
    return {val, index}
}

// const data = JSON.parse(quotes);

let prevQuoteIndex = -1;
let prevColorIndex = 0;

const colors = ["blue", "red", "yellow", "green","lightgrey"];

const Quote = () => {
    const newQuoteInfo = randomFromArr(quotes, prevQuoteIndex);
    prevQuoteIndex = newQuoteInfo.index;

    const [newQuote, setNewQuote] = useState(newQuoteInfo.val);
    const [colorText, setTextColor] = useState("white");
   


    const handleNewQuote = () => {
        const newQuoteInfo = randomFromArr(quotes, prevQuoteIndex);
        setNewQuote(newQuoteInfo.val);
        prevQuoteIndex = newQuoteInfo.index;
    
        
    }
   
    useEffect(() => {
        const colorInfo = randomFromArr(colors, prevColorIndex);
        // setNewQuote(color.val);
        const color = colorInfo.val;
        prevColorIndex = colorInfo.index;
        document.body.style.backgroundColor = color;
        setTextColor(color);

    },[newQuote]);
 
    return (
        <div id ="quote-box" className="Quote"  style={{ color: colorText }}>
            <h1>{newQuote.quote}</h1>
            <p>{newQuote.author}</p>
            <button onClick={handleNewQuote}>New quote</button>
        </div>
    )
}

export default Quote;