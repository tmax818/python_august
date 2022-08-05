/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
  R - read/restate
  I - input 
  O - output
  T - talk

  WALK
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {
    let newArr = str.split(" ")
    console.log(newArr)
    let newStr = ""
    for(let i = 0; i < newArr.length;i++){
      console.log(newArr[i][0])
      let temp = newArr[i][0]
      console.log(temp)
      newStr += temp.toUpperCase()
    }
    console.log(newStr)
} 



acronymize(str1)
acronymize(str2)
acronymize(str3)
// acronymize(str4)