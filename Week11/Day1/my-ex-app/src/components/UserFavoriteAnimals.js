const UserFavoriteAnimals = (props) => {
    const {favAnimals} = props;
    return (
        <ul>
            {
            favAnimals.map((item, index) => {
                return (
                    <li key = {index}> {item} </li> 
                )
          })
        }
        </ul>
    )
}

export default UserFavoriteAnimals