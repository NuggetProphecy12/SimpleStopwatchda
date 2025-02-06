let startTime;

function startStopwatch() {
    startTime = new Date();
    console.log("Stopwatch started.");
}

function stopStopwatch() {
    const endTime = new Date();
    const elapsed = (endTime - startTime) / 1000;
    console.log(`Elapsed time: ${elapsed} seconds`);
}

// Example usage:
startStopwatch();
setTimeout(stopStopwatch, 3000); // Stops after 3 seconds
