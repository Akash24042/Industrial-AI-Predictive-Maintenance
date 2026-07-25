const predictionForm = document.getElementById("predictionForm");

const result = document.getElementById("result");
const riskLevel = document.getElementById("riskLevel");
const probability = document.getElementById("probability");
const progressBar = document.getElementById("progressBar");
const recommendationText = document.getElementById("recommendationText");


predictionForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const temperature = Number(
        document.getElementById("temperature").value
    );

    const vibration = Number(
        document.getElementById("vibration").value
    );

    const pressure = Number(
        document.getElementById("pressure").value
    );

    const rpm = Number(
        document.getElementById("rpm").value
    );

    const operating_hours = Number(
        document.getElementById("operating_hours").value
    );


    const machineData = {
        temperature: temperature,
        vibration: vibration,
        pressure: pressure,
        rpm: rpm,
        operating_hours: operating_hours
    };


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(machineData)
            }
        );


        if (!response.ok) {
            throw new Error("Prediction request failed");
        }


        const data = await response.json();


        result.classList.remove("hidden");


        riskLevel.textContent =
            data.risk_level;


        probability.textContent =
            data.failure_probability + "%";


        progressBar.style.width =
            data.failure_probability + "%";


        recommendationText.textContent =
            data.recommendation;


        if (data.risk_level === "LOW") {

            riskLevel.style.color = "#28d17c";
            progressBar.style.background = "#28d17c";

        }

        else if (data.risk_level === "MEDIUM") {

            riskLevel.style.color = "#f5b942";
            progressBar.style.background = "#f5b942";

        }

        else {

            riskLevel.style.color = "#ff5c6c";
            progressBar.style.background = "#ff5c6c";

        }

    }


    catch (error) {

        console.error(error);

        alert(
            "Unable to connect to the AI server. Make sure Flask is running."
        );

    }

});