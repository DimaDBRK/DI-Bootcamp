import {useContext,useEffect,useState} from 'react'
import {AppContext} from '../App';
import {getFromLoacalStorage,addToLoacalStorge} from '../helpers/storage'
import CurrentWeather from './CurrentWeather';
import {useNavigate,useLocation} from 'react-router-dom';

const BASE_URL = process.env.REACT_APP_BASE_URL;
const API_KEY = process.env.REACT_APP_API_KEY;
const FAVORITE = getFromLoacalStorage('favorite');


const Favorites = (props) => {
  const [favorite, setFavorite] = useState([]);
  const [refresh, setRefresh] = useState(true);
  const {setCity,setCityKey,setCountry} = useContext(AppContext);
  const navigate = useNavigate();

  useEffect(()=>{
     const getFavorites = async() => {
       await setFavorite(FAVORITE);
       setRefresh(false)
     }
    getFavorites();
  })

  const showCity = (cityKey,city,country) => {
    setCityKey(cityKey);
    setCity(city);
    setCountry(country);
    navigate('/')
  }

  return(
    <>
      <h2>Favorites</h2>
      {
        favorite.map(city => {
          // console.log('favorite',city);
          return(
            <div onClick={()=> showCity(city.cityKey,city.city,city.country)} key={city.cityKey} style={{display:'inline-block',border:'1px solid #ccc', margin:'10px'}}>
              <CurrentWeather cityKey={city.cityKey} city={city.city} country={city.country}/>
            </div>
          )
        })
      }
    </>
  )
}
export default Favorites
