let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // Check if the input text is empty
    if (!textToAnalyze.trim()) {
        document.getElementById("system_response").innerHTML = "";
        document.getElementById("error_message").innerHTML = "Invalid text! Please try again!";
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
                document.getElementById("error_message").innerHTML = "";
            } else if (this.status == 400) {
                let errorResponse = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = "";
                document.getElementById("error_message").innerHTML = errorResponse.error;
            } else {
                document.getElementById("system_response").innerHTML = "An unexpected error occurred.";
                document.getElementById("error_message").innerHTML = "";
            }
        }
    };

    // Make sure the text is encoded properly for URL parameters
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
