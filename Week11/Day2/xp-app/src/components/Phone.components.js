import React, { Component } from "react"

const changeColor = (event) => {
    console.log("Click color", event);
}

class Phone extends Component {
 constructor(props) {
    super(props);
    this.state = {
        brand: "Samsung",
        model: "Galaxy S20",
        color: "black",
        year: 2020
    };
 }

changeColor = (event) => {
    console.log("Click color", event);
    this.setState({ color: "blue",})
}

 render() {
  
    return (
        <>
            <h2>This phone brand is { this.state.brand }</h2>;
            <h3>It's a { this.state.color } { this.state.model } from { this.state.year }</h3>
            <button onClick={ this.changeColor }>Change color</button>
        </>
    )
 }
}

export default Phone;