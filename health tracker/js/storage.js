
// Updated storage.js - S3-based backup/restore without authentication

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    initStorage();
});

function initStorage() {
    const exportDataBtn = document.getElementById('export-data');
    const importDataBtn = document.getElementById('import-data');
    const backupDataBtn = document.getElementById('backup-data');
    const restoreDataBtn = document.getElementById('restore-data');
    const clearDataBtn = document.getElementById('clear-data');

    if (exportDataBtn) exportDataBtn.addEventListener('click', exportData);
    if (importDataBtn) importDataBtn.addEventListener('click', importData);
    if (backupDataBtn) backupDataBtn.addEventListener('click', backupToCloud);
    if (restoreDataBtn) restoreDataBtn.addEventListener('click', restoreFromCloud);
    if (clearDataBtn) clearDataBtn.addEventListener('click', clearData);
}

function getEntries() {
    const storedEntries = localStorage.getItem('moodEntries');
    return storedEntries ? JSON.parse(storedEntries) : [];
}

async function saveEntry(entry) {
    const entries = getEntries();
    entries.push(entry);
    localStorage.setItem('moodEntries', JSON.stringify(entries));
}

function exportData() {
    const entries = getEntries();
    const dataStr = JSON.stringify(entries, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);
    const exportFileName = `mood-tracker-export-${new Date().toISOString().split('T')[0]}.json`;

    const link = document.createElement('a');
    link.setAttribute('href', dataUri);
    link.setAttribute('download', exportFileName);
    link.click();

    showNotification('Data exported successfully!', 'success');
}

function importData() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'application/json';
    input.onchange = e => {
        const file = e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = event => {
            try {
                const entries = JSON.parse(event.target.result);
                if (!Array.isArray(entries)) throw new Error('Invalid data format');
                entries.forEach(entry => {
                    if (!entry.id || !entry.date || !entry.mood) {
                        throw new Error('Invalid entry format');
                    }
                });
                localStorage.setItem('moodEntries', JSON.stringify(entries));
                updateMoodHistory();
                updateCalendarView(new Date().getFullYear(), new Date().getMonth());
                updateInsights();
                showNotification('Data imported successfully!', 'success');
            } catch (error) {
                console.error('Import error:', error);
                showNotification('Error importing data. Invalid file.', 'error');
            }
        };
        reader.readAsText(file);
    };
    input.click();
}

async function backupToCloud() {
    const entries = getEntries();
    const fileName = `guest/mood-tracker-backup.json`;
    const blob = new Blob([JSON.stringify(entries)], { type: 'application/json' });

    try {
        const result = await fetchPresignedUrl('PUT', fileName);
        await fetch(result.url, { method: 'PUT', body: blob });
        showNotification('Data backed up successfully!', 'success');
    } catch (error) {
        console.error('Backup error:', error);
        showNotification('Backup failed. Try again later.', 'error');
    }
}

async function restoreFromCloud() {
    const fileName = `guest/mood-tracker-backup.json`;

    try {
        const result = await fetchPresignedUrl('GET', fileName);
        const response = await fetch(result.url);
        const entries = await response.json();

        localStorage.setItem('moodEntries', JSON.stringify(entries));
        updateMoodHistory();
        updateCalendarView(new Date().getFullYear(), new Date().getMonth());
        updateInsights();
        showNotification('Data restored successfully!', 'success');
    } catch (error) {
        console.error('Restore error:', error);
        showNotification('Restore failed. Backup may not exist.', 'error');
    }
}

async function fetchPresignedUrl(method, fileName) {
    const apiUrl = `https://your-vercel-project-name.vercel.app/api/presign?method=${method}&file=${encodeURIComponent(fileName)}`;
    const res = await fetch(apiUrl);
    if (!res.ok) throw new Error('Failed to get presigned URL');
    return await res.json();
}


function clearData() {
    if (confirm('Are you sure you want to clear all your data?')) {
        localStorage.removeItem('moodEntries');
        updateMoodHistory();
        updateCalendarView(new Date().getFullYear(), new Date().getMonth());
        updateInsights();
        showNotification('All data cleared.', 'success');
    }
}

window.storage = {
    getEntries,
    saveEntry,
    exportData,
    importData,
    backupToCloud,
    restoreFromCloud,
    clearData
};
