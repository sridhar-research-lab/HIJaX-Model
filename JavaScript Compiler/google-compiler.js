var esprima = require('esprima');
const fs = require('fs');
const ClosureCompiler = require('google-closure-compiler').jsCompiler;
var text = fs.readFileSync("benign-base-code.txt", "utf-8");
const sourcecode = text.split("\n");
const closureCompiler = new ClosureCompiler({
  compilation_level: 'ADVANCED'
});
id_ignore = ['console','prompts','confirm','alert','log','setTimeout','Math','round','pow','sqrt','ceil','floor','sin','cos','min','max','exp','random','Number','toString','length','pop','shift','unshift','reverse','toUpperCase','toLowerCase', 'sort', 'Object', 'constructor', 'Array', 'searchParams', 'performance', 'JSON','replace','split','join','includes','indexOf','search','splice','require','forEach','function','for','keys','hasOwnProperty','assign','push','concat','isArray','if','parseInt','get','now','toUpperCase','toLowerCase','parse','reduce','filter','parseFloat','toPrecision','values','charAt','substring','tan', 'of'];

async function testCode(arr){
    let output = [];
    for(i = 0; i < arr.length; i++){
        let tempSTR = '';
        if(i == arr.length-1){
            tempSTR = arr[i];
        }
        else{
            tempSTR = arr[i].substring(0, arr[i].length-1);
        }
        let tokenArr = await esprima.tokenize(tempSTR);
        //console.log(tokenArr);
        let varArr = [];
        let local_ignore = [];
        for(j = 0; j < tokenArr.length; j++){
            if(j > 0){
                if((tokenArr[j-1].value == '.') && (tokenArr[j].type == 'Identifier')){
                    continue;
                }
            }
            if(j < (tokenArr.length-1)){
                if((tokenArr[j+1].value == 'of') && (tokenArr[j].type == 'Identifier')){
                    local_ignore.push(tokenArr[j].value);
                    continue;
                }
            }
            if(j > 1){
                if((tokenArr[j-2].value == 'function') && (tokenArr[j-1].value == '(') && (tokenArr[j].type == 'Identifier')){
                    local_ignore.push(tokenArr[j].value);
                    continue;
                }
            }
            if(j < (tokenArr.length-1)){
                if((tokenArr[j].type == 'Identifier') && (tokenArr[j+1].value == '(') && !(id_ignore.includes(tokenArr[j].value))){
                    let new_string = tokenArr[j].value + '()';
                    varArr.push(new_string);
                    continue;
                }
            }
            if(j > 0){
                if((tokenArr[j].type == 'Identifier') && (tokenArr[j-1].type == 'Keyword')){
                    if((tokenArr[j-1].value == 'var') || (tokenArr[j-1].value == 'let') || (tokenArr[j-1].value == 'const')){
                        continue;
                    }
                }
            }
            if((tokenArr[j].type == 'Identifier') && !(id_ignore.includes(tokenArr[j].value)) && !(local_ignore.includes(tokenArr[j].value))){
                varArr.push(tokenArr[j].value);
            }
        }
        let uniqueVarArr = [...new Set(varArr)];
        finalStr = '';
        finalArr = [];
        if(uniqueVarArr.length > 0){
            for(j = 0; j < uniqueVarArr.length; j++){
                if(uniqueVarArr[j].includes('()')){
                    finalStr += 'function ' + uniqueVarArr[j] + '{}; ';
                }
                else{
                    finalStr += 'var ' + uniqueVarArr[j] + '= ?; ';
                }
            }
        }
        let slot_arr = [`''`, `[]`,`0`, `new URL(document.location)`];
        let all_combos = [];
        if(uniqueVarArr.length == 1){
            for(j = 0; j < slot_arr.length; j++){
                let tempArr = [slot_arr[j]];
                all_combos.push(tempArr);
            }
        }
        else if(uniqueVarArr.length == 2){
            for(j = 0; j < slot_arr.length; j++){
                for(k = 0; k < slot_arr.length; k++){
                    let tempArr = [slot_arr[j], slot_arr[k]];
                    all_combos.push(tempArr);
                }
            }
        }
        else if(uniqueVarArr.length == 3){
            for(j = 0; j < slot_arr.length; j++){
                for(k = 0; k < slot_arr.length; k++){
                    for(l = 0; l < slot_arr.length; l++){
                        let tempArr = [slot_arr[j], slot_arr[k], slot_arr[l]];
                        all_combos.push(tempArr);
                    }
                }
            }
        }
        for(j = 0; j < all_combos.length; j++){
            let strHolder = finalStr;
            for(k = 0; k < all_combos[j].length; k++){
                strHolder = strHolder.replace('?', all_combos[j][k]);
            }
            finalArr.push(strHolder);
        }
        let val;
        if(tempSTR[tempSTR.length-1] != ';'){
            tempSTR = tempSTR + ';';
        }
        if(uniqueVarArr.length > 0){
            val = await compileStr(finalArr, tempSTR);
        }
        else{
            val = await compileStrSimple(finalStr + tempSTR);
        }
        //console.log(val);
        output.push(val);
    }
    return output;
}
async function compileStr(codeArr, rest){
    let errorCodes = [];
    for(a = 0; a < codeArr.length; a++){
        let input_str = codeArr[a] + rest;
        console.log(input_str);
        let resultPromise = await closureCompiler.run([{
            src: input_str,
            sourceMap: null
            }], (exitCode, stdOut, stdErr) => {
            console.log('code: ' + codeStr);
            console.log('exit: ' + exitCode);
            console.log('output: ' + stdOut);
            console.log('error: ' + stdErr);
            errorCodes.push(exitCode);
        });
    }
    console.log('$');
    return errorCodes;
}

async function compileStrSimple(input_str){
    let errorCodes = [];
    console.log(input_str);
    let resultPromise = await closureCompiler.run([{
        src: input_str,
        sourceMap: null
        }], (exitCode, stdOut, stdErr) => {
        console.log('code: ' + codeStr);
        console.log('exit: ' + exitCode);
        console.log('output: ' + stdOut);
        console.log('error: ' + stdErr);
        errorCodes.push(exitCode);
    });
    console.log('$');
    return errorCodes;
}

async function run(input){
    let results = await testCode(input);
}

run(sourcecode);