# PythonADUsers
API that allows you to connect to Active Directory and get a list of users filtered by groups

# How to install
Install all dependencies
```
pip install -r requirements.txt
```

# How to use
### create_ad_connection/
Create connection with Active Directory

Example of post data
```
{
	"hostname": "127.0.0.1",
	"port": 10389,
	"user": "UID=admin,OU=system",
	"password": "secret"
}
```

### get_users/
Get users of Active Directory

To filter users by groups use url parameter 'group'

Example of url request
```
get_users/?group=ou=users,dc=wimpi,dc=net
```
