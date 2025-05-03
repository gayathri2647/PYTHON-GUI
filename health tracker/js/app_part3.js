/**
 * Update calendar view
 * @param {number} year - The year to display
 * @param {number} month - The month to display (0-11)
 */
function updateCalendarView(year, month) {
    const calendarGrid = document.querySelector('.calendar-grid');
    const calendarMonth = document.getElementById('calendar-month');
    
    if (!calendarGrid || !calendarMonth) return;
    
    // Clear grid
    calendarGrid.innerHTML = '';
    
    // Update month and year display
    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December'];
    calendarMonth.textContent = `${monthNames[month]} ${year}`;
    
    // Get entries from storage
    const entries = getEntries();
    
    // Create map of dates with entries
    const entryDates = {};
    entries.forEach(entry => {
        const date = new Date(entry.date);
        const dateKey = `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`;
        entryDates[dateKey] = entry.mood;
    });
    
    // Get first day of month and number of days
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    
    // Add day headers
    const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    dayNames.forEach(day => {
        const dayHeader = document.createElement('div');
        dayHeader.className = 'calendar-day-header';
        dayHeader.textContent = day;
        calendarGrid.appendChild(dayHeader);
    });
    
    // Add empty cells for days before first day of month
    for (let i = 0; i < firstDay; i++) {
        const emptyDay = document.createElement('div');
        emptyDay.className = 'calendar-day empty';
        calendarGrid.appendChild(emptyDay);
    }
    
    // Add days of month
    for (let i = 1; i <= daysInMonth; i++) {
        const dayCell = document.createElement('div');
        dayCell.className = 'calendar-day';
        
        // Check if this is today
        const today = new Date();
        if (year === today.getFullYear() && month === today.getMonth() && i === today.getDate()) {
            dayCell.classList.add('today');
        }
        
        // Check if there's an entry for this day
        const dateKey = `${year}-${month}-${i}`;
        if (entryDates[dateKey] !== undefined) {
            dayCell.classList.add('has-entry');
            
            // Add mood emoji
            const moodEmojis = ['😞', '🙁', '😐', '🙂', '😄'];
            const dayMood = document.createElement('div');
            dayMood.className = 'day-mood';
            dayMood.textContent = moodEmojis[entryDates[dateKey] - 1] || '😐';
            dayCell.appendChild(dayMood);
        }
        
        // Add day number
        const dayNumber = document.createElement('div');
        dayNumber.className = 'day-number';
        dayNumber.textContent = i;
        dayCell.appendChild(dayNumber);
        
        // Add click event to show entry for this day
        dayCell.addEventListener('click', () => {
            // TODO: Show entry details for this day
        });
        
        calendarGrid.appendChild(dayCell);
    }
}

/**
 * Update insights based on mood data
 */
function updateInsights() {
    // Get entries from storage
    const entries = getEntries();
    
    // Update mood chart
    updateMoodChart(entries);
    
    // Update streak count
    updateStreakCount(entries);
    
    // Update AI insights if authenticated
    if (isAuthenticated()) {
        updateAIInsights(entries);
    }
}

/**
 * Update mood chart visualization
 * @param {Array} entries - The mood entries
 */
function updateMoodChart(entries) {
    const chartCanvas = document.getElementById('mood-chart');
    if (!chartCanvas || entries.length === 0) return;
    
    // Get last 14 days of entries
    const now = new Date();
    const twoWeeksAgo = new Date(now.getTime() - 14 * 24 * 60 * 60 * 1000);
    
    // Create a map of dates for the last 14 days
    const dateLabels = [];
    const moodData = [];
    
    for (let i = 13; i >= 0; i--) {
        const date = new Date(now.getTime() - i * 24 * 60 * 60 * 1000);
        const dateStr = date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
        dateLabels.push(dateStr);
        
        // Find entry for this date
        const entry = entries.find(e => {
            const entryDate = new Date(e.date);
            return entryDate.getDate() === date.getDate() && 
                   entryDate.getMonth() === date.getMonth() && 
                   entryDate.getFullYear() === date.getFullYear();
        });
        
        moodData.push(entry ? entry.mood : null);
    }
    
    // Create chart
    if (window.moodChart) {
        window.moodChart.destroy();
    }
    
    window.moodChart = new Chart(chartCanvas, {
        type: 'line',
        data: {
            labels: dateLabels,
            datasets: [{
                label: 'Mood',
                data: moodData,
                borderColor: '#4a90e2',
                backgroundColor: 'rgba(74, 144, 226, 0.1)',
                borderWidth: 2,
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    min: 1,
                    max: 5,
                    ticks: {
                        stepSize: 1,
                        callback: function(value) {
                            const labels = ['Terrible', 'Bad', 'Okay', 'Good', 'Great'];
                            return labels[value - 1] || '';
                        }
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const labels = ['Terrible', 'Bad', 'Okay', 'Good', 'Great'];
                            const value = context.raw;
                            return value ? labels[value - 1] : 'No entry';
                        }
                    }
                }
            }
        }
    });
}

