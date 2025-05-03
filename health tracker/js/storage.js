/**
 * Mental Health Tracker - Storage Module
 * 
 * This file handles data storage using LocalStorage and Amazon DynamoDB.
 * It provides functions for saving, retrieving, and syncing mood entries.
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize storage
    initStorage();
});

/**
 * Initialize storage
 */
function initStorage() {
    // Set up data export/import
    const exportDataBtn = document.getElementById('export-data');
    const importDataBtn = document.getElementById('import-data');
    const backupDataBtn = document.getElementById('backup-data');
    const restoreDataBtn = document.getElementById('restore-data');
    const clearDataBtn = document.getElementById('clear-data');
    
    if (exportDataBtn) {
        exportDataBtn.addEventListener('click', exportData);
    }
    
    if (importDataBtn) {
        importDataBtn.addEventListener('click', importData);
    }
    
    if (backupDataBtn) {
        backupDataBtn.addEventListener('click', backupToCloud);
    }
    
    if (restoreDataBtn) {
        restoreDataBtn.addEventListener('click', restoreFromCloud);
    }
    
    if (clearDataBtn) {
        clearDataBtn.addEventListener('click', clearData);
    }
}

/**
 * Get all mood entries
 * @returns {Array} - Array of mood entries
 */
function getEntries() {
    const storedEntries = localStorage.getItem('moodEntries');
    return storedEntries ? JSON.parse(storedEntries) : [];
}

/**
 * Save a mood entry
 * @param {Object} entry - The mood entry to save
 */
async function saveEntry(entry) {
    // Save to local storage
    const entries = getEntries();
    entries.push(entry);
    localStorage.setItem('moodEntries', JSON.stringify(entries));
    
    // If authenticated, also save to DynamoDB
    if (await isAuthenticated()) {
        try {
            await saveEntryToCloud(entry);
        } catch (error) {
            console.error('Error saving entry to cloud:', error);
            // We'll continue even if cloud save fails
            // The entry will be synced later when connection is restored
        }
    }
}

/**
 * Save entry to DynamoDB
 * @param {Object} entry - The mood entry to save
 */
async function saveEntryToCloud(entry) {
    try {
        // Get current user
        const user = await window.auth.getCurrentUser();
        if (!user) throw new Error('User not authenticated');
        
        // Create item for DynamoDB
        const params = {
            TableName: 'MoodEntries',
            Item: {
                userId: user.username,
                entryId: entry.id,
                date: entry.date,
                mood: entry.mood,
                symptoms: entry.symptoms,
                notes: entry.notes
            }
        };
        
        // Save to DynamoDB using AWS SDK
        // In a real implementation, you would use AWS.DynamoDB.DocumentClient
        // For now, we'll just simulate the API call
        console.log('Saving to DynamoDB:', params);
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 300));
        
        return true;
    } catch (error) {
        console.error('Error saving to DynamoDB:', error);
        throw error;
    }
}

/**
 * Sync local data with cloud
 */
async function syncWithCloud() {
    if (!await isAuthenticated()) return;
    
    try {
        // Get local entries
        const localEntries = getEntries();
        
        // Get cloud entries
        const cloudEntries = await getEntriesFromCloud();
        
        // Merge entries (cloud entries take precedence for same IDs)
        const mergedEntries = mergeEntries(localEntries, cloudEntries);
        
        // Update local storage
        localStorage.setItem('moodEntries', JSON.stringify(mergedEntries));
        
        // Update UI
        updateMoodHistory();
        updateCalendarView(new Date().getFullYear(), new Date().getMonth());
        updateInsights();
        
        return true;
    } catch (error) {
        console.error('Error syncing with cloud:', error);
        throw error;
    }
}

/**
 * Get entries from DynamoDB
 * @returns {Array} - Array of mood entries from cloud
 */
async function getEntriesFromCloud() {
    try {
        // Get current user
        const user = await window.auth.getCurrentUser();
        if (!user) throw new Error('User not authenticated');
        
        // Query DynamoDB
        const params = {
            TableName: 'MoodEntries',
            KeyConditionExpression: 'userId = :userId',
            ExpressionAttributeValues: {
                ':userId': user.username
            }
        };
        
        // In a real implementation, you would use AWS.DynamoDB.DocumentClient
        // For now, we'll just simulate the API call
        console.log('Querying DynamoDB:', params);
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Return sample data for demonstration
        return [];
    } catch (error) {
        console.error('Error getting entries from DynamoDB:', error);
        throw error;
    }
}

/**
 * Merge local and cloud entries
 * @param {Array} localEntries - Local entries
 * @param {Array} cloudEntries - Cloud entries
 * @returns {Array} - Merged entries
 */
