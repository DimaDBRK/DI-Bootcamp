import './Exercise3.css'

const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
  };


const Exercise = () => {
    return (
        <>
            <h1 style={
                {
                    color:'red',
                    backgroundColor:'lightblue'
                }
            }>Header 1</h1>
            <h1 style={style_header}>Headar for part 2</h1>
            
            <p className="para">Some text...</p>
            <a href= "">Link</a>
            <img src= {`https://robohash.org/2?size=150x150`} alt= ''/>
            <form>
                <input></input>
                <button>Submit</button>
            </form>
            <ul>
                <li>1 list</li>
                <li>2 list</li>
            </ul>

        </>
    );
};

export default Exercise