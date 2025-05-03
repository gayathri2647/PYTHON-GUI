/**
 * Mental Health Tracker - Main Application
 * 
 * This file contains the core functionality of the Mental Health Tracker application.
 * It handles UI interactions, navigation, and coordinates with other modules.
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize the application
    initApp();
});

/**
 * Initialize the application
 */
function initApp() {
    // Set current date
    updateCurrentDate();
    
    // Initialize UI components
    initNavigation();
    initThemeToggle();
    initFormHandlers();
    initHistoryView();
    initCalendarView();
    
    // Check authentication status
    checkAuthStatus();
    
    // Show dashboard or auth section based on authentication
    showDashboard();
}

/**
 * Update the current date display
 */
function updateCurrentDate() {
    const currentDateElement = document.getElementById('current-date');
    if (currentDateElement) {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        currentDateElement.textContent = now.toLocaleDateString(undefined, options);
    }
}

/**
 * Initialize navigation between dashboard sections
 */
function initNavigation() {
    const navButtons = document.querySelectorAll('.nav-button');
    
    navButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons and sections
            navButtons.forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.dashboard-section').forEach(section => {
                section.classList.remove('active');
            });
            
            // Add active class to clicked button
            button.classList.add('active');
            
            // Show the corresponding section
            const targetSection = button.getAttribute('data-target');
            document.getElementById(targetSection).classList.add('active');
        });
    });
}

/**
 * Initialize theme toggle functionality
 */
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const themeStyle = document.getElementById('theme-style');
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    
    // Check if user has a theme preference in localStorage
    const darkMode = localStorage.getItem('darkMode') === 'true';
    
    // Apply theme based on preference
    if (darkMode) {
        themeStyle.href = 'css/dark-mode.css';
        if (darkModeToggle) darkModeToggle.checked = true;
    }
    
    // Theme toggle in header
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
    
    // Theme toggle in settings
    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', () => {
            toggleTheme();
        });
    }
}

/**
 * Toggle between light and dark theme
 */
function toggleTheme() {
    const themeStyle = document.getElementById('theme-style');
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    
    if (themeStyle.href.includes('dark-mode.css')) {
        themeStyle.href = '';
        localStorage.setItem('darkMode', 'false');
        if (darkModeToggle) darkModeToggle.checked = false;
    } else {
        themeStyle.href = 'css/dark-mode.css';
        localStorage.setItem('darkMode', 'true');
        if (darkModeToggle) darkModeToggle.checked = true;
    }
}

/**
 * Initialize form handlers
 */
function initFormHandlers() {
    const moodForm = document.getElementById('mood-form');
    
    if (moodForm) {
        moodForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Get form data
            const moodValue = document.querySelector('input[name="mood"]:checked')?.value;
            const symptomsElements = document.querySelectorAll('input[name="symptoms"]:checked');
            const symptoms = Array.from(symptomsElements).map(el => el.value);
            const notes = document.getElementById('notes').value;
            
            // Validate form
            if (!moodValue) {
                showNotification('Please select your mood', 'error');
                return;
            }
            
            // Create entry object
            const entry = {
                id: Date.now().toString(),
                date: new Date().toISOString(),
                mood: parseInt(moodValue),
                symptoms,
                notes
            };
            
            // Save entry
            saveEntry(entry);
            
            // Reset form
            moodForm.reset();
            
            // Show success notification
            showNotification('Your mood has been recorded!', 'success');
            
            // Update views
            updateMoodHistory();
            updateCalendarView();
            updateInsights();
        });
    }
}

/**
 * Initialize history view
 */
function initHistoryView() {
    // Set up view toggle
    const viewButtons = document.querySelectorAll('.view-button');
    const historyViews = document.querySelectorAll('.history-view');
    
    viewButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons and views
            viewButtons.forEach(btn => btn.classList.remove('active'));
            historyViews.forEach(view => view.classList.remove('active'));
            
            // Add active class to clicked button
            button.classList.add('active');
            
            // Show the corresponding view
            const targetView = button.getAttribute('data-view');
            document.getElementById(`${targetView}-view`).classList.add('active');
        });
    });
    
    // Set up history filter
    const historyFilter = document.getElementById('history-filter');
    if (historyFilter) {
        historyFilter.addEventListener('change', updateMoodHistory);
    }
    
    // Initial load of history
    updateMoodHistory();
}

/**
 * Update mood history display
 */
