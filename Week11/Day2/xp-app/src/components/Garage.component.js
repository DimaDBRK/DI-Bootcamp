import React from "react"

// class Garage extends React.Component {
//     render() {
//         return (
//             <>
//                 <p>Who lives in my Garage?</p>
//             </>
//         );
//     }
// }

function Garage(props) {
    const {size} =  props;
    return (
                <>
                    <p>Who lives in my { size } Garage?</p>
                </>
    );
}

export default Garage;