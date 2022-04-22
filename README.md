# Docker Build Exec Program

This program sends the file containing the program to the API and processes it instead.

The API simply acts as `multipart/form-data` and further informs you that the service is updated.

 

## Program Settings

Please run the program in the following order

```shell
# Default Setup Settings
sudo sh Install/install.sh

# Background Run Settings
sudo sh Install/set.sh
```

or

```shell
# Default Setup Settings
sudo sh Install/install.sh

# Run API General
sudo python3 App/main.py 
```

Make sure to run the API in the parent folder where README is located

To match, the default program installation requires administrator privileges, as well as background, API execution, all require administrator privileges.



- Example) CURL Python Request

```shell
curl -X 'POST' \
  'http://fig-tree.mireu.xyz/check' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@main.py;type=application/x-python'
```



- Example) Execution results

```json
{
    // Language executed
	"test build language" : "python",  
	
    // Container build time
    "container build time" : 0.7950694561004639,
	
    // Program Run Time
    "file execution time" : 0.02586960792541504,
	
    // Program Operation Results
    "file result" : "this_is_a_sample_file\n"
}
```



- Unsupported file types

```json
{
	// File type transferred
	"test build language" : "text/x-rust",
    
    // Result message
	"message" : "unsupported service file"
}
```



### Supported Docker Container Images

| Language   | Docker Hub URL                   | Implementation Form (T/F) |
| ---------- | -------------------------------- | ------------------------- |
| Python     | https://hub.docker.com/_/python  | True                      |
| Javascript | https://hub.docker.com/_/node    | True                      |
| Golang     | https://hub.docker.com/_/golang  | True                      |
| Ruby       | https://hub.docker.com/_/ruby    | False                     |
| Java       | https://hub.docker.com/_/openjdk | False                     |
| Php        | https://hub.docker.com/_/php     | False                     |
| Gcc        | https://hub.docker.com/_/gcc     | True                      |
| Rust       | https://hub.docker.com/_/rust    | False                     |
| R          | https://hub.docker.com/_/r-base  | False                     |