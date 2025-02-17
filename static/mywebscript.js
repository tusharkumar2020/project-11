let RunSentimentAnalysis = () => {
    // Get the text to analyze from the input field
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // Create a new XMLHttpRequest object
    let xhttp = new XMLHttpRequest();

    // Define what happens when the request is completed
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Parse the JSON response from the server
            let response = JSON.parse(xhttp.responseText);
            // Display the response text in the 'system_response' div
            document.getElementById("system_response").innerHTML = response.response;
        } else if (this.readyState == 4 && this.status == 400) {
            // Handle status code 400 (invalid text)
            document.getElementById("system_response").innerHTML = "Invalid text! Please try again.";
        } else if (this.readyState == 4) {
            // Handle other error responses
            document.getElementById("system_response").innerHTML = "Error: " + xhttp.responseText;
        }
    };

    // Prepare the POST request
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Send the text data as JSON in the request body
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
};