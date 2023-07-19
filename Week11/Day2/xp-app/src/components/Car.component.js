import React from "react"
import Garage from './Garage.component'

class Car1 extends React.Component {
    constructor() {
        super();
        console.log("this cat test constructor");
        this.state = {color:"red"};
    }
    render() {
        return (
        <>
        <header>This car Model is a: {this.props.info.model}</header>
        <h1>This is a car { this.state.color }</h1>
        < Garage size = "small" />
        </>
        );
    }
}

//function 
const Car = (props) => {
const {info} = props;
const color = "red"
        return (
        <>
        <header>This car Model is a: { info.model }</header>
        <h1>This is a car { color }</h1>
        < Garage size = "small" />
        </>
        );
    
}

export default Car;