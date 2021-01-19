const fs = require('fs');
var esprima = require('esprima');
var counter = 0;
var counter2 = 0;
var text = fs.readFileSync("so-benign-very-high-20000-2.txt", "utf-8");
var file_data = text.split("\n");
for(i = 0; i < file_data.length; i++) {
    let line = file_data[i];
    counter2++;
    try 
    {
        /*if(line.includes("&#58;") && line.includes("\"&#11;")){
            var mySubString = line.substring(
                line.lastIndexOf("&#58;") + 5, 
                line.indexOf("\"&#11;")
            );
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }
        else if(line.includes("load=") && line.includes(">\"")){
            var mySubString = line.substring(
                line.lastIndexOf("load=") + 5, 
                line.indexOf(">\"")
            );
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }
        else if(line.includes('javascript:')){
            var start_index = line.indexOf('javascript:') + 11;
            var remaining_str = line.substr(start_index);
            var mySubString = '';
            if(remaining_str.includes('&Tab')){
                mySubString = remaining_str.substring(0,remaining_str.indexOf('&Tab'));
            }
            else if(remaining_str.includes('"></')){
                mySubString = remaining_str.substring(0,remaining_str.indexOf('"></'));
            }
            else if(remaining_str.includes('</')){
                mySubString = remaining_str.substring(0,remaining_str.indexOf('</'));
            }
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }
        else if(line.includes("onerror=") && line.includes(";>")){
            var mySubString = line.substring(
                line.lastIndexOf("onerror=") + 8, 
                line.indexOf(";>")
            );
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }
        else if(line.includes("onerror=") && line.includes("//")){
            var mySubString = line.substring(
                line.lastIndexOf("onerror=") + 8, 
                line.indexOf("//")
            );
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }
        else if(line.includes("onerror=") && line.includes(">")){
            var mySubString = line.substring(
                line.lastIndexOf("onerror=") + 8, 
                line.indexOf(">")
            );
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }
        else if(line.includes("<script>") && line.includes("</script")){
            var mySubString = line.substring(
                line.lastIndexOf("<script>") + 8, 
                line.indexOf("</script")
            );
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }
        else if(line.includes("<SCRIPT>") && line.includes("</SCRIPT>")){
            var mySubString = line.substring(
                line.lastIndexOf("<SCRIPT>") + 8, 
                line.indexOf("</SCRIPT>")
            );
            console.log(counter2 + ' -> ' + mySubString);
            esprima.parseScript(mySubString);
        }*/
        esprima.parseScript(line);
    }
    catch(err) {
        counter++;
        console.log('Error{' + counter + "}: " + line);
    }
}
syntax_correctness = ((file_data.length - counter)/file_data.length) * 100;
console.log("syntactic correctness: " + syntax_correctness + "%")