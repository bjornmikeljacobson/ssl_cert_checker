import ssl
import socket
import datetime


def check_ssl_cert(domain):
    # Get the SSL certificate for the domain
    context = ssl.create_default_context()
    s = context.wrap_socket(socket.socket(), server_hostname=domain)
    s.connect((domain, 443))
    cert = s.getpeercert()

    # Get the expiration date of the certificate
    expires = datetime.datetime.strptime(cert["notAfter"], '%b %d %H:%M:%S %Y %Z')

    # Check if the certificate has expired
    if expires < datetime.datetime.now():
        print(f"SSL certificate for {domain} has expired")
    else:
        print(f"SSL certificate for {domain} expires on {expires.strftime('%Y-%m-%d %H:%M:%S')}")


# Test the SSL certificate checker
check_ssl_cert("google.com")
