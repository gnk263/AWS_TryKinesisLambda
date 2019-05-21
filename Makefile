BUCKET_NAME := gnk263-sam-bucket
STACK_NAME := TryKinesisLambda

create-bucket:
	aws s3 mb s3://$(BUCKET_NAME)

build:
	sam build

deploy:
	sam package \
		--output-template-file packaged.yaml \
		--s3-bucket $(BUCKET_NAME)

	sam deploy \
		--template-file packaged.yaml \
		--stack-name $(STACK_NAME) \
		--capabilities CAPABILITY_IAM

delete:
	aws cloudformation delete-stack --stack-name $(STACK_NAME)

put-records:
	aws kinesis put-records --cli-input-json file://test-data.json
