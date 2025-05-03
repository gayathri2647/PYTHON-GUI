/**
 * Mental Health Tracker - Authentication Module
 * 
 * This file handles user authentication using Amazon Cognito.
 * It provides functions for user sign-up, sign-in, and sign-out.
 */

// AWS Cognito configuration
const awsConfig = {
    Auth: {
        // These would be your actual Cognito User Pool details in production
        region: 'us-east-1',
        userPoolId: 'us-east-1_xxxxxxxxx',
        userPoolWebClientId: 'xxxxxxxxxxxxxxxxxxxxxxxxxx',
        mandatorySignIn: false,
        authenticationFlowType: 'USER_PASSWORD_AUTH'
    }
};

// Initialize AWS Amplify
try {
    AWS.Amplify.configure(awsConfig);
} catch (error) {
    console.error('Error initializing AWS Amplify:', error);
}

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize authentication UI
    initAuthUI();
});

/**
 * Initialize authentication UI
 */
function initAuthUI() {
    // Set up auth tab switching
    const authTabs = document.querySelectorAll('.auth-tab');
    const authForms = document.querySelectorAll('.auth-form');
    const authLinks = document.querySelectorAll('.auth-link');
    
    // Tab switching
    authTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs and forms
            authTabs.forEach(t => t.classList.remove('active'));
            authForms.forEach(f => f.classList.remove('active'));
            
            // Add active class to clicked tab
            tab.classList.add('active');
            
            // Show the corresponding form
            const targetForm = tab.getAttribute('data-tab');
            document.getElementById(`${targetForm}-form`).classList.add('active');
        });
    });
    
    // Auth links (sign in/sign up)
    authLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            const action = link.getAttribute('data-action');
            if (action === 'show-signin') {
                document.querySelector('[data-tab="signin"]').click();
            } else if (action === 'show-signup') {
                document.querySelector('[data-tab="signup"]').click();
            }
        });
    });
    
    // Set up form submissions
    const signinForm = document.getElementById('signin-form');
    const signupForm = document.getElementById('signup-form');
    const loginButton = document.getElementById('login-button');
    const logoutButton = document.getElementById('logout-button');
    
    if (signinForm) {
        const signinButton = document.getElementById('signin-button');
        signinButton.addEventListener('click', handleSignIn);
    }
    
    if (signupForm) {
        const signupButton = document.getElementById('signup-button');
        signupButton.addEventListener('click', handleSignUp);
    }
    
    if (loginButton) {
        loginButton.addEventListener('click', showAuthSection);
    }
    
    if (logoutButton) {
        logoutButton.addEventListener('click', handleSignOut);
    }
    
    // Check if user is already signed in
    checkSession();
}

/**
 * Handle sign-in form submission
 */
async function handleSignIn() {
    const email = document.getElementById('signin-email').value;
    const password = document.getElementById('signin-password').value;
    
    // Validate form
    if (!email || !password) {
        showNotification('Please enter both email and password', 'error');
        return;
    }
    
    try {
        // Show loading state
        document.getElementById('signin-button').textContent = 'Signing in...';
        
        // Sign in with Cognito
        const user = await AWS.Amplify.Auth.signIn(email, password);
        
        // Update UI for authenticated user
        updateAuthenticatedUI(user);
        
        // Show success notification
        showNotification('Signed in successfully!', 'success');
        
        // Sync data from cloud
        syncDataFromCloud();
        
    } catch (error) {
        console.error('Error signing in:', error);
        showNotification(error.message || 'Error signing in. Please try again.', 'error');
    } finally {
        // Reset button text
        document.getElementById('signin-button').textContent = 'Sign In';
    }
}

/**
 * Handle sign-up form submission
 */
async function handleSignUp() {
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;
    const confirmPassword = document.getElementById('signup-confirm-password').value;
    
    // Validate form
    if (!email || !password) {
        showNotification('Please enter both email and password', 'error');
        return;
    }
    
    if (password !== confirmPassword) {
        showNotification('Passwords do not match', 'error');
        return;
    }
    
    try {
        // Show loading state
        document.getElementById('signup-button').textContent = 'Signing up...';
        
        // Sign up with Cognito
        const { user } = await AWS.Amplify.Auth.signUp({
            username: email,
            password,
            attributes: {
                email
            }
        });
        
        // Show success notification
        showNotification('Sign up successful! Please check your email for verification.', 'success');
        
        // Switch to sign-in tab
        document.querySelector('[data-tab="signin"]').click();
        
    } catch (error) {
        console.error('Error signing up:', error);
        showNotification(error.message || 'Error signing up. Please try again.', 'error');
    } finally {
        // Reset button text
        document.getElementById('signup-button').textContent = 'Sign Up';
    }
}

