function solution(array, commands) {
  var answer = [];

  for (command of commands) {
    const [start, end, idx] = command;
    const newArr = array.slice(start - 1, end).sort((a, b) => a - b);
    //console.log(newArr)
    answer.push(newArr[idx - 1]);
  }

  return answer;
}
