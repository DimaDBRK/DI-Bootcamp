
import './App.css';
import { useState } from "react";
import './components/Language.css'
//data


function App() {
  
  const [languages, setLanguages] = useState([
      {name: "Php", votes: 0},
      {name: "Python", votes: 0},
      {name: "JavaSript", votes: 0},
      {name: "Java", votes: 0}
    ])
  
  const voite = (name) => {
    setLanguages(
      languages.map((item)=> 
        item.name === name ?{...item, votes: item.votes + 1} : {...item}
      )  
    );
  };
  
  console.log("test before rturn");
  console.log(languages[0].name);
  return (
      
    <div className="container">
    <h1>Vote Your Language!</h1>
      {
      languages.map((item, index) => {
        return (
        <div key={item.name} className="language-box" > 
          <p>{item.votes}</p>
          <p>{item.name}</p>
          <button onClick={() => voite(item.name) }>Click Here</button> 
        </div>
      )
      })
      }
    </div>
    
  );
}

export default App;
