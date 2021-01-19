const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const checklist = require('./checklist.js');
const checkArray = checklist.check;

const key = 'X5aPmbfL)2har15ph1oXEQ((';
const searchFilter = 'A(e6zppbsTuWqLugAlVBYvnCgLuXD';
const answerFilter = '!-.7zMlVR.MUL';
const url = 'https://api.stackexchange.com/2.2/';
const nottagged = fs.readFileSync('nottagged.txt', 'UTF-8');
const tagged = fs.readFileSync('tagged.txt', 'UTF-8');
var page = '2';
var pagesize = '100';

var testList = '';
var list = [];
var valid = true;
var has_more = true;


    page += 1; //to get next page
   
    let promise = new Promise (function(resolve, reject){ //calls stackexchange API
        resolve(axios.get(`https://api.stackexchange.com//2.2/search/advanced?page=${page}&pagesize=${pagesize}&fromdate=1104537600&order=desc&min=10&sort=votes&accepted=True&closed=False&tagged=${tagged}&nottagged=${nottagged}&title=how&site=stackoverflow&filter=${searchFilter}&key=${key}`));
    })
    .then(function(response){
            has_more = response.data.has_more;
            console.log("HAS MORE: ", has_more);
            response.data.items.forEach(item =>{
                console.log(item.tags);
                checkArray.every(i => { //validates that items in checklist.js are not in the tags of the question
                    if(item.tags.includes(i)){
                        console.log(i);
                        valid = false;
                        console.log('valid set false');
                    }});
                if(valid == true){
                    list.push([item.title, item.accepted_answer_id]); 
                }
                valid = true;
            })
            return list;
        })
    
    .then(function(list){
        new Promise(function(resolve,reject){
            list.forEach(listSet =>{
                var writestreamQ = fs.createWriteStream('./testQuestions.txt', {flags: 'a'}); //append question to txt file
                writestreamQ.write(JSON.stringify(listSet[0]) + "\n");
                writestreamQ.end();
                console.log("Q: ", listSet[0]);
    
                let id = listSet[1];
                new Promise (function(resolve, reject){
                    resolve(axios.get(`${url}answers/${id}?order=desc&sort=activity&site=stackoverflow&filter=${answerFilter}&key=${key}`));
                })        
                .then(response =>{
                    new Promise (function(resolve, reject){
                        $ = cheerio.load(response.data.items[0].body);
                        var answer = $('pre').html(); // selecting only code portions of answer
                        answer = answer.replace(/&quot;/g, "'");
                        answer = answer.replace(/&apos;/g, "'");
                        answer = answer.replace(/&lt/g, "<");
                        answer = answer.replace(/&gt/g, ">");
                        answer = answer.replace(/\/\/.*\n/g, '');
                        answer = answer.replace(/\n/g, '');
                        answer = answer.replace(/<code>/g, '');
                        answer = answer.replace(/<\/code>/g, '');
    
                        var writestreamA = fs.createWriteStream('./testAnswers.txt', {flags: 'a'}); //append answer to txt file
                        writestreamA.write(JSON.stringify(answer) + "\n");
                        writestreamA.end();
                        console.log("A: ", answer);
    
                        resolve();
                    }) 
                })
                .catch(error =>{throw error})
            }); 
            resolve();
        })
    })

