# Transformations

Contains Data Transformations Scripts

1. merge all csv in a folder
2. batch_spliter the merge csv file
3. deduplicate csv based on a column

Transformation Sequence:
1. json_email_segregations
2. proxy_curl_transformation
3. api/proxy_curl
4. add headers
5. 3_contact_number_fetcher
6. merge_email_number