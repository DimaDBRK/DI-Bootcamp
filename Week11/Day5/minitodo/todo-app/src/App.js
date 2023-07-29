
import './App.css';
import Cards from './components/Cards';
import CardsDB from './components/CardsDB';

import { Routes, Route, Link } from "react-router-dom";


// fro DB - table todos
// create table todos (
// 	id serial primary key,
// 	todo varchar(255) not null,
// 	date date NOT NULL default current_date,
//   isdone boolean default false
// )

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <nav>
        <Link to="/">TODO on object</Link>{" /\\ "}
        <Link to="/db">TODO with DB</Link>{" /\\ "}
      
      </nav>
      <Routes>
        <Route path='/' element={<Cards/>}/>
        <Route path='/db' element={<CardsDB/>}/>
      </Routes >
        
      
      </header>
    </div>
  );
}

export default App;
