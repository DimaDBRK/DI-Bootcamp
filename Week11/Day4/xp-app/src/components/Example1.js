import React from "react";
import data from "../data/data2.json";

const  Example1  = () => {
    return(
        <>
        <h2>Example1 SocialMedias</h2>
        <ul>
            {
            data.SocialMedias.map((item, index) => {
                return <li key={index}>{item}</li>
                })
            }
        </ul>
        </>
    );
}

export default Example1;