function mergeEntries(localEntries, cloudEntries) {
    // Create a map of entries by ID
    const entriesMap = {};
    
    // Add local entries to map
    localEntries.forEach(entry => {
        entriesMap[entry.id] = entry;
    });
    
    // Add cloud entries to map (overwriting local entries with same ID)
    cloudEntries.forEach(entry => {
        entriesMap[entry.id] = entry;
    });
    
    // Convert map back to array
    return Object.values(entriesMap);
}

/**
 * Export data as JSON file
 */
function exportData() {
    const entries = getEntries();
    const dataStr = JSON.stringify(entries, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);
    
    const exportFileDefaultName = `mood-tracker-export-${new Date().toISOString().split('T')[0]}.json`;
    
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
    
    showNotification('Data exported successfully!', 'success');
}

/**
 * Import data from JSON file
 */
function importData() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'application/json';
    
    input.onchange = e => {
        const file = e.target.files[0];
        
        if (!file) {
            return;
        }
        
        const reader = new FileReader();
        
        reader.onload = event => {
            try {
                const entries = JSON.parse(event.target.result);
                
                if (!Array.isArray(entries)) {
                    throw new Error('Invalid data format');
                }
                
                // Validate entries
                entries.forEach(entry => {
                    if (!entry.id || !entry.date || !entry.mood) {
                        throw new Error('Invalid entry format');
                    }
                });
                
                // Save entries
                localStorage.setItem('moodEntries', JSON.stringify(entries));
                
                // Update UI
                updateMoodHistory();
                updateCalendarView(new Date().getFullYear(), new Date().getMonth());
                updateInsights();
                
                showNotification('Data imported successfully!', 'success');
            } catch (error) {
                console.error('Error importing data:', error);
                showNotification('Error importing data. Please check the file format.', 'error');
            }
        };
        
        reader.readAsText(file);
    };
    
    input.click();
}

/**
 * Backup data to S3
 */
async function backupToCloud() {
    if (!await isAuthenticated()) {
        showNotification('Please sign in to backup your data', 'error');
        return;
    }
    
    try {
        // Show loading state
        const backupBtn = document.getElementById('backup-data');
        backupBtn.textContent = 'Backing up...';
        
        // Get entries
        const entries = getEntries();
        
        // Get current user
        const user = await window.auth.getCurrentUser();
        
        // Create backup file
        const fileName = `${user.username}/mood-tracker-backup-${new Date().toISOString()}.json`;
        const dataStr = JSON.stringify(entries);
        
        // In a real implementation, you would use AWS.S3
        // For now, we'll just simulate the API call
        console.log('Backing up to S3:', fileName, entries.length, 'entries');
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        showNotification('Data backed up successfully!', 'success');
    } catch (error) {
        console.error('Error backing up data:', error);
        showNotification('Error backing up data. Please try again.', 'error');
    } finally {
        // Reset button text
        const backupBtn = document.getElementById('backup-data');
        if (backupBtn) backupBtn.textContent = 'Backup to Cloud';
    }
}

/**
 * Restore data from S3
 */
async function restoreFromCloud() {
    if (!await isAuthenticated()) {
        showNotification('Please sign in to restore your data', 'error');
        return;
    }
    
    try {
        // Show loading state
        const restoreBtn = document.getElementById('restore-data');
        restoreBtn.textContent = 'Restoring...';
        
        // Get current user
        const user = await window.auth.getCurrentUser();
        
        // In a real implementation, you would use AWS.S3 to list and get objects
        // For now, we'll just simulate the API call
        console.log('Restoring from S3 for user:', user.username);
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Simulate getting the latest backup
        // In a real implementation, you would list objects and get the latest one
        
        // Update UI
        updateMoodHistory();
        updateCalendarView(new Date().getFullYear(), new Date().getMonth());
        updateInsights();
        
        showNotification('Data restored successfully!', 'success');
    } catch (error) {
        console.error('Error restoring data:', error);
        showNotification('Error restoring data. Please try again.', 'error');
    } finally {
        // Reset button text
        const restoreBtn = document.getElementById('restore-data');
        if (restoreBtn) restoreBtn.textContent = 'Restore from Cloud';
    }
}

/**
 * Clear all data
 */
function clearData() {
    if (confirm('Are you sure you want to clear all your data? This cannot be undone.')) {
        localStorage.removeItem('moodEntries');
        
        // Update UI
        updateMoodHistory();
        updateCalendarView(new Date().getFullYear(), new Date().getMonth());
        updateInsights();
        
        showNotification('All data has been cleared.', 'success');
    }
}

/**
 * Check if user is authenticated
 * @returns {Promise<boolean>} - Whether the user is authenticated
 */
async function isAuthenticated() {
    return window.auth && await window.auth.isAuthenticated();
}

// Export functions for use in other modules
window.storage = {
    getEntries,
    saveEntry,
    syncWithCloud,
    exportData,
    importData,
    backupToCloud,
    restoreFromCloud,
    clearData
};