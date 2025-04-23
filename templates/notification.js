

// Check if the browser supports notifications
if ("Notification" in window) {
  // Request permission from the user
  Notification.requestPermission().then(permission => {
    if (permission === "granted") {
      // Create and show a notification
      const notification = new Notification("Hello!", {
        body: "This is a web notification demo.",
        icon: "https://via.placeholder.com/100" // Replace with your desired icon URL
      });

      // Add an event listener for when the notification is clicked
      notification.onclick = () => {
        window.open("https://yourwebsite.com"); // Redirect to a website on click
      };
    } else {
      console.log("Notification permission denied.");
    }
  });
} else {
  console.log("Notifications are not supported by your browser.");
}