/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/
/// {a: }
const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
  const obj = {}
  let newStr = ""
  for(let i = 0; i< str.length; i++){
    if(obj[str[i]]){
      continue
    } else {
      newStr += str[i]
      obj[str[i]] = 1
    }
    // obj[str[i]] = 1
    // console.log(obj)
    // if(obj[str[i]] === 1){
    //   newStr += str[i]
    // } 
    // else {
    //   continue
    // }
  }
  console.log(newStr)
  return newStr
}
stringDedupe(str2)