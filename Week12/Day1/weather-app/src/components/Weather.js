import React from "react";
import {useState, useRef, useEffect } from "react";
import apiKey from "../apikey.js"

console.log("apikey=>", apiKey);

const Weather = (props) => {
    const [weatherInfo, setWeather] = useState(""); //or null?
    const [temperature, setTemperature] = useState(""); //or null?
    const [forecastInfoArr, setForecast] = useState([]);
    const [favoritesArr, setFavorites] = useState([]);
    const [newCity, setNewCity] = useState("");

    const [city, setCity] = useState({
                                            key: "215854",
                                            city: "Tel Aviv"
                                        }
                                        );
     
    // function to serialise an object of keys and values into a query string
    function objToQueryString(obj) {
        const keyValuePairs = [];
        for (const key in obj) {
          keyValuePairs.push(encodeURIComponent(key) + '=' + encodeURIComponent(obj[key]));
        }
        return keyValuePairs.join('&');
      }
   
  


      // get ifo for city
      const cityInfo = async (cityName) => {
        console.log("funct cityInfo");
        if (cityName.length > 3) {
            
            const cityParams = {
                apikey: apiKey,
                q: cityName
            }
            const requestString = objToQueryString(cityParams);
            const linkCity = `http://dataservice.accuweather.com/locations/v1/cities/autocomplete`;
            console.log("URL=>",`${linkCity}?${requestString}`)
            try {
                
                const res = await fetch(`${linkCity}?${requestString}`);
                console.log("resp=>", res);
                if (res.ok) {
                const data = await res.json();
                console.log("data resp=>", data);
                setCity({
                        key: data[0].Key, 
                        city: data[0].LocalizedName
                        });
                
                console.log("city: ", city);
                setNewCity("");
                } else {
                    console.log("Problem with fetch")
                }
            } catch(error) {
                console.log(error)
            }  
        }
    }
 

  

   
    // const forecast = async (lat, lon ) => {
    //     const forecastParams = { 
    //         lat: lat,
    //         lon: lon,
    //         appid: apiKey,
    //         units: 'metric' 
    //         }
        
    //     const requestString = objToQueryString(forecastParams);
    //     try {
    //         const res = await fetch(linkMain +"forecast?"+ requestString);
    //         const data = await res.json();
    //         console.log(data);
    //         if (data.cod == 200) {
    //             forecastInfo = data['list'];
    //             console.log("forecastInfo=>", forecastInfo);
    //         }
            
    //         // setWeather(data);
    //     } catch (e) {
    //         console.log(e);
    //     }

    // }

    // const Info = async (city) => {
    //     const weatherParams = { 
    //         q: city,
    //         appid: apiKey,
    //         units: 'metric' 
    //     }

    //     const requestString = objToQueryString(weatherParams);

    //     try {
    //         const res = await fetch(linkMain +"weather?"+ requestString);
    //         const data = await res.json();
    //         console.log(data);
    //         if (data.cod === 200) {
    //             weatherInCity.temperature = data["main"]["temp"]
    //             weatherInCity.humidity = data["main"]["humidity"]
    //             weatherInCity.wind_speed = data["wind"]["speed"]
    //             weatherInCity.description = data["weather"][0]["description"]
    //             weatherInCity.pressure = data["main"]["pressure"] 
    //             weatherInCity.city_api = data['name']
    //             weatherInCity.lat = data['coord']['lat']
    //             weatherInCity.lon = data['coord']['lon']
    //         }
    //         console.log("weatherInCity=>", weatherInCity);
    //         forecast(weatherInCity.lat, weatherInCity.lon);
    //         // setWeather(data);
    //     } catch (e) {
    //         console.log(e);
    //     }
    // }

    const handleCity = (event) => {
       
        if (event.keyCode === 13) {
            console.log("search city starts");
            console.log(event.target.value);
            cityInfo(event.target.value);
        }

    }
    


    return(
        <div>
            <h1>Weather Info:</h1>
      
                <input value = {newCity} onChange={e => setNewCity(e.target.value)} onKeyDown={handleCity} type="text" id="cityInput"/>
     
   
        </div>
 
    )
}

export default Weather;