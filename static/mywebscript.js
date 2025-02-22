let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value.trim();

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            let response = JSON.parse(this.responseText);
            
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = response.response;
            } else if (this.status == 400) {  // Handling empty input case
                document.getElementById("system_response").innerHTML = response.error;
            } else {
                document.getElementById("system_response").innerHTML = "An unexpected error occurred.";
            }
        }
    };

    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    let data = JSON.stringify({ text: textToAnalyze });
    xhttp.send(data);
};
