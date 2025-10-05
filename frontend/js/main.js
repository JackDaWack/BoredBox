document.addEventListener('DOMContentLoaded', () => {
    // Example: Fetch a random activity from the Bored API and display it
    const activityBtn = document.getElementById('get-activity');
    const activityDisplay = document.getElementById('activity-display');

    activityBtn.addEventListener('click', async () => {
        try {
            const response = await fetch('https://www.boredapi.com/api/activity/');
            const data = await response.json();
            activityDisplay.textContent = data.activity;
        } catch (error) {
            activityDisplay.textContent = 'Failed to fetch activity.';
        }
    });
});