from google.oauth2 import service_account
from google.cloud import aiplatform

# Load the service account key file
credentials = service_account.Credentials.from_service_account_info(
    {
        "type": "service_account",
        "project_id": "mounika8036-426015",
        "private_key_id": "b4fef215183c2e161242f9d6a7c6cad2947fe9fa",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1VrRJ7JalVlTd\nMCxJuY7dhcKA1OzC4CqsXgR2Qok++DY0gVUuNKConsvRe1AdXxGH6HY+aDF58/kc\nUrRl05QV8SZEogbbKLyvOeAdJ6fnUA/Jrths8mxoCwhqVjgNQZoBkFTK+s9ymYqS\njeBtmMr0qehFpcUAagVWSicPmwpP2OAlJW/kpxXU+G14dk7DEikflxpX8NyuoxSP\n20tfxuMqJ6mJ0voPD0M02jpbaqM6YDZFZGtXeFKDizGA9bVVY/t9j/sFKTrx4+w2\nyhw9nd7tUvO9lRppw2B8PWclHoRP2PBYbrxm8QLTuI0J+VpgHi3xvMaqACeFUPmf\nQwLwZ4cJAgMBAAECggEAI6QsAU+X+F00htjeC4uGEfIlXY78Df1jRceg1uGS+iZs\n+PrmlBNR9HJpmv3CrFMwLec5vmBaQR77ul5jCJSCSaHBJMI32MFz/HjCnNhbfvJU\neA5+iUNInVZ1y/iwQaLAM0h78f1D4sFc5BswnjnmwhnXBkFjrAYqkGA4ty+A4lpn\n36mTY9UnplP5byqHZS9Ntz0WS2Qyh8dOg9XSdw5pjGD2SzafaasoYmm7IDN0QZ20\nOMX5o3I4ktId+yHNG3gp8e8dQb+CRFEMAsCavCLiociECusiVa5a/cjISdr5KZKg\nWRv0yjHhFlxjzo3nr0PM/RkXgTdr2pFxDel8kMUzVQKBgQDvivh+g3cnV8zgDqoC\nMzWjwJJeM1WURq950r0vi6UA6MJa0HqIJijak2jb32jAzDZu0GVlu0Xg0G6QZB+i\nl2Hx2jswYTsTNW+Egvw2d+vHlO88YK0hCdKwhaIKUtMqEr87qZipgRfbRbrDR22h\nZk8WRkNLVijQR+QP/i7JpssplwKBgQDBzA0LMCqirdRomniEnOy9hmStWNidxDDu\nNSvQ4qSawIp6lTxUkdHWe+sCMJfOfr01nEOFLKpnlTUPCDYKh15JHUdA3/maPC4f\nkBkSdGXRiJ8QbjujvYi7VB6hZQ9zggIyNsAD8w0j0EMvhGKJ1KybCl9VzH/GBOWy\nIiGrTQioXwKBgFwm3kntUV11TX+0pHqMMMp6PtS2cunD96WqCNXNpwCeioZdRYYz\nB+xuYRyU6buh1B71VMy6Kru984rgubrW+fsMtVB7Vzqgh/I2YciigbYZ+Z8EohXf\nrYnzHs9R5aJ968uMBwrOetsEDEErrWU18p7jEOhekPzvazEr29v/qpCpAoGBAKJB\nzP38EwZnkjsOci9eD9zS5AI7LApTlEAtJoVa7URgRtFBl+SavlzdHbOUqdWLSbHU\nJrge4IGfbHAsiMqh8jA3IkxP+nTHRDrK9CL+b61SvRMNqEN80jk9wfORYLFuPZZ7\nPqNP4UWF/mqPZc1O0kFxGscEVEqgGQzfBN+evMvzAoGAcgB/8nifiIscQ3Mfm39i\n1Dvw1pIr/vXKp9Msbz7tZYuOno+mbep9a0HtOryICMGbg8urDw4ulex6ShXwSQjz\nDXMSl4XDVy9ohLg80LBjTF5/2o3TdwsTYhOYbW0xTKAP3mKqTcuKLc0YhyVLwbsc\nxfxeJ7n9bnLMDHzKHemi/YY=\n-----END PRIVATE KEY-----\n",
        "client_email": "mounika8036@mounika8036-426015.iam.gserviceaccount.com",
        "client_id": "107998271760158546074",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mounika8036%40mounika8036-426015.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
)

# Initialize the AI Platform client with credentials
aiplatform.init(credentials=credentials)
