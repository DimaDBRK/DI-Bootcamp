import React, { Component } from "react"


class Color extends React.Component {
    constructor(props) {
      super(props);
      this.state = {favoriteColor : "red"};
    }
    static getDerivedStateFromProps() {
        console.log("Derived");
        return null
    }

    // Part I : shouldComponentUpdate 2. If you set the return value of the shouldComponentUpdate() method to false, you won’t be able to change the value of the favoriteColor property to “blue”, (even after clicking on the button)
    
    shouldComponentUpdate() {
        // return false
        return true
    }
    // Part II: componentDidUpdate. 3. In the componentDidUpdate method, add a console.log("after update"). Open the Dev Tools, to see when this message is displayed.

    componentDidUpdate() {
        console.log("componentDidUpdate => after update");
        // starts every update
    }

    // Part III : getSnapshotBeforeUpdate Use the getSnapshotBeforeUpdate() method, add a console.log("in getSnapshotBeforeUpdate"). Open the Dev Tools, to see when this message is displayed.
    componentWillUnmount() {
        console.log("componentWillUnmount => in getSnapshotBeforeUpdate");
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
