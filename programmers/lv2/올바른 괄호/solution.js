function solution(s) {
  let target = [...s];
  let leftstack = [];
  let rightstack = [];

  for (let t of target) {
    if (t === "(" && rightstack.length === 0) {
      leftstack.push(t);
    } else if (t === ")" && leftstack.length === 0) {
      rightstack.push(t);
    } else if (t === "(" && rightstack.length > 0) {
      rightstack.push(t);
    } else if (t === ")" && leftstack.length > 0) {
      leftstack.pop();
    }

    //         console.log("----------")
    //         console.log("left?", leftstack)
    //         console.log("right?", rightstack)
    //         console.log("----------")
  }

  if (!leftstack.length && !rightstack.length) {
    return true;
  }
  return false;
}
