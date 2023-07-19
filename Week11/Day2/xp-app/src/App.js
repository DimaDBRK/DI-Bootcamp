import './App.css';

import Car from './components/Car.component';
import Events from './components/Events.component';
import Phone from './components/Phone.components';
import Color from './components/Color.component';

const carinfo = {name: "Ford", model: "Mustang"};

function App() {
  return (
    <>
      <p>Ex1</p>
      <Car info = {carinfo} />
      <p>Ex2</p>
      <Events/>
      <p>Ex3</p>
      <Phone/>
      <p>Ex4</p>
      <Color/>
    </>
  );
}

export default App;
