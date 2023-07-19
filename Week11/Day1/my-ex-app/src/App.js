import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from './components/UserFavoriteAnimals';
import Exercise from './components/Exercise3';
import Card from './components/BootstrapCard';
import "bootstrap/dist/css/bootstrap.min.css";

const myelement = <h1>I Love JSX!</h1>;
const sum = 5 + 5;

// Exercise 2 : Object
const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

// Gold
const celebrities = [
  {
      title: 'Bob Dylan',
      imageUrl: 'https://miro.medium.com/max/4800/1*_EDEWvWLREzlAvaQRfC_SQ.jpeg',
      buttonLabel: 'Go to Wikipedia',
      buttonUrl: 'https://en.wikipedia.org/wiki/Bob_Dylan',
      description:
          'Bob Dylan (born Robert Allen Zimmerman, May 24, 1941) is an American singer/songwriter, author, and artist who has been an influential figure in popular music and culture for more than five decades.',
  },
  {
      title: 'McCartney',
      imageUrl:
          'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Paul_McCartney_in_October_2018.jpg/240px-Paul_McCartney_in_October_2018.jpg',
      buttonLabel: 'Go to Wikipedia',
      buttonUrl: 'https://en.wikipedia.org/wiki/Paul_McCartney',
      description:
          'Sir James Paul McCartney CH MBE (born 18 June 1942) is an English singer, songwriter, musician, composer, and record and film producer who gained worldwide fame as co-lead vocalist and bassist for the Beatles.',
  },
]

const planets = ['Mars','Venus','Jupiter','Earth','Saturn','Neptune' ];

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
        
       {/* Gold */}
       <Card celebrities = {celebrities}/>
      
       <ul className="list-group">
        {
          planets.map((item, index) => {
            return (
            <li key = {item} className="list-group-item"> {item} </li>
            )
          })
        }
      </ul>
        
        
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
