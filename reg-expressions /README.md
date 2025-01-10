# Useful Regular expressions for DevSecOps 

Here are some useful Python regex patterns for DevSecOps tasks, such as detecting sensitive data, analyzing logs, validating inputs, and scanning configurations.

## Detecting Sensitive Data 

### Email Addresses 

Useful for searching logs or code for exposed email addresses:

**Regex: r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'**

```python
import re
text = "Contact us at admin@example.com or support@example.org"
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(emails)

```

### Detect AWS Access Keys 

Search for accidentally hardcoded AWS Access Keys in code:

**Regex: r'AKIA[0-9A-Z]{16}'**

```python
import re
text = "AWS Access Key: AKIAIOSFODNN7EXAMPLE"
aws_keys = re.findall(r'AKIA[0-9A-Z]{16}', text)
print(aws_keys)

```

### Detect IP addresses 

Scan for IPv4 addresses in configuration files or logs

**Regex: r'\b(?:\d{1,3}\.){3}\d{1,3}\b'**

```python
import re
text = "Server IPs: 192.168.1.1 and 10.0.0.25"
ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
print(ips)

```

### Detect credit card numbers 

Check for patterns matching credit card formats (basic Luhn-like structure):

**Regex: r'\b(?:\d[ -]*?){13,16}\b'**

```python
import re
text = "Card: 4111-1111-1111-1111 or 5500 0000 0000 0004"
cards = re.findall(r'\b(?:\d[ -]*?){13,16}\b', text)
print(cards)
```

### Detect passwords 

Look for hardcoded passwords in configuration files:

**Regex: r'\b(?:password|pwd)\s*=\s*[^\s]+'**

```python

import re
text = "password=supersecret123 and pwd=badpassword"
passwords = re.findall(r'\b(?:password|pwd)\s*=\s*[^\s]+', text, re.IGNORECASE)
print(passwords)
```

## Log Analysis 

### Extract timestamps 

Detect ISO 8601 timestamps in logs:

**Regex: r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z'**

```python
import re
text = "Error occurred at 2024-04-01T15:30:00Z"
timestamps = re.findall(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', text)
print(timestamps)
```

### Extract HTTP Status Codes

Find HTTP status codes (e.g., 200, 404, 500) in logs

**Regex: r'\b[1-5][0-9]{2}\b'**

```python
import re
text = "GET /index.html 200 OK, POST /login 404 Not Found"
status_codes = re.findall(r'\b[1-5][0-9]{2}\b', text)
print(status_codes)

```

### Parse Log levels

Match log levels like ERROR, INFO, and DEBUG:

**Regex: r'\b(INFO|ERROR|DEBUG|WARN|CRITICAL)\b'**

```python
import re
text = "[ERROR] Connection failed. [INFO] Reconnecting."
levels = re.findall(r'\b(INFO|ERROR|DEBUG|WARN|CRITICAL)\b', text)
print(levels)
```

## Input Validation 

### Validate URLs

Ensure strings are valid URLs:

**Regex: r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[\S]*)?'**

```python
import re
text = "Visit https://example.com or http://test.org"
urls = re.findall(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[\S]*)?', text)
print(urls)
```

### Validate File Paths

Match Unix or Windows file paths:

**Regex: r'(/[\w/]+)|([a-zA-Z]:\\[\w\\]+)'**

```python
import re
text = "/etc/passwd or C:\\Users\\Admin\\file.txt"
paths = re.findall(r'(/[\w/]+)|([a-zA-Z]:\\[\w\\]+)', text)
print(paths)

```

### Validate Hashes

Detect common cryptographic hash patterns (e.g., MD5, SHA256):

**Regex for MD5: r'\b[a-fA-F0-9]{32}\b'**

**Regex for SHA256: r'\b[a-fA-F0-9]{64}\b'**

```python
import re
text = "MD5: 5d41402abc4b2a76b9719d911017c592, SHA256: a3f2..."
md5_hashes = re.findall(r'\b[a-fA-F0-9]{32}\b', text)
sha256_hashes = re.findall(r'\b[a-fA-F0-9]{64}\b', text)
print(md5_hashes, sha256_hashes)
```

## Configuration and secrets scanning 

### Detect Private Keys

Scan for RSA private keys in code:

**Regex: r'-----BEGIN [A-Z ]+KEY-----[\s\S]+?-----END [A-Z ]+KEY-----'**

```python
import re
text = "-----BEGIN PRIVATE KEY-----\nMIIBVgIBADANBg...\n-----END PRIVATE KEY-----"
private_keys = re.findall(r'-----BEGIN [A-Z ]+KEY-----[\s\S]+?-----END [A-Z ]+KEY-----', text)
print(private_keys)

```

### Detect IPV6 Addresses 

Match IPv6 addresses:

**Regex: r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'**

```python
import re
text = "IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ipv6 = re.findall(r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b', text)
print(ipv6)
```

