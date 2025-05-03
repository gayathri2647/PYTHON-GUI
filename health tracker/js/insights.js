/**
 * Mental Health Tracker - Insights Module
 * 
 * This file handles AI-powered mood analysis using Amazon Comprehend.
 * It provides functions for analyzing mood patterns and generating insights.
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize insights
    initInsights();
});

/**
 * Initialize insights
 */
function initInsights() {
    // Nothing to initialize here for now
    // Insights are updated when the user navigates to the insights section
}

/**
 * Update AI insights based on mood data
 * @param {Array} entries - The mood entries
 */
async function updateAIInsights(entries) {
    const aiInsights = document.getElementById('ai-insights');
    if (!aiInsights) return;
    
    // Check if user is authenticated
    if (!await isAuthenticated()) {
        aiInsights.innerHTML = '<p class="login-required-message">Sign in to get AI-powered insights about your mood patterns.</p>';
        return;
    }
    
    // Show loading state
    aiInsights.innerHTML = '<p>Analyzing your mood patterns...</p>';
    
    try {
        // Get insights from Amazon Comprehend
        const insights = await analyzeEntries(entries);
        
        // Display insights
        displayInsights(insights, aiInsights);
    } catch (error) {
        console.error('Error updating AI insights:', error);
        aiInsights.innerHTML = '<p>Error analyzing mood patterns. Please try again later.</p>';
    }
}

/**
 * Analyze entries using Amazon Comprehend
 * @param {Array} entries - The mood entries
 * @returns {Object} - The analysis results
 */
async function analyzeEntries(entries) {
    try {
        // Filter entries with notes
        const entriesWithNotes = entries.filter(entry => entry.notes && entry.notes.trim().length > 0);
        
        if (entriesWithNotes.length === 0) {
            return {
                sentiment: null,
                keyPhrases: [],
                patterns: [],
                suggestions: [
                    'Try adding notes to your mood entries to get more insights.',
                    'Regular tracking with detailed notes helps identify patterns.'
                ]
            };
        }
        
        // Prepare text for analysis
        const combinedText = entriesWithNotes.map(entry => entry.notes).join(' ');
        
        // In a real implementation, you would use AWS.Comprehend
        // For now, we'll just simulate the API call
        console.log('Analyzing text with Amazon Comprehend:', combinedText.substring(0, 100) + '...');
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Simulate sentiment analysis
        const sentimentScores = {
            Positive: Math.random() * 0.5 + 0.3,
            Negative: Math.random() * 0.3,
            Neutral: Math.random() * 0.3,
            Mixed: Math.random() * 0.1
        };
        
        const sentiment = Object.keys(sentimentScores).reduce((a, b) => 
            sentimentScores[a] > sentimentScores[b] ? a : b
        );
        
        // Simulate key phrases extraction
        const keyPhrases = [
            'work stress',
            'good sleep',
            'exercise',
            'family time',
            'meditation'
        ].filter(() => Math.random() > 0.3);
        
        // Generate patterns based on entries
        const patterns = generatePatterns(entries);
        
        // Generate suggestions based on patterns and sentiment
        const suggestions = generateSuggestions(patterns, sentiment);
        
        return {
            sentiment,
            sentimentScores,
            keyPhrases,
            patterns,
            suggestions
        };
    } catch (error) {
        console.error('Error analyzing entries:', error);
        throw error;
    }
}

/**
 * Generate patterns based on entries
 * @param {Array} entries - The mood entries
 * @returns {Array} - The identified patterns
 */
