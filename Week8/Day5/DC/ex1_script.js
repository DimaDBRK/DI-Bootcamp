// DC

// consts, vars, data
const stringList = [{1:"Astronomer", 2: "Moon starer", "isAnagram": ""}, 
                    {1:"School master", 2: "The classroom", "isAnagram": ""},
                    {1:"The Morse Code", 2: "Here come dots", "isAnagram": ""},
                    {1:"This is not one", 2: "Yes, it is for test", "isAnagram": ""},
                  ]

// functions
function isAnagram(str1,str2) {
  // function to clean str for future compare
  function cleanString(str) {
    const res = str.replace(/[^a-z]/gi, '').toLowerCase();
  // [^a-z] matches everything but a-z
  // the flag `g` means it should match multiple occasions
  // the flag `i` is in case sensitive which means that `A` and `a` is treated as the same character ( and `B,b`, `C,c` etc )  
    return [...res].sort().join("");
  }

  return cleanString(str1)===cleanString(str2);
}

//Tests
console.log(isAnagram(stringList[3]["1"], stringList[3]["2"]));
// Driver
stringList.forEach((element, index) => {
  element["isAnagram"] = isAnagram(element["1"],element["2"])
  console.log(`#${index+1} "${element["1"]}" and "${element["2"]}" ${(element["isAnagram"])? "are":"are NOT"} anagrams.`)
}
  );
