import '../App.css';
import { useState } from "react";
import Info from './Info.component';

// import FormData from 'form-data';

const countries = ['Thailand', 'Japan', 'Brazil'];

const Form = ({info}) => {
    const [values, setValues] = useState(
        {
        fname: '',
        lname: '',
        age: '',
        gender: '',
        destination: '',
        nonuts: false,
        nolactose: false,
        vegan: false
    });
    
    console.log("inform=>",values);
    
    //to show radiobuttons
       
    const setValueSmart = ({name, value}) =>{
        // const {name, value} = newInfo;
        console.log(name, value)
        setValues(oldValues => ({...oldValues, [name]: value }));
        
    };
    

    const sandFormData = async () => {
        const res = await fetch('/' + '?' +  new URLSearchParams(values) , {
          method: 'GET',
        //   headers: { 'Content-Type': 'application/json' },
        //   body: JSON.stringify(values)
        });
        // const data = await res.json();
        if (res.status !== 200) {
          throw new Error(`Request failed: ${res.status}`); 
        }
      }
    
    const clearForm = () => {
        setValues({
            fname: '',
            lname: '',
            age: '',
            gender: '',
            destination: '',
            nonuts: false,
            nolactose: false,
            vegan: false
        });
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log(event.target);
        try {
            await sandFormData();
            clearForm();
            alert('Your registration was successfully submitted!');
           
          } catch (e) {
            console.log(`Registration failed! ${e.message}`);
          }
    }
      
    

 
    // const onValueChange = (event) => {
       
    //     setGender(event.target.value);
    //     console.log("gender=>");
    // }

    // form change
    const onFormChange = (event) => {
        // check radio buttons
        // if (event.target.name === "gender") { 
        //     console.log('radio');
        //     setGender(event.target.value);
        // }
        // check check box
        if (event.target.type === "checkbox") { 
            console.log('checkbox');
            setValueSmart({name: event.target.name, value: event.target.checked});
        } else {
             setValueSmart({name: event.target.name, value: event.target.value}); 
        }


        // set value smart
        console.log("info setValueSmart=>", event.target.name, "val=>", values );


        // test target
        // console.log("form=>", event.target.name, "-",event.target.value);
       
    }
    

    return (
        <>
        <h1>DC: Form</h1>
        <form onChange = {onFormChange} onSubmit = {handleSubmit}>
            <input type="text" name="fname" placeholder="First Name" onChange={e => {}} value={values['fname']}/>
            <input type="text" name="lname" placeholder="Last Name" onChange={e => {}} value={values['lname']}/>
            <input type="text" name="age" placeholder="Age" onChange={e => {}} value={values['age']}/>
            
                <label htmlFor="female">Male</label>
                <input type="radio" id="male" name="gender" value="male" 
                checked={values['gender']==="male"}
                onChange={e => {}}
                // onClick={onValueChange}
                /> 
          
       
                <label htmlFor="female">Femail</label>
                <input type="radio" id="female" name="gender" value="female" 
                checked={values['gender'] === "female"}
                onChange={e => {}}
                // onClick={onValueChange}
                /> 
                
        
            <label htmlFor="destination"> Destination:</label>
            <select name="destination" id="destination" value={values['destination']} onChange={e => {}}>
                <option value="">Select...</option>
                {countries.map(country => <option key={country}>{country}</option>)}
            </select>
            <p>Dietary restriction</p>
            <label htmlFor="nuts">No nuts</label>
            <input type="checkbox" name="nonuts" id="nuts" onChange={e => {}} checked={values['nonuts']}></input>
            <label htmlFor="lactose">No lactose</label>
            <input type="checkbox" name="nolactose" id="lactose" onChange={e => {}} checked={values['nolactose']}></input>
            <label htmlFor="vegan">Vegan</label>
            <input type="checkbox" name="vegan" id="vegan" onChange={e => {}} checked={values['vegan']}></input>

            <input type='submit' value='Send'/>
            <button type="reset" onClick={clearForm}>Clear</button>
        </form>
        <Info info={values}/>
        </>
    );

};

export default Form;