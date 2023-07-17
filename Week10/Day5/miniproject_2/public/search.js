const searchTitle = async () => {
    console.log("Search Title starts");
    //collect info from inputs
    const titleForSearch = document.getElementById('title-input').value;
  
    try {
        const res = await fetch('/search/title',{
            method:'POST',
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                title: titleForSearch             
                
            })
            });

            if (res.status === 200) {
              
                const data = await res.text();
                console.log(data);
                // document.open();
                // document.write(data);
                // document.close();
                
            } 
    } catch (err) {
        console.log("ERROR FROM SERVER:", err)
    }

}

const searchCategory = async () => {
    console.log("Search category starts");
    //collect info from inputs
    const categoryForSearch = document.getElementById('category-input').value;
  
    try {
        const res = await fetch('/search/category',{
            method:'POST',
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                category: categoryForSearch             
                
            })
            });

            if (res.status === 200) {
              
                const data = await res.text();
                console.log(data);
                document.open();
                document.write(data);
                document.close();
            }
               
               
         
    } catch (err) {
        console.log("ERROR FROM SERVER:", err)
    }

}