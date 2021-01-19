const {c, cpp, node, python, java} = require('compile-run');
const fs = require('fs');
var esprima = require('esprima');
var text = fs.readFileSync("so-base-code.txt", "utf-8");
const sourcecode = text.split("\n");
id_ignore = ['console','prompts','confirm','alert','log','setTimeout','Math','round','pow','sqrt','ceil','floor','sin','cos','min','max','exp','random','Number','toString','length','pop','shift','unshift','reverse','toUpperCase','toLowerCase', 'sort'];
initArr = [`''`, `[]`];
counter_1 = 0;
counter_2 = 0;

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
        let varArr = [];
        for(j = 0; j < tokenArr.length; j++){
            if(j < (tokenArr.length-1)){
                if((tokenArr[j].type == 'Identifier') && (tokenArr[j+1].value == '(')){

                }
            }
            if(j > 0){
                if((tokenArr[j].type == 'Identifier') && (tokenArr[j-1].type == 'Keyword')){
                    if((tokenArr[j-1].value == 'var') || (tokenArr[j-1].value == 'let') || (tokenArr[j-1].value == 'const')){
                        continue;
                    }
                }
            }
            if((tokenArr[j].type == 'Identifier') && !(id_ignore.includes(tokenArr[j].value))){
                varArr.push(tokenArr[j].value);
            }
        }
        let uniqueVarArr = [...new Set(varArr)];
        let finalStr1 = '';
        let finalStr2 = '';
        if(uniqueVarArr.length > 0){
            for(j = 0; j < uniqueVarArr.length; j++){
                finalStr1 += 'var ' + uniqueVarArr[j] + '='+ initArr[0] +'; ';
                finalStr2 += 'var ' + uniqueVarArr[j] + '='+ initArr[1] +'; ';
            }
        }
        finalStr1 += tempSTR;
        finalStr2 += tempSTR;
        let val = await compileStr(finalStr1, finalStr2);
        //let val = await compileStrOld(tempSTR);
        //console.log(val);
        //console.log('------------------------------------');
        output.push({code_1: finalStr1, errorVal_1: val[0].exitCode, code_2: finalStr2, errorVal_2: val[1].exitCode, error1: val[1].stdout, error2: val[1].stdout});
    }
    return output;
}
async function compileStrOld(codeStr){
    let resultPromise = await node.runSource(codeStr);
    return resultPromise;
}
async function compileStr(codeStr1, codeStr2){
    let resultPromise1 = await node.runSource(codeStr1);
    let resultPromise2 = await node.runSource(codeStr2);
    return [resultPromise1, resultPromise2];
}
function findFunctions(){
    let functionsArr = [];
    functionVal = [];
    loop1:
    for(i = 0; i < tokenArr.length; i++){
        if(i <= (tokenArr.length-3)){
            if((tokenArr[i].type == 'Identifier') && (tokenArr[i+1].value == '(')){
                loop2:
                for(j = i; j < tokenArr.length; j++){
                    if(tokenArr[j].value == ')'){
                        functionVal.push(tokenArr[j].value);
                        break loop2;
                    }
                    else{
                        functionVal.push(tokenArr[j].value);
                    }
                }
                functionsArr.push(functionVal);
                functionVal = [];
            }
        }
    }
}
async function printStuff(){
    let results = await testCode(sourcecode);
    for(i = 0; i < results.length; i++){
        console.log('{' + (i+1) + '}');
        if((results[i].errorVal_1== 0) || (results[i].errorVal_2 == 0) || (results[i].errorVal_1== null) || (results[i].errorVal_1== null)){
            if(results[i].errorVal_1== 0){
                console.log('clean(1): ' + results[i].code_1);
            }
            else{
                console.log('clean(2): ' + results[i].code_2);
            }
            counter_1++;
        }
        else{
            console.log('error: ' + results[i].code_1 + ' <------> ' + results[i].code_2);
            counter_2++;
        }
    }
    let sucessRate = (counter_1 / results.length)*100;
    console.log('total: ' + results.length + ', correct: ' + counter_1 + ', errors: ' + counter_2 + ' -> success rate(' + sucessRate + '%)');
    
}
printStuff();