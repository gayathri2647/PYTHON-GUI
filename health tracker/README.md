# Mental Health Tracker with AI Insights

A web-based application for tracking mental health, moods, and symptoms with AI-powered insights.

## Features

- **Daily Mood Tracking**: Record your mood, symptoms, and personal notes
- **Mood History**: View and analyze your past mood entries
- **AI Insights**: Get personalized suggestions based on your mood patterns
- **Dark Mode**: Easy on the eyes, especially at night
- **Daily Reminders**: Never forget to log your mood
- **Calendar View**: Visualize your mood over time
- **Mood Streaks**: Stay motivated with streak tracking
- **Private & Secure**: Data stored securely with AWS
- **Offline Support**: Use the app even without internet connection

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Local Storage**: Browser's LocalStorage for offline functionality
- **AWS Services**:
  - Amazon Cognito: User authentication
  - Amazon DynamoDB: Cloud data storage
  - Amazon Comprehend: AI-based sentiment analysis
  - Amazon S3: Data backup and restore
  - AWS Amplify: Hosting and AWS service integration

## Getting Started

### Local Development

1. Clone this repository
2. Open `index.html` in your browser for local testing
3. The app will work with local storage only (no AWS features)

### AWS Setup

To enable cloud features, you'll need to set up the following AWS services:

#### 1. Amazon Cognito

1. Create a User Pool in the AWS Console
2. Configure app client settings
3. Update the `awsConfig` object in `js/auth.js` with your User Pool details

```javascript
const awsConfig = {
    Auth: {
        region: 'YOUR_REGION',
        userPoolId: 'YOUR_USER_POOL_ID',
        userPoolWebClientId: 'YOUR_APP_CLIENT_ID',
        mandatorySignIn: false,
        authenticationFlowType: 'USER_PASSWORD_AUTH'
    }
};
```

#### 2. Amazon DynamoDB

1. Create a table named `MoodEntries` with the following schema:
   - Partition key: `userId` (String)
   - Sort key: `entryId` (String)
   - Other attributes: `date` (String), `mood` (Number), `symptoms` (List), `notes` (String)

2. Set up appropriate IAM permissions for your Cognito authenticated users to access their own data

#### 3. Amazon Comprehend

1. Set up IAM permissions for your application to use Amazon Comprehend
2. The application will use Comprehend for:
   - Sentiment analysis of mood entry notes
   - Key phrase extraction to identify common themes
   - Language detection (optional)

#### 4. Amazon S3

1. Create an S3 bucket for user data backups
2. Configure CORS settings to allow access from your application domain
3. Set up appropriate IAM permissions for authenticated users to access their own backup files

#### 5. AWS Amplify

1. Install the AWS Amplify CLI: `npm install -g @aws-amplify/cli`
2. Initialize Amplify in your project: `amplify init`
3. Add authentication: `amplify add auth`
4. Add storage (S3 and DynamoDB): `amplify add storage`
5. Push changes to AWS: `amplify push`
6. Deploy your application: `amplify publish`

## Project Structure

```
mental-health-tracker/
├── index.html          # Main HTML file
├── css/
│   ├── styles.css      # Main stylesheet
│   └── dark-mode.css   # Dark mode styles
├── js/
│   ├── app.js          # Main application logic
│   ├── auth.js         # Authentication with Cognito
│   ├── storage.js      # Data storage (LocalStorage & DynamoDB)
│   ├── insights.js     # AI insights with Comprehend
│   └── backup.js       # S3 backup/restore functionality
└── tests/
    └── app.test.js     # Unit tests
```

## Usage

1. **Sign Up/Sign In**: Create an account or sign in to enable cloud features
2. **Track Your Mood**: Record your daily mood, symptoms, and notes
3. **View History**: See your past entries in list or calendar view
4. **Get Insights**: Receive AI-powered analysis of your mood patterns
5. **Manage Data**: Backup, restore, or export your data

## Privacy and Security

Your mental health data is important and private. This application:
- Stores data locally in your browser by default
- Only uploads to the cloud when you're signed in
- Encrypts data in transit and at rest
- Uses AWS IAM policies to ensure users can only access their own data
- Never shares your data with third parties

## Development

### Testing

Run tests with Jest:

```
npm install
npm test
```

### Extending the Application

- Add new symptoms in the HTML form
- Customize the AI insights by modifying the `insights.js` file
- Add additional AWS services by updating the AWS Amplify configuration

## License

MIT

## Disclaimer

This application is not a substitute for professional mental health care. If you're experiencing serious mental health issues, please consult with a healthcare professional.