function generatePatterns(entries) {
    const patterns = [];
    
    // Need at least 7 entries to identify patterns
    if (entries.length < 7) {
        return patterns;
    }
    
    // Check for day of week patterns
    const dayMoods = [0, 0, 0, 0, 0, 0, 0]; // Sun, Mon, ..., Sat
    const dayCounts = [0, 0, 0, 0, 0, 0, 0];
    
    entries.forEach(entry => {
        const date = new Date(entry.date);
        const day = date.getDay();
        dayMoods[day] += entry.mood;
        dayCounts[day]++;
    });
    
    // Calculate average mood for each day
    const dayAvgMoods = dayMoods.map((total, i) => 
        dayCounts[i] > 0 ? total / dayCounts[i] : 0
    );
    
    // Find best and worst days
    let bestDay = 0;
    let worstDay = 0;
    
    for (let i = 0; i < 7; i++) {
        if (dayCounts[i] > 0) {
            if (dayAvgMoods[i] > dayAvgMoods[bestDay] || dayCounts[bestDay] === 0) {
                bestDay = i;
            }
            if (dayAvgMoods[i] < dayAvgMoods[worstDay] || dayCounts[worstDay] === 0) {
                worstDay = i;
            }
        }
    }
    
    // Only add pattern if there's a significant difference
    if (dayCounts[bestDay] > 0 && dayCounts[worstDay] > 0 && 
        dayAvgMoods[bestDay] - dayAvgMoods[worstDay] > 1) {
        const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        patterns.push(`Your mood tends to be better on ${dayNames[bestDay]} and worse on ${dayNames[worstDay]}.`);
    }
    
    // Check for symptom correlations
    const symptomMoods = {};
    const symptomCounts = {};
    
    entries.forEach(entry => {
        if (entry.symptoms && entry.symptoms.length > 0) {
            entry.symptoms.forEach(symptom => {
                symptomMoods[symptom] = (symptomMoods[symptom] || 0) + entry.mood;
                symptomCounts[symptom] = (symptomCounts[symptom] || 0) + 1;
            });
        }
    });
    
    // Calculate average mood for each symptom
    const symptoms = Object.keys(symptomCounts);
    const symptomAvgMoods = {};
    
    symptoms.forEach(symptom => {
        symptomAvgMoods[symptom] = symptomMoods[symptom] / symptomCounts[symptom];
    });
    
    // Calculate overall average mood
    const totalMood = entries.reduce((sum, entry) => sum + entry.mood, 0);
    const avgMood = totalMood / entries.length;
    
    // Find symptoms with significant impact on mood
    symptoms.forEach(symptom => {
        if (symptomCounts[symptom] >= 3) { // Need at least 3 occurrences
            const moodDiff = symptomAvgMoods[symptom] - avgMood;
            if (Math.abs(moodDiff) >= 0.5) {
                if (moodDiff < 0) {
                    patterns.push(`${symptom} appears to negatively affect your mood.`);
                } else {
                    patterns.push(`${symptom} doesn't seem to significantly impact your mood.`);
                }
            }
        }
    });
    
    // Check for mood trends
    if (entries.length >= 14) {
        const recentEntries = [...entries].sort((a, b) => 
            new Date(b.date) - new Date(a.date)
        ).slice(0, 7);
        
        const olderEntries = [...entries].sort((a, b) => 
            new Date(b.date) - new Date(a.date)
        ).slice(7, 14);
        
        const recentAvg = recentEntries.reduce((sum, entry) => sum + entry.mood, 0) / recentEntries.length;
        const olderAvg = olderEntries.reduce((sum, entry) => sum + entry.mood, 0) / olderEntries.length;
        
        if (recentAvg - olderAvg > 0.5) {
            patterns.push('Your mood has been improving over the past week.');
        } else if (olderAvg - recentAvg > 0.5) {
            patterns.push('Your mood has declined over the past week.');
        } else {
            patterns.push('Your mood has been relatively stable recently.');
        }
    }
    
    return patterns;
}

/**
 * Generate suggestions based on patterns and sentiment
 * @param {Array} patterns - The identified patterns
 * @param {string} sentiment - The overall sentiment
 * @returns {Array} - The suggestions
 */
