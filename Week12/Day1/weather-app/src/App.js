import './App.css';
import Weather from './components/Weather';
import React, {useState,createContext} from 'react';
import AutoCompleteText from './components/AutoCompleteText'
import CurrentWeather from './components/CurrentWeather'
import FiveDaysForcast from './components/FiveDaysForcast'
import {Routes,Route} from 'react-router-dom';
import NavBar from './components/NavBar'
import Favorites from './components/Favorites'

export const AppContext = createContext(null);

function App() {

  const [city, setCity] = useState('Tel Aviv');
  const [country, setCountry] = useState('Israel');
  const [cityKey,setCityKey] = useState(215854);
  const [metric, setMetric] = useState(true);

  return (
    <div className="App">
     <NavBar/>
     <Routes>
      <Route path='/' element={
        <AppContext.Provider value={{
          city,
          setCity,
          cityKey,
          setCityKey,
          metric,
          setMetric,
          country,
          setCountry
      }}>
          <div className="App">
            <AutoCompleteText />
            <CurrentWeather />
            <FiveDaysForcast />
          </div>
        </AppContext.Provider>
      } />
      <Route path='/favorites' element={
        <AppContext.Provider value={{
          city,
          setCity,
          cityKey,
          setCityKey,
          metric,
          setMetric,
          country,
          setCountry
      }}>
         <Favorites/>
        </AppContext.Provider>
      } />
    </Routes>

    </div>
  );
}

export default App;
