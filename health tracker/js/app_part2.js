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