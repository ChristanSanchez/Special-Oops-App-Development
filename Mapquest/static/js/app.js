// ============================================
// DOM ELEMENTS
// ============================================

const form = document.getElementById("routeForm");

const originInput =
    document.getElementById("origin");

const destinationInput =
    document.getElementById("destination");

const swapButton =
    document.getElementById("swapButton");

const clearButton =
    document.getElementById("clearButton");

const findRouteButton =
    document.getElementById("findRouteButton");

const buttonContent =
    document.getElementById("buttonContent");

const loadingContent =
    document.getElementById("loadingContent");

const emptyState =
    document.getElementById("emptyState");

const errorState =
    document.getElementById("errorState");

const results =
    document.getElementById("results");

const errorMessage =
    document.getElementById("errorMessage");

const tryAgainButton =
    document.getElementById("tryAgainButton");


// ============================================
// ICON INITIALIZATION
// ============================================

lucide.createIcons();


// ============================================
// FORM SUBMISSION
// ============================================

form.addEventListener("submit", async (event) => {

    event.preventDefault();

    clearErrors();


    const origin =
        originInput.value.trim();

    const destination =
        destinationInput.value.trim();


    // Validation
    let valid = true;


    if (!origin) {

        document.getElementById(
            "originError"
        ).textContent =
            "Please enter a starting location.";

        valid = false;
    }


    if (!destination) {

        document.getElementById(
            "destinationError"
        ).textContent =
            "Please enter a destination.";

        valid = false;
    }


    if (!valid) {
        return;
    }


    const unit =
        document.querySelector(
            'input[name="unit"]:checked'
        ).value;


    const routeType =
        document.querySelector(
            'input[name="routeType"]:checked'
        ).value;


    const requestData = {
        origin: origin,
        destination: destination,
        unit: unit,
        route_type: routeType
    };


    setLoading(true);


    try {

        const response = await fetch(
            "/api/route",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body:
                    JSON.stringify(requestData)
            }
        );


        const data =
            await response.json();


        if (!response.ok || !data.success) {

            showError(
                data.error ||
                "Unable to calculate the route."
            );

            return;
        }


        displayResults(
            data,
            origin,
            destination
        );


    } catch (error) {

        console.error(error);

        showError(
            "Unable to connect to the routing service."
        );

    } finally {

        setLoading(false);

    }

});


// ============================================
// DISPLAY RESULTS
// ============================================

function displayResults(
    data,
    origin,
    destination
) {

    emptyState.classList.add("hidden");
    errorState.classList.add("hidden");

    results.classList.remove("hidden");


    // Route title
    document.getElementById(
        "routeTitle"
    ).textContent =
        `${origin} → ${destination}`;


    document.getElementById(
        "routeSubtitle"
    ).textContent =
        "Your calculated route is ready.";


    // Route badge
    document.getElementById(
        "routeBadge"
    ).textContent =
        capitalize(data.route_type);


    // Unit
    const unitLabel =
        data.unit === "k"
            ? "km"
            : "mi";


    // Distance
    document.getElementById(
        "distanceValue"
    ).textContent =
        `${Number(data.distance).toFixed(1)} ${unitLabel}`;


    // Time
    document.getElementById(
        "timeValue"
    ).textContent =
        formatTravelTime(
            data.travel_time
        );


    // Steps
    document.getElementById(
        "stepValue"
    ).textContent =
        `${data.directions.length} steps`;


    document.getElementById(
        "stepCount"
    ).textContent =
        `${data.directions.length} total steps`;


    // Generate directions
    renderDirections(
        data.directions,
        unitLabel
    );


    // Re-render icons
    lucide.createIcons();

}


// ============================================
// DIRECTIONS
// ============================================

function renderDirections(
    directions,
    unitLabel
) {

    const container =
        document.getElementById(
            "directionsList"
        );


    container.innerHTML = "";


    directions.forEach(
        (step, index) => {

            const item =
                document.createElement("div");


            item.className =
                "direction-item";


            item.innerHTML = `

                <div class="step-indicator">

                    <div class="step-circle">
                        ${index + 1}
                    </div>

                </div>


                <div class="direction-text">

                    ${escapeHTML(
                        step.narrative
                    )}

                </div>


                <div class="direction-distance">

                    ${Number(
                        step.distance
                    ).toFixed(1)}
                    ${unitLabel}

                </div>

            `;


            container.appendChild(item);

        }
    );

}


// ============================================
// SWAP LOCATIONS
// ============================================

swapButton.addEventListener(
    "click",
    () => {

        const temp =
            originInput.value;

        originInput.value =
            destinationInput.value;

        destinationInput.value =
            temp;

        clearErrors();

    }
);


// ============================================
// CLEAR
// ============================================

clearButton.addEventListener(
    "click",
    () => {

        originInput.value = "";
        destinationInput.value = "";

        clearErrors();

        results.classList.add("hidden");
        errorState.classList.add("hidden");

        emptyState.classList.remove("hidden");

        originInput.focus();

    }
);


// ============================================
// TRY AGAIN
// ============================================

tryAgainButton.addEventListener(
    "click",
    () => {

        errorState.classList.add("hidden");

        emptyState.classList.remove("hidden");

        originInput.focus();

    }
);


// ============================================
// LOADING STATE
// ============================================

function setLoading(loading) {

    findRouteButton.disabled =
        loading;


    if (loading) {

        buttonContent.classList.add(
            "hidden"
        );

        loadingContent.classList.remove(
            "hidden"
        );

    } else {

        buttonContent.classList.remove(
            "hidden"
        );

        loadingContent.classList.add(
            "hidden"
        );

    }

}


// ============================================
// ERROR STATE
// ============================================

function showError(message) {

    emptyState.classList.add("hidden");
    results.classList.add("hidden");

    errorState.classList.remove("hidden");

    errorMessage.textContent =
        message;

}


// ============================================
// VALIDATION
// ============================================

function clearErrors() {

    document.getElementById(
        "originError"
    ).textContent = "";

    document.getElementById(
        "destinationError"
    ).textContent = "";

}


// ============================================
// FORMAT TRAVEL TIME
// ============================================

function formatTravelTime(time) {

    if (!time) {
        return "--";
    }


    const parts =
        time.split(":");


    if (parts.length !== 3) {
        return time;
    }


    const hours =
        parseInt(parts[0]);

    const minutes =
        parseInt(parts[1]);


    if (hours === 0) {
        return `${minutes} min`;
    }


    return `${hours} hr ${minutes} min`;

}


// ============================================
// CAPITALIZE
// ============================================

function capitalize(text) {

    if (!text) {
        return "";
    }


    return (
        text.charAt(0).toUpperCase()
        +
        text.slice(1)
    );

}


// ============================================
// BASIC HTML ESCAPING
// ============================================

function escapeHTML(text) {

    const div =
        document.createElement("div");

    div.textContent =
        text;

    return div.innerHTML;

}