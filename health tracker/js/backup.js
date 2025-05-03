/**
 * Mental Health Tracker - Backup Module
 * 
 * This file handles data backup and restore using Amazon S3.
 * It provides functions for backing up and restoring mood entries.
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize backup functionality
    initBackup();
});

/**
 * Initialize backup functionality
 */
function initBackup() {
    // Set up backup/restore buttons
    const backupBtn = document.getElementById('backup-data');
    const restoreBtn = document.getElementById('restore-data');
    
    if (backupBtn) {
        backupBtn.addEventListener('click', backupData);
    }
    
    if (restoreBtn) {
        restoreBtn.addEventListener('click', restoreData);
    }
}

/**
 * Backup data to S3
 */
async function backupData() {
    try {
        // Check if user is authenticated
        if (!await isAuthenticated()) {
            showNotification('Please sign in to backup your data', 'error');
            return;
        }
        
        // Show loading state
        const backupBtn = document.getElementById('backup-data');
        if (backupBtn) backupBtn.textContent = 'Backing up...';
        
        // Get entries
        const entries = getEntries();
        
        // Get current user
        const user = await window.auth.getCurrentUser();
        
        // Create backup file
        const timestamp = new Date().toISOString();
        const fileName = `${user.username}/mood-tracker-backup-${timestamp}.json`;
        const dataStr = JSON.stringify(entries);
        
        // Upload to S3
        await uploadToS3(fileName, dataStr);
        
        // Show success notification
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
async function restoreData() {
    try {
        // Check if user is authenticated
        if (!await isAuthenticated()) {
            showNotification('Please sign in to restore your data', 'error');
            return;
        }
        
        // Show loading state
        const restoreBtn = document.getElementById('restore-data');
        if (restoreBtn) restoreBtn.textContent = 'Restoring...';
        
        // Get current user
        const user = await window.auth.getCurrentUser();
        
        // Get list of backups
        const backups = await listBackups(user.username);
        
        if (backups.length === 0) {
            showNotification('No backups found. Create a backup first.', 'error');
            return;
        }
        
        // Get latest backup
        const latestBackup = backups[0];
        
        // Download backup
        const data = await downloadFromS3(latestBackup.key);
        
        // Parse backup data
        const entries = JSON.parse(data);
        
        // Validate entries
        if (!Array.isArray(entries)) {
            throw new Error('Invalid backup format');
        }
        
        // Confirm restore
        if (confirm(`Restore data from backup created on ${latestBackup.lastModified.toLocaleString()}? This will replace your current data.`)) {
            // Save entries to local storage
            localStorage.setItem('moodEntries', JSON.stringify(entries));
            
            // Update UI
            updateMoodHistory();
            updateCalendarView(new Date().getFullYear(), new Date().getMonth());
            updateInsights();
            
            showNotification('Data restored successfully!', 'success');
        }
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
 * Upload data to S3
 * @param {string} fileName - The file name
 * @param {string} data - The data to upload
 */
async function uploadToS3(fileName, data) {
    try {
        // In a real implementation, you would use AWS.S3
        // For now, we'll just simulate the API call
        console.log('Uploading to S3:', fileName, data.length, 'bytes');
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        return true;
    } catch (error) {
        console.error('Error uploading to S3:', error);
        throw error;
    }
}

/**
 * List backups in S3
 * @param {string} userId - The user ID
 * @returns {Array} - Array of backup objects
 */
async function listBackups(userId) {
    try {
        // In a real implementation, you would use AWS.S3
        // For now, we'll just simulate the API call
        console.log('Listing backups for user:', userId);
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Return sample data
        return [
            {
                key: `${userId}/mood-tracker-backup-2023-01-01T12:00:00.000Z.json`,
                lastModified: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000) // 7 days ago
            },
            {
                key: `${userId}/mood-tracker-backup-2023-01-02T12:00:00.000Z.json`,
                lastModified: new Date(Date.now() - 14 * 24 * 60 * 60 * 1000) // 14 days ago
            }
        ];
    } catch (error) {
        console.error('Error listing backups:', error);
        throw error;
    }
}

/**
 * Download data from S3
 * @param {string} key - The S3 object key
 * @returns {string} - The downloaded data
 */
async function downloadFromS3(key) {
    try {
        // In a real implementation, you would use AWS.S3
        // For now, we'll just simulate the API call
        console.log('Downloading from S3:', key);
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 800));
        
        // Return sample data
        return JSON.stringify([
            {
                id: '1234567890',
                date: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
                mood: 4,
                symptoms: ['stress'],
                notes: 'Had a good day despite some stress at work.'
            },
            {
                id: '0987654321',
                date: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString(),
                mood: 3,
                symptoms: ['fatigue'],
                notes: 'Feeling tired but otherwise okay.'
            }
        ]);
    } catch (error) {
        console.error('Error downloading from S3:', error);
        throw error;
    }
}

/**
 * Get entries from local storage
 * @returns {Array} - Array of mood entries
 */
function getEntries() {
    const storedEntries = localStorage.getItem('moodEntries');
    return storedEntries ? JSON.parse(storedEntries) : [];
}

/**
 * Check if user is authenticated
 * @returns {Promise<boolean>} - Whether the user is authenticated
 */
async function isAuthenticated() {
    return window.auth && await window.auth.isAuthenticated();
}

// Export functions for use in other modules
window.backup = {
    backupData,
    restoreData
};