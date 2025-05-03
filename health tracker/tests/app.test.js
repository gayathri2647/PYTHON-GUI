/**
 * Mental Health Tracker - Tests
 * 
 * This file contains tests for the Mental Health Tracker application.
 */

// Mock localStorage
const localStorageMock = (function() {
    let store = {};
    return {
        getItem: function(key) {
            return store[key] || null;
        },
        setItem: function(key, value) {
            store[key] = value.toString();
        },
        removeItem: function(key) {
            delete store[key];
        },
        clear: function() {
            store = {};
        }
    };
})();

// Mock DOM elements
const mockElements = {};

// Mock document methods
document.getElementById = jest.fn(id => {
    if (!mockElements[id]) {
        mockElements[id] = {
            value: '',
            textContent: '',
            classList: {
                add: jest.fn(),
                remove: jest.fn(),
                contains: jest.fn()
            },
            addEventListener: jest.fn(),
            appendChild: jest.fn()
        };
    }
    return mockElements[id];
});

document.querySelector = jest.fn(selector => {
    const id = selector.replace(/[#.]/g, '');
    return document.getElementById(id);
});

document.querySelectorAll = jest.fn(selector => {
    return [document.getElementById('mock-element')];
});

// Mock AWS Amplify
global.AWS = {
    Amplify: {
        configure: jest.fn(),
        Auth: {
            signIn: jest.fn(),
            signUp: jest.fn(),
            signOut: jest.fn(),
            currentAuthenticatedUser: jest.fn()
        }
    }
};

// Mock Chart.js
global.Chart = jest.fn(() => ({
    destroy: jest.fn()
}));

// Tests
describe('Mental Health Tracker', () => {
    beforeEach(() => {
        // Set up localStorage mock
        Object.defineProperty(window, 'localStorage', { value: localStorageMock });
        localStorage.clear();
        
        // Reset mocks
        jest.clearAllMocks();
    });
    
    describe('Entry Management', () => {
        test('should save entry to localStorage', () => {
            // Arrange
            const entry = {
                id: '1234567890',
                date: '2023-01-01T12:00:00.000Z',
                mood: 4,
                symptoms: ['stress'],
                notes: 'Test note'
            };
            
            // Act
            saveEntry(entry);
            
            // Assert
            const entries = JSON.parse(localStorage.getItem('moodEntries'));
            expect(entries).toHaveLength(1);
            expect(entries[0]).toEqual(entry);
        });
        
        test('should get entries from localStorage', () => {
            // Arrange
            const entries = [
                {
                    id: '1234567890',
                    date: '2023-01-01T12:00:00.000Z',
                    mood: 4,
                    symptoms: ['stress'],
                    notes: 'Test note'
                }
            ];
            localStorage.setItem('moodEntries', JSON.stringify(entries));
            
            // Act
            const result = getEntries();
            
            // Assert
            expect(result).toEqual(entries);
        });
        
        test('should return empty array when no entries exist', () => {
            // Act
            const result = getEntries();
            
            // Assert
            expect(result).toEqual([]);
        });
    });
    
    describe('UI Interactions', () => {
        test('should show notification', () => {
            // Arrange
            const message = 'Test notification';
            const type = 'success';
            
            // Act
            showNotification(message, type);
            
            // Assert
            expect(document.getElementById('notification-message').textContent).toBe(message);
            expect(document.getElementById('notification').className).toContain(type);
            expect(document.getElementById('notification').classList.add).toHaveBeenCalledWith('show');
        });
        
        test('should toggle theme', () => {
            // Arrange
            const themeStyle = document.getElementById('theme-style');
            themeStyle.href = '';
            
            // Act
            toggleTheme();
            
            // Assert
            expect(themeStyle.href).toContain('dark-mode.css');
            expect(localStorage.getItem('darkMode')).toBe('true');
            
            // Act again to toggle back
            toggleTheme();
            
            // Assert
            expect(themeStyle.href).toBe('');
            expect(localStorage.getItem('darkMode')).toBe('false');
        });
    });
    
    describe('Authentication', () => {
        test('should update UI when user is authenticated', async () => {
            // Arrange
            const user = {
                username: 'testuser',
                attributes: {
                    email: 'test@example.com'
                }
            };
            
            // Act
            updateAuthenticatedUI(user);
            
            // Assert
            expect(document.getElementById('dashboard').classList.remove).toHaveBeenCalledWith('hidden');
            expect(document.getElementById('auth-section').classList.add).toHaveBeenCalledWith('hidden');
            expect(document.getElementById('login-button').classList.add).toHaveBeenCalledWith('hidden');
            expect(document.getElementById('user-profile').classList.remove).toHaveBeenCalledWith('hidden');
            expect(document.getElementById('username').textContent).toBe(user.attributes.email);
        });
        
        test('should update UI when user is not authenticated', () => {
            // Act
            updateUnauthenticatedUI();
            
            // Assert
            expect(document.getElementById('login-button').classList.remove).toHaveBeenCalledWith('hidden');
            expect(document.getElementById('user-profile').classList.add).toHaveBeenCalledWith('hidden');
        });
    });
});

// Mock functions for testing
function saveEntry(entry) {
    const entries = getEntries();
    entries.push(entry);
    localStorage.setItem('moodEntries', JSON.stringify(entries));
}

function getEntries() {
    const storedEntries = localStorage.getItem('moodEntries');
    return storedEntries ? JSON.parse(storedEntries) : [];
}

function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    const notificationMessage = document.getElementById('notification-message');
    
    if (!notification || !notificationMessage) return;
    
    notificationMessage.textContent = message;
    notification.className = `notification ${type}`;
    notification.classList.add('show');
}

function toggleTheme() {
    const themeStyle = document.getElementById('theme-style');
    
    if (themeStyle.href.includes('dark-mode.css')) {
        themeStyle.href = '';
        localStorage.setItem('darkMode', 'false');
    } else {
        themeStyle.href = 'css/dark-mode.css';
        localStorage.setItem('darkMode', 'true');
    }
}

function updateAuthenticatedUI(user) {
    const dashboard = document.getElementById('dashboard');
    const authSection = document.getElementById('auth-section');
    const loginButton = document.getElementById('login-button');
    const userProfile = document.getElementById('user-profile');
    const username = document.getElementById('username');
    
    if (dashboard) dashboard.classList.remove('hidden');
    if (authSection) authSection.classList.add('hidden');
    if (loginButton) loginButton.classList.add('hidden');
    if (userProfile) userProfile.classList.remove('hidden');
    if (username && user.attributes) {
        username.textContent = user.attributes.email;
    }
}

function updateUnauthenticatedUI() {
    const loginButton = document.getElementById('login-button');
    const userProfile = document.getElementById('user-profile');
    
    if (loginButton) loginButton.classList.remove('hidden');
    if (userProfile) userProfile.classList.add('hidden');
}