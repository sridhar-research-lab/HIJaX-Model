const {c, cpp, node, python, java} = require('compile-run');
var arr = ['prompt("var0","0");','alert("var0");','confirm("var0");','console.log("var0");'];
async function stuff(arr){
    for(i = 0; i < arr.length; i++){
        let resultPromise = await node.runSource(arr[i]);
        console.log(resultPromise);
    }
}

stuff(arr)