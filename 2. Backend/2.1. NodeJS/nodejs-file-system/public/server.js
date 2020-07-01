var http = require('http');
var fs = require('fs');

//404 error response
function the404Response(response){
    response.writeHead(404,{"Content-Type":"text/plain"});
    response.write("Error 404: Page Not Found...");
    response.end();
}
//Handle a user request
function onRequest(request,response){
    if(request.method=='GET' && request.url=='/'){
        response.writeHead(200,{"Content-Text":"text/html"});
        fs.createReadStream("./index.html").pipe(response);
    }else{
        the404Response(response);
    }

}
http.createServer(onRequest).listen(3000);
console.log("server is running on localhost:3000");