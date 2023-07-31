export const addToLoacalStorge = (key, data) => {
    window.localStorage.setItem(key,JSON.stringify(data));
  }
  
  export const getFromLoacalStorage = (key) => {
    return JSON.parse( window.localStorage.getItem(key) ) || [];
  }
  