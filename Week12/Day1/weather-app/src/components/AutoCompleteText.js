import React, {useState,useEffect,useContext} from 'react';
import {AppContext} from '../App';
import './AutoCompleteText.css'

const BASE_URL = process.env.REACT_APP_BASE_URL;
const API_KEY = process.env.REACT_APP_API_KEY;

const AutoCompleteText = (props) => {
  const [suggestions, setSuggestions] = useState([]);
  const [hint,setHint] = useState('');

  const {setCity,setCityKey,setCountry} = useContext(AppContext);

  const getSuggestions = (e) => {
    setHint(e)
    fetch(`${BASE_URL}/locations/v1/cities/autocomplete?apikey=${API_KEY}&q=${e}`)
    .then(res=>res.json())
    .then(data=>{
      console.log(data);
      setSuggestions(data)
    })
    .catch(e=> {
      console.log(e);
    })
  }

  return(
    <div className="AutoCompleteText">
      <input type="text"
        onChange={(e)=>getSuggestions(e.target.value)}
      />
      {/*<button onClick={()=>getSuggestions()}>click</button>*/}
      <ul>
      {
        suggestions.map(item => {
          return (
            <li onClick={()=>{
                  setCityKey(item.Key);
                  setCity(item.LocalizedName);
                  setCountry(item.Country.LocalizedName)
                  setSuggestions([]);
                  setHint(item.LocalizedName)
                }} key={item.Key}>
              {item.LocalizedName}, {item.Country.LocalizedName}
            </li>
          )
        })
      }
      </ul>
    </div>
  )
}
export default AutoCompleteText;
