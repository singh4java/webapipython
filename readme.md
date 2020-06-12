pip install flask  
pip install gevent 
pip freeze > requirements.txt 
docker build -t mo1207/webapipython . 
docker run --rm -it -p 8080:8080 mo1207/webapipython:latest
