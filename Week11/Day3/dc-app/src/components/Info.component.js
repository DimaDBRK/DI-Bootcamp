import '../App.css';
import { useState } from "react";

const Info = ({info}) => {
    // console.log(props)
    // const {info} = props;
    
    
    return (
        <>
        <h1>Entered info:</h1>
        <p>Your name: {info.fname} {info.lname}</p>
        <p>Your age: {info.age} </p>
        <p>Your gender: {info.gender} </p>
        <p>Your destinition: {info.destination}</p>
        <p>Your dietary restrictions:</p>
        <div>
            <p>**Nuts free:{info.nonuts ? 'Yes': 'No'}</p>
            <p>**Lactose free:{info.nolactose ? 'Yes': 'No'}</p>
            <p>**Vegan meal:{info.vegan ? 'Yes': 'No'}</p>
        </div>
        </>
    )
}

export default Info;