/**
 * Handle sign-out
 */
async function handleSignOut() {
    try {
        // Sign out from Cognito
        await AWS.Amplify.Auth.signOut();
        
        // Update UI for unauthenticated user
        updateUnauthenticatedUI();
        
        // Show success notification
        showNotification('Signed out successfully!', 'success');
        
    } catch (error) {
        console.error('Error signing out:', error);
        showNotification(error.message || 'Error signing out. Please try again.', 'error');
    }
}

/**
 * Check if user has an active session
 */
async function checkSession() {
    try {
        // Get current authenticated user
        const user = await AWS.Amplify.Auth.currentAuthenticatedUser();
        
        // Update UI for authenticated user
        updateAuthenticatedUI(user);
        
        // Sync data from cloud
        syncDataFromCloud();
        
    } catch (error) {
        // User is not authenticated, show unauthenticated UI
        updateUnauthenticatedUI();
    }
}

/**
 * Update UI for authenticated user
 * @param {Object} user - The authenticated user object
 */
function updateAuthenticatedUI(user) {
    const dashboard = document.getElementById('dashboard');
    const authSection = document.getElementById('auth-section');
    const loginButton = document.getElementById('login-button');
    const userProfile = document.getElementById('user-profile');
    const username = document.getElementById('username');
    const cloudOnlyElements = document.querySelectorAll('.cloud-only');
    
    // Show dashboard, hide auth section
    if (dashboard) dashboard.classList.remove('hidden');
    if (authSection) authSection.classList.add('hidden');
    
    // Update login/profile visibility
    if (loginButton) loginButton.classList.add('hidden');
    if (userProfile) userProfile.classList.remove('hidden');
    
    // Set username
    if (username && user.attributes) {
        username.textContent = user.attributes.email;
    }
    
    // Show cloud-only elements
    cloudOnlyElements.forEach(el => el.style.display = 'flex');
    
    // Update insights with AI data
    updateInsights();
}

/**
 * Update UI for unauthenticated user
 */
function updateUnauthenticatedUI() {
    const loginButton = document.getElementById('login-button');
    const userProfile = document.getElementById('user-profile');
    const cloudOnlyElements = document.querySelectorAll('.cloud-only');
    
    // Update login/profile visibility
    if (loginButton) loginButton.classList.remove('hidden');
    if (userProfile) userProfile.classList.add('hidden');
    
    // Hide cloud-only elements
    cloudOnlyElements.forEach(el => el.style.display = 'none');
    
    // Update insights without AI data
    updateInsights();
}

/**
 * Show authentication section
 */
function showAuthSection() {
    const dashboard = document.getElementById('dashboard');
    const authSection = document.getElementById('auth-section');
    
    if (dashboard) dashboard.classList.add('hidden');
    if (authSection) authSection.classList.remove('hidden');
}

/**
 * Sync data from cloud
 */
function syncDataFromCloud() {
    // This will be implemented in storage.js
    // For now, we'll just show a notification
    showNotification('Syncing data from cloud...', 'info');
    
    // Simulate sync delay
    setTimeout(() => {
        showNotification('Data synced successfully!', 'success');
    }, 1500);
}

/**
 * Check if user is authenticated
 * @returns {Promise<boolean>} - Whether the user is authenticated
 */
async function isUserAuthenticated() {
    try {
        await AWS.Amplify.Auth.currentAuthenticatedUser();
        return true;
    } catch (error) {
        return false;
    }
}

// Export functions for use in other modules
window.auth = {
    isAuthenticated: isUserAuthenticated,
    signOut: handleSignOut,
    getCurrentUser: async () => {
        try {
            return await AWS.Amplify.Auth.currentAuthenticatedUser();
        } catch (error) {
            return null;
        }
    }
};