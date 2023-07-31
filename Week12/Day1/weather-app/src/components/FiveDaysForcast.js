import {useContext,useEffect,useState} from 'react'
import {AppContext} from '../App';
import {getDayOfTheWeek, getShortDate} from '../helpers/dates'

const BASE_URL = process.env.REACT_APP_BASE_URL;
const API_KEY = process.env.REACT_APP_API_KEY;

const FiveDaysForcast = (props) => {
  const [forcastWeather, setForcastWeather] = useState({})
  const {city,cityKey,metric} = useContext(AppContext);

  useEffect(()=>{
    getForcastWeather(cityKey)
  },[cityKey])

  const getForcastWeather = (cityKey) => {
     fetch(`${BASE_URL}/forecasts/v1/daily/5day/${cityKey}?apikey=${API_KEY}&metric=${metric}`)
     .then(res=>res.json())
     .then(data=>{
       // console.log('Forcast',data);
       setForcastWeather(data)
     })
     .catch(e=> {
       console.log(e);
     })
   }



  return(
    <>
      <h2>Five Days Forcast</h2>
      {
        forcastWeather.DailyForecasts?forcastWeather.DailyForecasts.map((day,i) => {
          return(
            <div key={i} style={{
                            display:'inline-block',
                            border:'1px solid #ccc',
                            margin:'10px'}}>
              <p>
                { getDayOfTheWeek(day.Date) }
                <br/>
                { getShortDate(day.Date) }
              </p>
              <p>{
                <img src={`https://developer.accuweather.com/sites/default/files/${day.Day.Icon<10?'0'+day.Day.Icon:day.Day.Icon}-s.png`} />
              }<br/>
                {day.Temperature.Maximum.Value} {day.Temperature.Maximum.Unit}
              </p>
              <p>{
                <img src={`https://developer.accuweather.com/sites/default/files/${day.Night.Icon<10?'0'+day.Night.Icon:day.Night.Icon}-s.png`} />
              }<br/>
                {day.Temperature.Minimum.Value} {day.Temperature.Minimum.Unit}
              </p>
            </div>
          )
        }):null
      }
    </>
  )
}
export default FiveDaysForcast
//https://dataservice.accuweather.com/forecasts/v1/daily/5day/623?apikey=4x0wFtVYvGqcsciZNrDwEye6ZE7gQkQW
