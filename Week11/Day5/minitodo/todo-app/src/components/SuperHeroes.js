import React from "react";
import {useState, useRef, useEffect } from "react";
import data from "../data/superheroes.json";
import '../App.css';

const prevId = [];

const SuperHeroes = (props) => {
    const [superHeroesInfo, setSuperHeroesInfo] = useState(data.superheroes);

    const [score, setScore] = useState(0);
    const [topScore, setTopScore] = useState(0);
    // const [prevId, setPrevId] = useState(-1);
    const [win, setWin] = useState(false);
    const [lose, setLose] = useState(false)
    const [lastScore, setLastScore] = useState(0)
    

    const shuffleArray = (array) => {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    const handleCardClick = (event) => {
        setLose(false);
        shuffleArray(superHeroesInfo);
        setSuperHeroesInfo(superHeroesInfo);
   
        const id = +event.currentTarget.getAttribute('hero-id');
        
        
        
        if (event.button === 0 & event.detail>=1) {
            console.log("card id:", id);
            // check prev
         
            console.log("next:", prevId, id, prevId != id);  
            if (!prevId.includes(id)) {
                setScore(score + 1);
                prevId.push(id);
                console.log(prevId);
                      
                if (score >= 11) {
                    console.log("You win!");
                    setWin(true);
                }

            } 
            else if (prevId.includes(id)) {
                prevId.length = 0;
                if (topScore < score) {setTopScore(score)};
                setLastScore(score);
                setLose(true);
                setScore(0);
                

            }
 

        }
    }



    return(
        <div>
            <div className="header-box">
                <h2>Super Heroes memory game</h2>
                <div className="score">
                    <p>Score: {score}</p>
                    <p>Top Score: {topScore}</p>
                </div>
            </div>
            <div className="instruction">
                <p>Get points by clicking on an image but don't click on any more than once!</p>
            </div>
            
            { 
            win ?
                    <div className="win" onClick={() => setWin(false)}>
                        <p>You win!!!</p>
                    </div>
                : <></>
            }
            { 
            lose ?
                    <div className="lose" onClick={() => setLose(false)}>
                        <p>You lose with score: {lastScore}!!!</p>
                    </div>
                : <></>
            }
            <div className="card-box">
           
            {   
                superHeroesInfo.map((item)=>{
                    return(
                        <div hero-id={item.id} key={item.id} onClick={handleCardClick} className="hero">
                            <img src={item.image} alt={item.name} className="heroImage"/>
                            <p><span>Name:</span> {item.name}</p>
                            <p><span>Occupation:</span>{item.occupation}</p>
                        </div>
                    )
                })
               
            }
            </div>
            
        </div>
       
    )
}

export default SuperHeroes;