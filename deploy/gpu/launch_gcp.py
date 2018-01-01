#!/usr
"""
gcloud beta compute --project "" instances create "gputest" --zone "us-west1-b" --machine-type "n1-standard-4" --subnet "default" --no-restart-on-failure --maintenance-policy "TERMINATE" --service-account "{}" --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring.write","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --accelerator type=nvidia-tesla-p100,count=1 --min-cpu-platform "Automatic" --image "ubuntu-1604-xenial-v20171212" --image-project "ubuntu-os-cloud" --boot-disk-size "128" --boot-disk-type "pd-ssd" --boot-disk-device-name "gputest"
"""