  aws iam create-policy \
    --policy-name s3access-policy \
    --policy-document file://iam_access_policy.json
    
 eksctl utils associate-iam-oidc-provider --region=us-east-1 --cluster=clo835 --approve
 
 eksctl create iamserviceaccount \
  --name clo \
  --namespace final \
  --cluster clo835 \
  --attach-policy-arn arn:aws:s3:::team-final-project/s3access-policy \
  --approve
  