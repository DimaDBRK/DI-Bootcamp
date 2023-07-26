import React from "react";
import data from "../data/data3.json";

const  Example3  = () => {
    return(
        <>
        <h2>Example3 Skills </h2>
       
            {
            data.Experiences.map((item, index) => {
                return (
                <div key={index}>
                    <img src={item.logo} alt="logo" style={{ width: '200px', }}/>
                    <h3 ><a href={item.url}>{item.companyName}</a></h3>
              
                    {
                    item.roles.map((role,index)=>{
                        return (
                            <div key={role.title}>
                                
                                <h4 >{role.title}</h4>
                                <p>{role.startDate} {role.location}</p>
                                <p>{role.description}</p>
                            </div>
                        )
                    })

                    }
                </div>
                
                )
                })
            }
       
        </>
    );
}

export default Example3;