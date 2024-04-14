1. Start Docker
The docker mongo-db container stores the data in the host machine.
 - ``` docker-compose up -d ```  to start container in background
 - ```docker container ls ``` to check whether it worked

2. Run Backend using Flask: 
- ```flask --app expense_server run --debug --port 5000``` in console
- click on link in console to open a swagger documentation
- 
3. Run Frontend using React:
```npm start```