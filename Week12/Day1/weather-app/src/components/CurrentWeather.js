import {useContext,useEffect,useState} from 'react'
import {AppContext} from '../App';
import {getFromLoacalStorage,addToLoacalStorge} from '../helpers/storage'

const BASE_URL = process.env.REACT_APP_BASE_URL;
const API_KEY = process.env.REACT_APP_API_KEY;
const FAVORITE = getFromLoacalStorage('favorite');

const CurrentWeather = (props) => {
   const [currentWeather, setCurrentWeather] = useState([]);
   const [favorite, setFavorite] = useState([])
   const {city,cityKey,metric,country,setCity,setCountry} = useContext(AppContext);

   useEffect(()=>{
     const getFavorites = async() => {
       await setFavorite(FAVORITE);
     }
    getFavorites();
   },[props.country,props.city]);

   useEffect(()=>{

     getCurrentWeather(props.cityKey||cityKey);

   },[cityKey,props.cityKey])

   const getCurrentWeather = (cityKey) => {
      fetch(`${BASE_URL}/currentconditions/v1/${cityKey}?apikey=${API_KEY}&metric=${metric}`)
      .then(res=>res.json())
      .then(data=>{
        // console.log(data);
        setCurrentWeather(data)
      })
      .catch(e=> {
        console.log(e);
      })
    }

    const addToFavorite = async () => {
      favorite.push({city,country,cityKey})
      let newFavorite = [...favorite]
      await addToLoacalStorge('favorite',newFavorite)
      await setFavorite(newFavorite)
    }

    const removeFromFavorite = async () => {
      let index = favorite.findIndex(item => item.cityKey == cityKey)
      favorite.splice(index,1);
      let newFavorite = [...favorite]
      await addToLoacalStorge('favorite',newFavorite)
      await setFavorite(newFavorite)
    }

    const isCityInFavorite = () => {
      let index = favorite.findIndex(item => item.cityKey == cityKey)
      return index===-1 ? false: true;
    }

    if(currentWeather.length===0) return null;

    return(
      <div>
        <h4>{!props.cityKey ? 'Current Weather':null}</h4>
        <p>{props.city||city}<br/>{props.country||country}</p>
        <p>{
          currentWeather[0].Temperature.Metric.Value
        }</p>
        <p>{
          currentWeather[0].WeatherText
        }</p>
        <p>{
          <img src={`https://developer.accuweather.com/sites/default/files/${currentWeather[0].WeatherIcon<10?'0'+currentWeather[0].WeatherIcon:currentWeather[0].WeatherIcon}-s.png`} />
        }</p>
        {
          !props.cityKey ?
          isCityInFavorite()?
          <button onClick={()=>removeFromFavorite()}>Remove From Favorite</button>
          :
          <button onClick={()=>addToFavorite()}>Add To Favorite</button>
          : null
        }

      </div>
    )
}
export default CurrentWeather
//https://dataservice.accuweather.com//currentconditions/v1/623?apikey=4x0wFtVYvGqcsciZNrDwEye6ZE7gQkQW
