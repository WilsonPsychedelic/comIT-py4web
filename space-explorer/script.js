// Step 1: Find the elements we want to work with
const launchBtn = document.getElementById("launch-btn");
const missionStatus = document.getElementById("mission-status");
const explorerName = document.getElementById("explorer-name");

// Step 2: Listen for a click on the button
launchBtn.addEventListener("click", function() {
    launchMission();
});

// Step 3: Define what happens when the button is clicked
function launchMission() {
  // Change the button text
launchBtn.textContent = "🛸 Mission Active!";
launchBtn.disabled = true;    //prevent clicking twice!

// Add text to the empty paragraph
missionStatus.textContent = "📡 Signal received. Destination: Return orbit.";

// Add a class (cleaner than inline styles!)
missionStatus.classList.add("status-active");
}

// Change the style of that paragraph
missionStatus.style.color = "#7effd4";
missionStatus.style.marginTop = "20px";
missionStatus.style.fontSize = "15px";

// Make the name editable on double-click
explorerName.addEventListener("dblclick", function() {

  const newName = prompt("Enter your explorer name:");

  if (newName) { // only update if they typed something
    explorerName.textContent = newName;
}

});