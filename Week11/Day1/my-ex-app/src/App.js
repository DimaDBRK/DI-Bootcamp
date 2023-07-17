import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from './components/UserFavoriteAnimals';
import Exercise from './components/Exercise3';

const myelement = <h1>I Love JSX!</h1>;
const sum = 5 + 5;

// Exercise 2 : Object
const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* Exercise 1: With JSX*/}
        {/* 1. In the App.js file, display a “Hello World!” message in a paragraph.*/}
        <p>Hello World!</p>
        {/* Create a constant variable with JSX const myelement = <h1>I Love JSX!</h1>;, and render it on the page. */}
        {myelement}
        {/* Create a constant variable named sum, which value is 5 + 5. Render on the page, the following sentence "React is <sum> times better with JSX" */}
        <h1>React is {sum} times better with JSX</h1>


         {/*In the App.js file, render the first name and the last name of the user in two <h3>.  */}
         <h3> First name {user.firstName} </h3>
         <h3> Last name {user.lastName} </h3>
         <UserFavoriteAnimals favAnimals = {user.favAnimals}/>
        {/* 3 */}
        <Exercise/>
        <img src={logo} className="App-logo" alt="logo" />
        
       
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
