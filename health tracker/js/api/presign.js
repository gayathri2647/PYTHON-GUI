import AWS from 'aws-sdk';

export default async function handler(req, res) {
  const { method, file } = req.query;

  const s3 = new AWS.S3({
    region: process.env.AWS_REGION,
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
    signatureVersion: 'v4',
  });

  const params = {
    Bucket: process.env.AWS_BUCKET_NAME,
    Key: file,
    Expires: 60,
  };

  try {
    const url = s3.getSignedUrl(method === 'PUT' ? 'putObject' : 'getObject', params);
    res.status(200).json({ url });
  } catch (e) {
    res.status(500).json({ error: 'Failed to generate URL' });
  }
}
