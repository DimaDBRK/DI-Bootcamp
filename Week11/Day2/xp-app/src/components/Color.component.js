import React, { Component } from "react"


class Color extends React.Component {
    constructor(props) {
      super(props);
      this.state = {favoriteColor : "red"};
    }
    static getDerivedStateFromProps() {
        console.log("Derived")
    }

    changeColor = () => {
        this.setState({favoriteColor : "blue"});
    }

    render() {
        console.log("render")
       return (

           <>
           <h1>My favorite color is : {this.state.favoriteColor}</h1>
           <button onClick={ this.changeColor }>Change color</button>
           </>
       )
    }
    componentDidMount() {
        setTimeout(() => {
            this.setState({favoriteColor:"yellow"})
        },5000)
    }
}
   
  

export default Color;
