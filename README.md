# Amazon QLDB Login Example

Amazon QLDB is a blockchain-based database created by Amazon (AWS). This project is an example of how it works, it's just an flask api that can read and write on the database, in this example we'll read and write users and password.

## Why to use Amazon QLDB
QLDB or Amazon Quantum Ledger Database is a blockchain-based database which means that the database is transparent, immutable, and cryptographically verifiable in other words, the database is the dream of any Auditor out there. Ths project is an easy introducction to this service.

## Features
Using the code in this project you can easily query to your QLDB. Just import the class QLDBDriver Like this:

```python
from Clases.QLDBDriver import QLDBDriver

db = QLDBDriver()
```

To query data just call the "create_query" method of "db"

```python
query = "SELECT * FROM users WHERE username = '{}'".format(username)
data = db.create_query(query)

if len(data) > 0:
    return data[0]
```

To insert data, call the "create_insert" method of db, the first parameter is the table name, the second one is the data to insert

```python
data_to_save = {
    "username" : user,
    "password" : password
}
db.create_insert("users", data_to_save)
```


## How to use 

### Installation
1. Move to the directory src with your terminal
2. Install all the required package with the following command ">> pip install -r requirements.txt"
3. Go to [Amazon QLDB](https://aws.amazon.com/es/qldb/), Login, etc.
4. Create a Ledger.
5. Click your Ledger and find your "Region" and your "Amazon Resource Name (ARN)", save them.
6. Go to "Query editor" in the left menu
7. Select your Ledger, Copy the content of the file "Tables" in the text area and Click "Run"
8. Go to [Amazon IAM](https://aws.amazon.com/es/iam/)
9. Go to User, Add User 
10. Configure the user
11. Set it as "Programmatic access" and click Next
12. Select "Attach existing policies directly" and search for the "AmazonQLDBFullAccess" policy, then click Next
13. Continue with the process untill you find your "Access Key ID" and your "Secret Access Key"
14. Save them, they are your keys to access to QLDB from python
15. Go to the file "src/constants.py" fill all the information
16. Congrats! now you can use the project

### How to test it
1. Move to the directory src with your terminal
2. Run the following command ">>python main.py"
3. Go to your postman or whatever you use to make POST requests
4. Select your endpoint, in your case probably "http://127.0.0.1:5000/createUser"
5. Create your very first user with this JSON: "{ "user" : "myuser", "pass" : "mypassword" }"
6. Test your created user with the endpoint: "http://127.0.0.1:5000/validateUser" and JSON: "{ "user" : "myuser", "pass" : "mypassword" }"

## License
The name Amazon Quantum Ledger Database, AWS is property of Amazon. Everything else is licensed under MIT.

## More interesting projects
I have a lot of fun projects, check this:

### Blockchain
- https://github.com/HectorPulido/Decentralized-Twitter-with-blockchain-as-base

### Machine learning
- https://github.com/HectorPulido/Machine-learning-Framework-Csharp
- https://github.com/HectorPulido/Evolutionary-Neural-Networks-on-unity-for-bots
- https://github.com/HectorPulido/Imitation-learning-in-unity
- https://github.com/HectorPulido/Chatbot-seq2seq-C-

### You also can follow me in social networks
- Twitter: https://twitter.com/Hector_Pulido_
- Youtube: http://youtube.com/c/hectorandrespulidopalmar
- Twitch: https://www.twitch.tv/hector_pulido_