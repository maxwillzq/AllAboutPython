cd ./data
appcfg.py upload_data --url=http://localhost:8085/_ah/remote_api --config_file=../bulkloader.yaml --filename=unit.csv --kind=Unit
appcfg.py upload_data --url=http://localhost:8085/_ah/remote_api --config_file=../bulkloader.yaml --filename=lesson.csv --kind=Lesson