function updateMoodHistory() {
    const entriesContainer = document.getElementById('entries-container');
    const historyFilter = document.getElementById('history-filter');
    
    if (!entriesContainer) return;
    
    // Get entries from storage
    const entries = getEntries();
    
    // Apply filter
    let filteredEntries = [...entries];
    if (historyFilter) {
        const filterValue = historyFilter.value;
        const now = new Date();
        
        if (filterValue === 'week') {
            const weekAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
            filteredEntries = entries.filter(entry => new Date(entry.date) >= weekAgo);
        } else if (filterValue === 'month') {
            const monthAgo = new Date(now.getTime() - 30 * 24 * 60 * 60 * 1000);
            filteredEntries = entries.filter(entry => new Date(entry.date) >= monthAgo);
        } else if (filterValue === 'year') {
            const yearAgo = new Date(now.getTime() - 365 * 24 * 60 * 60 * 1000);
            filteredEntries = entries.filter(entry => new Date(entry.date) >= yearAgo);
        }
    }
    
    // Sort entries by date (newest first)
    filteredEntries.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    // Clear container
    entriesContainer.innerHTML = '';
    
    // Show message if no entries
    if (filteredEntries.length === 0) {
        entriesContainer.innerHTML = '<div class="no-entries-message">No entries found for this period.</div>';
        return;
    }
    
    // Create entry cards
    filteredEntries.forEach(entry => {
        const entryCard = createEntryCard(entry);
        entriesContainer.appendChild(entryCard);
    });
}

/**
 * Create an entry card element
 * @param {Object} entry - The entry object
 * @returns {HTMLElement} - The entry card element
 */
function createEntryCard(entry) {
    const entryCard = document.createElement('div');
    entryCard.className = 'entry-card';
    entryCard.dataset.id = entry.id;
    
    const date = new Date(entry.date);
    const formattedDate = date.toLocaleDateString(undefined, {
        weekday: 'short',
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
    
    // Map mood value to emoji
    const moodEmojis = ['😞', '🙁', '😐', '🙂', '😄'];
    const moodEmoji = moodEmojis[entry.mood - 1] || '😐';
    
    // Create entry header
    const entryHeader = document.createElement('div');
    entryHeader.className = 'entry-header';
    
    const entryDate = document.createElement('div');
    entryDate.className = 'entry-date';
    entryDate.textContent = formattedDate;
    
    const entryMood = document.createElement('div');
    entryMood.className = 'entry-mood';
    entryMood.textContent = moodEmoji;
    
    entryHeader.appendChild(entryDate);
    entryHeader.appendChild(entryMood);
    entryCard.appendChild(entryHeader);
    
    // Create symptoms tags if any
    if (entry.symptoms && entry.symptoms.length > 0) {
        const entrySymptoms = document.createElement('div');
        entrySymptoms.className = 'entry-symptoms';
        
        entry.symptoms.forEach(symptom => {
            const symptomTag = document.createElement('span');
            symptomTag.className = 'symptom-tag';
            symptomTag.textContent = symptom;
            entrySymptoms.appendChild(symptomTag);
        });
        
        entryCard.appendChild(entrySymptoms);
    }
    
    // Create notes if any
    if (entry.notes) {
        const entryNotes = document.createElement('div');
        entryNotes.className = 'entry-notes';
        entryNotes.textContent = entry.notes;
        entryCard.appendChild(entryNotes);
    }
    
    return entryCard;
}

/**
 * Initialize calendar view
 */
function initCalendarView() {
    const prevMonthBtn = document.getElementById('prev-month');
    const nextMonthBtn = document.getElementById('next-month');
    const calendarMonth = document.getElementById('calendar-month');
    
    // Set current month and year
    let currentDate = new Date();
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();
    
    // Add event listeners for month navigation
    if (prevMonthBtn) {
        prevMonthBtn.addEventListener('click', () => {
            currentMonth--;
            if (currentMonth < 0) {
                currentMonth = 11;
                currentYear--;
            }
            updateCalendarView(currentYear, currentMonth);
        });
    }
    
    if (nextMonthBtn) {
        nextMonthBtn.addEventListener('click', () => {
            currentMonth++;
            if (currentMonth > 11) {
                currentMonth = 0;
                currentYear++;
            }
            updateCalendarView(currentYear, currentMonth);
        });
    }
    
    // Initial calendar update
    updateCalendarView(currentYear, currentMonth);
}

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