/**
 * Update streak count
 * @param {Array} entries - The mood entries
 */
function updateStreakCount(entries) {
    const streakCountElement = document.querySelector('.streak-count');
    if (!streakCountElement) return;
    
    // Calculate streak
    let streak = 0;
    const now = new Date();
    now.setHours(0, 0, 0, 0);
    
    // Check if there's an entry for today
    const todayEntry = entries.find(entry => {
        const entryDate = new Date(entry.date);
        entryDate.setHours(0, 0, 0, 0);
        return entryDate.getTime() === now.getTime();
    });
    
    if (todayEntry) {
        streak = 1;
        
        // Check previous days
        let currentDate = new Date(now);
        currentDate.setDate(currentDate.getDate() - 1);
        
        while (true) {
            const dateEntry = entries.find(entry => {
                const entryDate = new Date(entry.date);
                entryDate.setHours(0, 0, 0, 0);
                return entryDate.getTime() === currentDate.getTime();
            });
            
            if (dateEntry) {
                streak++;
                currentDate.setDate(currentDate.getDate() - 1);
            } else {
                break;
            }
        }
    }
    
    streakCountElement.textContent = streak;
}

/**
 * Show notification
 * @param {string} message - The notification message
 * @param {string} type - The notification type (success, error)
 */
function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    const notificationMessage = document.getElementById('notification-message');
    
    if (!notification || !notificationMessage) return;
    
    // Set message and type
    notificationMessage.textContent = message;
    notification.className = `notification ${type}`;
    
    // Show notification
    notification.classList.add('show');
    
    // Hide after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

/**
 * Check authentication status
 */
function checkAuthStatus() {
    // This will be implemented in auth.js
    // For now, we'll just return false
    return false;
}

/**
 * Show dashboard or auth section based on authentication
 */
function showDashboard() {
    const dashboard = document.getElementById('dashboard');
    const authSection = document.getElementById('auth-section');
    const loginButton = document.getElementById('login-button');
    const userProfile = document.getElementById('user-profile');
    
    // For now, we'll show the dashboard without authentication
    if (dashboard) dashboard.classList.remove('hidden');
    if (authSection) authSection.classList.add('hidden');
    
    // Update login/profile visibility
    if (loginButton) loginButton.classList.remove('hidden');
    if (userProfile) userProfile.classList.add('hidden');
}

/**
 * Check if user is authenticated
 * @returns {boolean} - Whether the user is authenticated
 */
function isAuthenticated() {
    // This will be implemented in auth.js
    // For now, we'll just return false
    return false;
}

/**
 * Get entries from storage
 * @returns {Array} - The mood entries
 */
function getEntries() {
    // This will be implemented in storage.js
    // For now, we'll just return an empty array or sample data
    const storedEntries = localStorage.getItem('moodEntries');
    return storedEntries ? JSON.parse(storedEntries) : [];
}

/**
 * Save entry to storage
 * @param {Object} entry - The entry to save
 */
function saveEntry(entry) {
    // This will be implemented in storage.js
    // For now, we'll just save to localStorage
    const entries = getEntries();
    entries.push(entry);
    localStorage.setItem('moodEntries', JSON.stringify(entries));
}

/**
 * Update AI insights
 * @param {Array} entries - The mood entries
 */
function updateAIInsights(entries) {
    // This will be implemented in insights.js
    // For now, we'll just show a placeholder
    const aiInsights = document.getElementById('ai-insights');
    if (!aiInsights) return;
    
    if (!isAuthenticated()) {
        aiInsights.innerHTML = '<p class="login-required-message">Sign in to get AI-powered insights about your mood patterns.</p>';
        return;
    }
    
    // Placeholder for AI insights
    aiInsights.innerHTML = '<p>Analyzing your mood patterns...</p>';
}