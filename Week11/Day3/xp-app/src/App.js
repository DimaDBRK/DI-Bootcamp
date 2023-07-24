
import './App.css';
import { useState } from "react";
import React from "react";
import ErrorBoundary from './components/ErrorBoundary';

import './components/style.css'

import Color from './components/Color.component';

const BuggyCounter = (props) => {
  const [counter, setCounter] = useState(0);
  
  const handleClick = () => {
    console.log("click");
    setCounter(counter + 1);
  }
  if (counter >= 5) {
    throw new Error("I crashed!")
  }
  return (
    
      <h1 onClick={ handleClick }>{ counter }</h1>

)
}

// Add a Class component named Child to the same file. This new component will render a ‘Hello World!’ message in a header tag.
class ChildClass extends React.Component {
  componentWillUnmount() {
    alert("Header will be unmounted. I use componentWillUnmount  built-in method")
  };
  
  render() {
    return(
      <h1>Hello World!</h1>
    )
  }
}

function App() {
//  Add a new property named show to the state object. Set the value of this property to true.
const [show , setShow] = useState(true);

const handleClick = () => {
  setShow(!show);
}
  return (
    <div className="App">
      <p>Ex1</p>
      <h1>Click on the numbers to increase the counters.
The counter is programmed to throw error when it reaches 5. This simulates a JavaScript error in a component.
      </h1>
      <hr></hr>
    
      <p>These two counters are inside the same error boundary. If one crashes, the error boundary will replace both of them.
      </p>
      <ErrorBoundary>
          <BuggyCounter />
          <BuggyCounter />
      </ErrorBoundary>
      <hr></hr>
      <p>These two counters are each inside of their own error boundary. So if one crashes, the other is not affected.
      </p>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <hr></hr>
      <p>This counter is not inside of boundary. So if crashes, all other components are deleted.</p>
      <BuggyCounter />
      <p>Exercise 2 : Lifecycle (base on XP4 Day2)</p>
      <Color/>
      <p>Exercise 3 : Lifecycle #2</p>
      
      { show? <ChildClass/> : null}
      <button onClick={handleClick}>{show?'Remove header Ex3':'Add header'}</button>

    </div>
  );
}

export default App;