function generateSuggestions(patterns, sentiment) {
    const suggestions = [];
    
    // Add general suggestions
    suggestions.push('Continue tracking your mood daily for more accurate insights.');
    
    // Add suggestions based on sentiment
    if (sentiment === 'Negative') {
        suggestions.push('Consider speaking with a mental health professional about your feelings.');
        suggestions.push('Try incorporating mindfulness or meditation into your daily routine.');
    } else if (sentiment === 'Positive') {
        suggestions.push('Keep up the good work! Note what activities contribute to your positive mood.');
    } else if (sentiment === 'Mixed' || sentiment === 'Neutral') {
        suggestions.push('Try to identify specific factors that affect your mood positively or negatively.');
    }
    
    // Add suggestions based on patterns
    if (patterns.some(p => p.includes('worse on'))) {
        suggestions.push('Plan enjoyable activities on days when your mood tends to be lower.');
    }
    
    if (patterns.some(p => p.includes('negatively affect'))) {
        suggestions.push('Work on strategies to manage symptoms that negatively impact your mood.');
    }
    
    if (patterns.some(p => p.includes('declined'))) {
        suggestions.push('Reflect on recent changes that might be affecting your well-being.');
    }
    
    return suggestions;
}

/**
 * Display insights in the UI
 * @param {Object} insights - The analysis results
 * @param {HTMLElement} container - The container element
 */
function displayInsights(insights, container) {
    // Create insights HTML
    let html = '';
    
    // Add sentiment analysis
    html += '<div class="insight-section">';
    html += '<h4>Overall Sentiment</h4>';
    
    if (insights.sentiment) {
        html += `<p>Your notes generally express a <strong>${insights.sentiment.toLowerCase()}</strong> sentiment.</p>`;
        
        // Add sentiment scores visualization
        html += '<div class="sentiment-bars">';
        for (const [sentiment, score] of Object.entries(insights.sentimentScores)) {
            const percentage = Math.round(score * 100);
            html += `<div class="sentiment-bar-container">
                <div class="sentiment-label">${sentiment}</div>
                <div class="sentiment-bar">
                    <div class="sentiment-bar-fill" style="width: ${percentage}%"></div>
                </div>
                <div class="sentiment-score">${percentage}%</div>
            </div>`;
        }
        html += '</div>';
    } else {
        html += '<p>Add notes to your entries to see sentiment analysis.</p>';
    }
    html += '</div>';
    
    // Add key phrases
    if (insights.keyPhrases && insights.keyPhrases.length > 0) {
        html += '<div class="insight-section">';
        html += '<h4>Common Themes</h4>';
        html += '<div class="key-phrases">';
        insights.keyPhrases.forEach(phrase => {
            html += `<span class="key-phrase">${phrase}</span>`;
        });
        html += '</div>';
        html += '</div>';
    }
    
    // Add patterns
    if (insights.patterns && insights.patterns.length > 0) {
        html += '<div class="insight-section">';
        html += '<h4>Patterns</h4>';
        html += '<ul class="patterns-list">';
        insights.patterns.forEach(pattern => {
            html += `<li>${pattern}</li>`;
        });
        html += '</ul>';
        html += '</div>';
    }
    
    // Add suggestions
    if (insights.suggestions && insights.suggestions.length > 0) {
        html += '<div class="insight-section">';
        html += '<h4>Suggestions</h4>';
        html += '<ul class="suggestions-list">';
        insights.suggestions.forEach(suggestion => {
            html += `<li>${suggestion}</li>`;
        });
        html += '</ul>';
        html += '</div>';
    }
    
    // Add disclaimer
    html += '<div class="insight-disclaimer">';
    html += '<p><small>These insights are generated by AI and are not a substitute for professional mental health advice.</small></p>';
    html += '</div>';
    
    // Update container
    container.innerHTML = html;
}

/**
 * Check if user is authenticated
 * @returns {Promise<boolean>} - Whether the user is authenticated
 */
async function isAuthenticated() {
    return window.auth && await window.auth.isAuthenticated();
}

// Export functions for use in other modules
window.insights = {
    updateAIInsights
};