import React from "react";
import data from "../data/data2.json";

const  Example2  = () => {
    return(
        <>
        <h2>Example2 Skills </h2>
       
            {
            data.Skills.map((item, index) => {
                return (
                <div key={index}>
                <h3>{item.Area}</h3>
                <ul>
                    {
                    item.SkillSet.map((skill,index)=>{
                        return <li key={skill.Name}>{skill.Name}</li>
                    })

                    }
                </ul>
                </div>
                )
                })
            }
       
        </>
    );
}

export default Example2;