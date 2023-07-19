import React from 'react'

const clickMe = () => {
    alert("I was clicked");
}

const handleKeyPress = (event) => {
    console.log();
    if (event.keyCode !== 13) {
       return 
    }
    console.log("Enter pressed, input = ", event.target.value);
}

class Events extends React.Component {
    ToggleButton = () => {
        this.setState({ isToggledOn:!this.state.isToggledOn }); 
    }
    constructor(props) {
        super(props);
        this.state = { isToggledOn: true }
    }
    render() {
        const buttonMessage = (this.state.isToggledOn)? "ON" : "Off";
        // console.log("change:", this.state.isToggledOn, buttonMessage);
        return (
            <>
            <p>Hello</p>
            <button onClick={clickMe}>Click</button>
            <input type="text" onKeyDown={handleKeyPress}></input>
            <button onClick ={this.ToggleButton}>{ buttonMessage }</button>
            </>
        );
    }
}


export default Events