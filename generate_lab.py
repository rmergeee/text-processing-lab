import os
import random

BASE_DIR = "/home/rost/Work/text-processing-lab"

def make_dirs():
    dirs = [
        "00_regex",
        "01_grep/logs",
        "01_grep/codebase/modules",
        "01_grep/codebase/tests",
        "02_sed/configs",
        "02_sed/dirty_data",
        "03_awk/tabular",
        "03_awk/multi_record",
        "03_awk/reports",
        "04_vim",
        "05_cheatsheets"
    ]
    for d in dirs:
        os.makedirs(os.path.join(BASE_DIR, d), exist_ok=True)

def generate_regex_files():
    # 00_regex/patterns.txt
    patterns_content = """# ==============================================================================
# НАВЧАЛЬНИЙ ФАЙЛ: 00_regex/patterns.txt
# Тестові шаблони для тренування регулярних виразів (Email, Phone, IP, Date, URL тощо)
# ==============================================================================

# --- СЕКЦІЯ 1: Email адреси (валідні та невалідні) ---
user@example.com
john.doe@company.co.uk
developer+test123@gmail.com
admin_root@sub.network.org
first.middle.last@domain.com.ua
sales-support@tech-hub.io
invalid_email_no_at.com
@missingusername.com
double..dots@domain.org
trailing_dot@domain.com.
user@domain_without_extension
spaces in.email@domain.com
valid.123_456@sub-domain.example.info
support@192.168.1.1
fake.email@.leadingdot.com
robert.o'connor@enterprise.com

# --- СЕКЦІЯ 2: Номери телефонів (UA, US, International) ---
+380501234567
+380 67 987 65 43
+380 (93) 111-22-33
050-123-45-67
044 200 10 20
+1 (555) 123-4567
555-867-5309
+44 20 7946 0958
+49 30 123456
0800500100
123-45-67
phone: +380-63-000-11-22
invalid: +380123
invalid: 000-00-0000000
invalid: +1-800-CALL-ME

# --- СЕКЦІЯ 3: IPv4 та IPv6 адреси ---
127.0.0.1
192.168.1.1
10.0.0.254
172.16.254.1
8.8.8.8
1.1.1.1
255.255.255.255
0.0.0.0
# Невалідні IP:
999.123.45.67
192.168.1.256
10.0.1
1.2.3.4.5
300.0.0.1
192.168.01.1
# IPv6:
2001:0db8:85a3:0000:0000:8a2e:0370:7334
fe80::1ff:fe23:4567:890a
::1
2001:db8::2:1
invalid: 2001:xyz::1

# --- СЕКЦІЯ 4: Дати (ISO, EU, US, Timestamps) ---
2024-05-18
2023-12-31
1999-01-01
2026-10-12
15.08.2024
01.01.2025
31.02.2024
07/04/2024
12/25/2023
2024-05-18T14:32:00Z
2024-10-12 10:15:30.123
# Невалідні дати:
2024-13-40
32.01.2023
1999-00-15
2024/05/18-bad
12-34-5678

# --- СЕКЦІЯ 5: URL, Домени та Хеші ---
https://www.example.com
https://api.github.com/repos/user/project/issues?state=open&sort=created
http://localhost:8080/dashboard
ftp://backup.server.internal:21/archive_2024.tar.gz
ssh://git@github.com:22/user/repo.git
http://example.com/search?q=regex+training&page=2#results
https://sub-domain.test.co.uk:443/path/index.html
invalid://wrong_protocol
git@github.com:torvalds/linux.git
UUID: 550e8400-e29b-41d4-a716-446655440000
UUID: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
Hex: #ffffff, #000, #ff5733, #3B82F6, #invalid_hex
MAC: 00:1A:2B:3C:4D:5E, 00-14-22-01-23-45, 01:23:45:67:89:ZZ
"""
    with open(f"{BASE_DIR}/00_regex/patterns.txt", "w", encoding="utf-8") as f:
        f.write(patterns_content)

    # 00_regex/messy_text.txt
    messy_content = """<div class="user-profile" id="usr_8921">
    <h2 class="name">Олександр Коваленко</h2>
    <p class="bio">DevOps Engineer interested in Kubernetes, Linux kernel, and automated pipelines.</p>
    <div class="contact-info">
        <span class="email">Email: <a href="mailto:oleksandr.k@cloud-tech.ua">oleksandr.k@cloud-tech.ua</a></span>
        <span class="phone">Tel: +380 (50) 444-55-66</span>
        <span class="location">Kyiv, Ukraine</span>
    </div>
    <div class="keys">
        <!-- SECRET TOKEN: do not leak! -->
        <code class="api-token">sk_live_984712098471298471209384bcda710</code>
        <code class="jwt">eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c</code>
    </div>
</div>

The the quick brown fox jumps jumps over the lazy dog dog.
Notice that duplicate duplicate words words often happen in draft texts.

Ціни на товари в прайсі:
- Сервер Dell PowerEdge: $3,450.00 (або зі знижкою $3200)
- Маршрутизатор MikroTik: €189.50
- Комутатор Cisco 24p: 15400.00 ₴
- Кабель Patch Cord 5m: 120 ₴
- Підписка Cloud Storage: $19.99/mo
- Ліцензія RedHat: 999.00 USD

Системні логи та метрики:
Memory usage: 4.8GB / 16.0GB (30%)
Disk I/O: 120MB/s read, 45MB/s write
Latency: 45ms, 120ms, 3.5s, 0.450s
Network speed: 1000Mbps, 10Gbps, 54kbps

Посилання у тексті:
Знайдіть документацію за посиланням [Офіційний сайт](https://kernel.org) або в джерелі [Git Репозиторій](https://github.com/torvalds/linux).
Також перегляньте [Внутрішній портал](http://wiki.corp.local:8000/docs/sysadmin?ref=header&lang=ua).
"""
    with open(f"{BASE_DIR}/00_regex/messy_text.txt", "w", encoding="utf-8") as f:
        f.write(messy_content)

    # 00_regex/sentences.txt
    sentences_content = """# Речення для тренування складних правил: lookahead, lookbehind, жадібності (greedy/lazy), груп

# --- Тест паролів (Lookaheads: мінімум 1 велика літера, 1 цифра, 1 спецсимвол, довжина >= 8) ---
Password123!        # ВАЛІДНИЙ
alllowercase        # НЕВАЛІДНИЙ (нема великих, цифр, символів)
NOLOWERCASE123!     # НЕВАЛІДНИЙ (нема маленьких)
NoSpecial123        # НЕВАЛІДНИЙ (нема спецсимволу)
Short1!             # НЕВАЛІДНИЙ (менше 8 символів)
Str0ng!Passw0rd2024 # ВАЛІДНИЙ
Admin#2026Secure    # ВАЛІДНИЙ

# --- Lookaround для цін та валют ---
The total cost was $150 yesterday, but today it is $230.
I bought 5 apples for $5 and 3 oranges for $4.50.
Points earned: 150 points, 230 score, 500 bonus.
(Завдання: виділити тільки суми, що йдуть після $, але без самого знака $)
(Завдання: виділити числові значення, після яких стоїть слово 'points')

# --- Контекстні слова (Positive/Negative Lookbehind/Lookahead) ---
We bought an Apple iPhone and an Apple MacBook.
He likes drinking apple juice every morning.
The Big Apple is a nickname for New York City.
Look at that green pineapple on the table.
(Завдання: знайти слово 'Apple' лише коли воно позначає бренд, а не сік чи ананас)

# --- Жадібність квантифікаторів (Greedy vs Lazy) ---
<div>Перший блок</div> і <div>Другий блок</div> та <span>Третій блок</span>
"Цитата 1" а між ними слова "Цитата 2" і ще "Цитата 3"
(item1) + (item2) * (item3)
(Завдання: витягти вміст окремих блоків div, а не весь рядок від першого <div> до останнього </div>)
"""
    with open(f"{BASE_DIR}/00_regex/sentences.txt", "w", encoding="utf-8") as f:
        f.write(sentences_content)

def generate_grep_files():
    # 01_grep/logs/access.log (200+ realistic web log entries)
    ips = [
        "192.168.1.45", "10.0.0.15", "172.16.5.99", "185.191.171.12",
        "93.175.20.130", "198.51.100.42", "203.0.113.195", "66.249.66.1",
        "45.33.32.156", "194.44.112.5"
    ]
    user_agents = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "curl/7.88.1",
        "python-requests/2.31.0",
        "sqlmap/1.7.2#stable (https://sqlmap.org)"
    ]
    endpoints = [
        ("GET", "/index.html", 200, 4520),
        ("GET", "/api/v1/users", 200, 1850),
        ("POST", "/api/v1/login", 200, 340),
        ("POST", "/api/v1/login", 401, 120),
        ("GET", "/admin/dashboard", 403, 560),
        ("GET", "/static/css/style.css", 200, 12400),
        ("GET", "/static/js/app.js", 200, 45600),
        ("GET", "/wp-login.php", 404, 312),
        ("GET", "/.env", 404, 290),
        ("GET", "/.git/config", 404, 295),
        ("POST", "/api/v2/checkout", 500, 1024),
        ("GET", "/api/v2/reports/export", 504, 150),
        ("GET", "/images/logo.png", 304, 0),
        ("GET", "/robots.txt", 200, 154),
        ("GET", "/api/v1/products?category=electronics&sort=asc", 200, 8950),
        ("POST", "/api/v1/upload", 413, 412),
    ]

    random.seed(42)
    lines = []
    base_time = "12/Oct/2026"
    for hour in range(0, 12):
        for minute in range(0, 60, 3):
            sec = random.randint(10, 59)
            t_str = f"{base_time}:{hour:02d}:{minute:02d}:{sec:02d} +0300"
            ip = random.choice(ips)
            method, path, status, size = random.choice(endpoints)
            ua = random.choice(user_agents)
            ref = "-" if random.random() > 0.4 else "https://example.com/home"
            # special cases
            if "sqlmap" in ua:
                path = "/api/v1/products?id=1' OR '1'='1"
                status = 400
                size = 230
            line = f'{ip} - - [{t_str}] "{method} {path} HTTP/1.1" {status} {size} "{ref}" "{ua}"'
            lines.append(line)

    with open(f"{BASE_DIR}/01_grep/logs/access.log", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # 01_grep/logs/auth.log
    auth_lines = [
        "Oct 12 00:15:01 srv-core CRON[10452]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)",
        "Oct 12 00:15:02 srv-core CRON[10452]: pam_unix(cron:session): session closed for user root",
        "Oct 12 01:22:10 srv-core sshd[10550]: Failed password for invalid user admin from 198.51.100.42 port 39420 ssh2",
        "Oct 12 01:22:13 srv-core sshd[10550]: Failed password for invalid user admin from 198.51.100.42 port 39422 ssh2",
        "Oct 12 01:22:15 srv-core sshd[10550]: Failed password for invalid user test from 198.51.100.42 port 39424 ssh2",
        "Oct 12 01:22:18 srv-core sshd[10550]: Failed password for root from 198.51.100.42 port 39426 ssh2",
        "Oct 12 01:22:20 srv-core sshd[10550]: Maximum authentication attempts exceeded for root from 198.51.100.42 port 39426 ssh2 [preauth]",
        "Oct 12 02:40:11 srv-core sshd[11200]: Accepted publickey for rost from 10.0.0.15 port 52340 ssh2: RSA SHA256:d8a9f0e1c2b3a4",
        "Oct 12 02:40:11 srv-core sshd[11200]: pam_unix(sshd:session): session opened for user rost(uid=1000) by (uid=0)",
        "Oct 12 02:45:30 srv-core sudo:     rost : TTY=pts/0 ; PWD=/home/rost ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx",
        "Oct 12 02:45:30 srv-core sudo: pam_unix(sudo:session): session opened for user root(uid=0) by rost(uid=1000)",
        "Oct 12 02:45:35 srv-core sudo: pam_unix(sudo:session): session closed for user root",
        "Oct 12 03:10:05 srv-core sshd[11450]: Failed password for invalid user support from 45.33.32.156 port 41200 ssh2",
        "Oct 12 03:10:09 srv-core sshd[11450]: Failed password for invalid user oracle from 45.33.32.156 port 41202 ssh2",
        "Oct 12 03:10:12 srv-core sshd[11450]: Failed password for invalid user postgres from 45.33.32.156 port 41204 ssh2",
        "Oct 12 04:00:01 srv-core systemd-logind[750]: New session 125 of user root.",
        "Oct 12 04:30:22 srv-core sshd[12010]: Accepted publickey for deploy from 172.16.5.99 port 48110 ssh2: ED25519 SHA256:88fa90bc12",
        "Oct 12 04:30:22 srv-core sshd[12010]: pam_unix(sshd:session): session opened for user deploy(uid=1001) by (uid=0)",
        "Oct 12 04:32:10 srv-core sudo:   deploy : TTY=pts/1 ; PWD=/var/www ; USER=root ; COMMAND=/usr/bin/docker compose pull",
        "Oct 12 04:35:00 srv-core sshd[12010]: pam_unix(sshd:session): session closed for user deploy",
        "Oct 12 05:00:00 srv-core sshd[12800]: Invalid user guest from 185.191.171.12 port 59000",
        "Oct 12 05:00:02 srv-core sshd[12800]: Failed password for invalid user guest from 185.191.171.12 port 59000 ssh2"
    ]
    # repeat pattern with variation
    extended_auth = []
    for i in range(5):
        for line in auth_lines:
            hour_mod = f"{(int(line[4:6]) + i * 2) % 24:02d}"
            new_line = line[:4] + hour_mod + line[6:]
            extended_auth.append(new_line)

    with open(f"{BASE_DIR}/01_grep/logs/auth.log", "w", encoding="utf-8") as f:
        f.write("\n".join(extended_auth) + "\n")

    # 01_grep/logs/app_errors.log
    app_log = """2026-10-12 08:00:01.102 [INFO] [app.server] Starting worker process on pid=4021
2026-10-12 08:00:02.154 [INFO] [app.db] Connected to PostgreSQL pool at 10.0.0.50:5432
2026-10-12 08:05:12.330 [DEBUG] [app.auth] Token validation took 1.2ms for user_id=402
2026-10-12 08:12:44.901 [WARNING] [app.cache] Redis cache miss for key 'cache:users:active'
2026-10-12 08:15:20.445 [ERROR] [app.payments] [trace_id=a8f0-1234-bc] Payment gateway timeout after 5000ms
Traceback (most recent call last):
  File "/app/services/payment.py", line 142, in process_transaction
    response = requests.post(PAYMENT_GW_URL, json=payload, timeout=5)
  File "/usr/local/lib/python3.11/site-packages/requests/api.py", line 115, in post
    return request('post', url, data=data, json=json, **kwargs)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='gw.payfast.internal', port=443): Max retries exceeded
2026-10-12 08:15:21.002 [INFO] [app.payments] [trace_id=a8f0-1234-bc] Rolling back order #88492
2026-10-12 08:20:00.110 [DEBUG] [app.metrics] Flushed 140 metrics to Prometheus
2026-10-12 08:35:10.512 [ERROR] [app.db] [trace_id=db-9921-ff] Deadlock detected during concurrent update
Traceback (most recent call last):
  File "/app/services/inventory.py", line 88, in reserve_stock
    cursor.execute("UPDATE items SET stock = stock - %s WHERE id = %s", (qty, item_id))
psycopg2.errors.DeadlockDetected: deadlock detected
DETAIL: Process 4021 waits for ExclusiveLock on tuple (14, 5); blocked by process 4028.
2026-10-12 08:35:11.004 [WARNING] [app.inventory] Retrying reserve_stock for item_id=1409 (attempt 1/3)
2026-10-12 08:50:33.782 [CRITICAL] [app.storage] Out of disk space on mount /mnt/attachments! (99.8% used)
2026-10-12 08:50:34.001 [ERROR] [app.upload] Failed to write file /mnt/attachments/invoice_99.pdf: No space left on device
2026-10-12 09:00:15.220 [INFO] [app.cleanup] Deleted 1420 expired session records
"""
    with open(f"{BASE_DIR}/01_grep/logs/app_errors.log", "w", encoding="utf-8") as f:
        f.write(app_log)

    # 01_grep/codebase
    code_main = """\"\"\"
Main application entry point.
\"\"\"
import os
import sys
import logging
from modules.api import create_app
from modules.db import init_db

# TODO: Add CLI arguments parser (argparse or click)
# FIXME: Graceful shutdown handler is missing for SIGTERM

logger = logging.getLogger("app")

def main():
    logger.info("Initializing system...")
    db = init_db()
    # TODO: Verify database migration version
    app = create_app(db)
    print("Application started on port 8000")
    return app

if __name__ == "__main__":
    main()
"""
    with open(f"{BASE_DIR}/01_grep/codebase/main.py", "w", encoding="utf-8") as f:
        f.write(code_main)

    code_utils = """\"\"\"
Utility functions and helpers.
\"\"\"
import re
import hashlib

def hash_password(password: str) -> str:
    # FIXME: Use bcrypt instead of sha256 for passwords
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def validate_email(email: str) -> bool:
    # TODO: Improve regex to RFC 5322 compliance
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

# DEPRECATED: Do not use in new endpoints
def legacy_formatter(data: dict) -> str:
    \"\"\"Old XML formatter. Deprecated since v2.1.0.\"\"\"
    return f"<data>{data}</data>"
"""
    with open(f"{BASE_DIR}/01_grep/codebase/utils.py", "w", encoding="utf-8") as f:
        f.write(code_utils)

    code_api = """\"\"\"
API route controllers.
\"\"\"
from modules.db import get_user, list_users

# TODO: Add rate limiting middleware
# FIXME: Security vulnerability - sanitize user input in search

def get_users_route(request):
    \"\"\"GET /api/v1/users\"\"\"
    query = request.args.get("q", "")
    return list_users(search=query)

def get_user_by_id(user_id: int):
    \"\"\"GET /api/v1/users/{id}\"\"\"
    user = get_user(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return user, 200

# TODO: Implement user creation POST /api/v1/users
"""
    with open(f"{BASE_DIR}/01_grep/codebase/modules/api.py", "w", encoding="utf-8") as f:
        f.write(code_api)

    code_db = """\"\"\"
Database connection and queries.
\"\"\"
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
# TODO: Move DB_PASS to vault secret manager
DB_PASS = "default_secret_password"

def init_db():
    print(f"Connecting to database at {DB_HOST}:{DB_PORT}...")
    return {"connected": True}

def list_users(search: str = ""):
    # FIXME: SQL injection possible here if string formatted directly!
    sql = f"SELECT id, name, email FROM users WHERE name LIKE '%{search}%'"
    return []

def get_user(user_id: int):
    # TODO: Add query caching with Redis
    return {"id": user_id, "name": "Admin User"}
"""
    with open(f"{BASE_DIR}/01_grep/codebase/modules/db.py", "w", encoding="utf-8") as f:
        f.write(code_db)

    code_test = """\"\"\"
Unit tests for API and utils.
\"\"\"
import pytest
from utils import validate_email, hash_password

def test_validate_email_valid():
    assert validate_email("test@example.com") is True
    assert validate_email("user.name+tag@sub.domain.org") is True

def test_validate_email_invalid():
    assert validate_email("plainaddress") is False
    assert validate_email("@missinguser.com") is False

# TODO: Write tests for database mock failures
@pytest.mark.skip(reason="Not implemented yet")
def test_db_timeout():
    pass
"""
    with open(f"{BASE_DIR}/01_grep/codebase/tests/test_api.py", "w", encoding="utf-8") as f:
        f.write(code_test)

    config_json = """{
  "app_name": "CoreService",
  "version": "1.4.2",
  "environment": "staging",
  "server": {
    "host": "0.0.0.0",
    "port": 8080,
    "workers": 4,
    "debug": true
  },
  "database": {
    "host": "db.internal.net",
    "port": 5432,
    "name": "staging_db",
    "pool_size": 20
  },
  "logging": {
    "level": "DEBUG",
    "format": "json"
  }
}
"""
    with open(f"{BASE_DIR}/01_grep/codebase/config.json", "w", encoding="utf-8") as f:
        f.write(config_json)

def generate_sed_files():
    # 02_sed/configs/app.conf
    app_conf = """# ==========================================
# Application Configuration File
# Environment: Staging
# ==========================================

[general]
app_name = MyApp
# debug = true
debug = false
log_level = INFO
timezone = Europe/Kyiv

[server]
host = 127.0.0.1
# port = 8080
port = 3000
timeout = 60
keepalive = 300
workers = 2

[database]
db_host = localhost
db_port = 5432
db_name = old_database_name
db_user = app_admin
db_password = OLD_SECRET_KEY
# pool_size = 5
pool_size = 10
ssl_mode = disable

[redis]
redis_host = 127.0.0.1
redis_port = 6379
# redis_password = none
"""
    with open(f"{BASE_DIR}/02_sed/configs/app.conf", "w", encoding="utf-8") as f:
        f.write(app_conf)

    # 02_sed/configs/nginx.conf
    nginx_conf = """user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 768;
}

http {
    # Sendfile settings
    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;

    # Logging settings
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    # Server configuration
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # Root directory
        root /var/www/html;
        index index.html index.htm;

        server_name example.com www.example.com;

        location / {
            try_files $uri $uri/ =404;
        }

        # API Proxy
        location /api/ {
            proxy_pass http://localhost:3000/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        # Static assets caching
        location ~* \\.(jpg|jpeg|png|gif|ico|css|js)$ {
            expires 7d;
            add_header Cache-Control "public, no-transform";
        }
    }
}
"""
    with open(f"{BASE_DIR}/02_sed/configs/nginx.conf", "w", encoding="utf-8") as f:
        f.write(nginx_conf)

    # 02_sed/dirty_data/raw_export.csv
    csv_dirty = """id , first_name , last_name , email , birth_date , salary 
1 ,  John  , Doe , john.doe@example.com , 14/05/1990 , 3200 
2 , Jane ,  Smith , jane.smith@company.org , 22/11/1985 , 4500 

3 ,  Oleg , Kovalenko , oleg.k@work.ua , 08/02/1994 , 2800 
4 , Maria , Melnyk  , maria.m@domain.com , 30/09/1991 , 5100 
5 ,  Alex , Brown , alex.b@example.net , 19/07/1988 , 3900 

6 , Kateryna , Shevchenko , katya.sh@dev.ua , 01/12/1996 , 4200 
"""
    with open(f"{BASE_DIR}/02_sed/dirty_data/raw_export.csv", "w", encoding="utf-8") as f:
        f.write(csv_dirty)

    # 02_sed/dirty_data/dos_endings.txt (with \r\n and trailing spaces)
    dos_content = "First line with carriage return\r\nSecond line with trailing spaces   \r\n\r\nThird line after empty line\r\n\r\n\r\nFourth line with tabs\t\t\r\nFifth and final line\r\n"
    with open(f"{BASE_DIR}/02_sed/dirty_data/dos_endings.txt", "wb") as f:
        f.write(dos_content.encode("utf-8"))

    # 02_sed/substitutions.txt
    sub_content = """# Навчальний файл для адресних заміток sed (номери рядків, діапазони, вставки)

# Рядок 3: Замініть слово FOO на BAR
Line 04: This line contains FOO and another FOO.
Line 05: Another line with FOO.
Line 06: Keep this FOO as FOO if not targeted.
Line 07: Just normal line.
Line 08: Just normal line.
Line 09: Just normal line.
Line 10: Just normal line.

<!-- SECTION_ALPHA_START -->
Content inside section alpha.
Configuration parameter: active = true
Host parameter: host = alpha.local
Target item: replace_me_now
<!-- SECTION_ALPHA_END -->

Ordinary text in between sections.
Nothing to change here.

<!-- SECTION_BETA_START -->
Content inside section beta.
Configuration parameter: active = false
Host parameter: host = beta.local
Target item: replace_me_now
<!-- SECTION_BETA_END -->

End of document.
"""
    with open(f"{BASE_DIR}/02_sed/substitutions.txt", "w", encoding="utf-8") as f:
        f.write(sub_content)

def generate_awk_files():
    # 03_awk/tabular/users.csv (50 records)
    departments = ["Engineering", "DevOps", "Marketing", "Sales", "HR", "Finance", "Product"]
    first_names = ["Олександр", "Марія", "Дмитро", "Олена", "Іван", "Анна", "Сергій", "Юлія", "Андрій", "Наталія"]
    last_names = ["Ковальчук", "Шевченко", "Бондаренко", "Ткаченко", "Кравченко", "Коваль", "Олійник", "Бойко", "Мельник", "Лисенко"]
    statuses = ["active", "active", "active", "inactive", "on_leave"]

    users = ["id,first_name,last_name,email,department,salary,status,hire_date"]
    random.seed(101)
    for i in range(1, 51):
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        dept = random.choice(departments)
        salary = random.randint(1800, 7500)
        status = random.choice(statuses)
        year = random.randint(2018, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hire_date = f"{year}-{month:02d}-{day:02d}"
        email = f"user{i}_{ln.lower()}@corp.ua"
        users.append(f"{i},{fn},{ln},{email},{dept},{salary},{status},{hire_date}")

    with open(f"{BASE_DIR}/03_awk/tabular/users.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(users) + "\n")

    # 03_awk/tabular/passwd.mock (mock /etc/passwd)
    passwd_lines = [
        "root:x:0:0:root:/root:/bin/bash",
        "daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin",
        "bin:x:2:2:bin:/bin:/usr/sbin/nologin",
        "sys:x:3:3:sys:/dev:/usr/sbin/nologin",
        "sync:x:4:65534:sync:/bin:/bin/sync",
        "games:x:5:60:games:/usr/games:/usr/sbin/nologin",
        "man:x:6:12:man:/var/cache/man:/usr/sbin/nologin",
        "lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin",
        "mail:x:8:8:mail:/var/mail:/usr/sbin/nologin",
        "news:x:9:9:news:/var/spool/news:/usr/sbin/nologin",
        "uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin",
        "proxy:x:13:13:proxy:/bin:/usr/sbin/nologin",
        "www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin",
        "backup:x:34:34:backup:/var/backups:/usr/sbin/nologin",
        "list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin",
        "irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin",
        "gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin",
        "nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin",
        "systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin",
        "systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin",
        "rost:x:1000:1000:Rostyslav User,,,:/home/rost:/bin/bash",
        "deploy:x:1001:1001:CI/CD Automation Agent:/home/deploy:/bin/bash",
        "analyst:x:1002:1002:Data Analyst User:/home/analyst:/bin/zsh",
        "developer:x:1003:1003:Fullstack Dev:/home/developer:/bin/bash",
        "qa_tester:x:1004:1004:QA Test User:/home/qa_tester:/bin/sh",
        "guest_demo:x:1005:1005:Demo Visitor:/home/guest_demo:/bin/false",
        "postgres:x:115:122:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash",
        "redis:x:116:123:Redis In-Memory Store,,,:/var/lib/redis:/usr/sbin/nologin",
        "prometheus:x:117:124:Prometheus Monitoring:/var/lib/prometheus:/usr/sbin/nologin",
        "grafana:x:118:125:Grafana Dashboard:/usr/share/grafana:/bin/false"
    ]
    with open(f"{BASE_DIR}/03_awk/tabular/passwd.mock", "w", encoding="utf-8") as f:
        f.write("\n".join(passwd_lines) + "\n")

    # 03_awk/tabular/metrics.tsv
    metrics_lines = ["timestamp\thostname\tcpu_pct\tmem_mb\tdisk_io_kbs\tstatus"]
    hosts = ["srv-web-01", "srv-web-02", "srv-db-01", "srv-redis-01", "srv-worker-01"]
    random.seed(202)
    for minute in range(0, 30):
        t = f"2026-10-12 10:{minute:02d}:00"
        for h in hosts:
            if "db" in h:
                cpu = round(random.uniform(40.0, 95.0), 1)
                mem = random.randint(12000, 15800)
                io = random.randint(1200, 8500)
            elif "web" in h:
                cpu = round(random.uniform(15.0, 75.0), 1)
                mem = random.randint(2000, 4200)
                io = random.randint(100, 1200)
            else:
                cpu = round(random.uniform(5.0, 45.0), 1)
                mem = random.randint(1500, 3100)
                io = random.randint(50, 400)
            status = "CRITICAL" if cpu > 90.0 else ("WARNING" if cpu > 70.0 else "OK")
            metrics_lines.append(f"{t}\t{h}\t{cpu}\t{mem}\t{io}\t{status}")

    with open(f"{BASE_DIR}/03_awk/tabular/metrics.tsv", "w", encoding="utf-8") as f:
        f.write("\n".join(metrics_lines) + "\n")

    # 03_awk/multi_record/inventory.txt (stanza records with RS="")
    inventory_content = """Item: Dell PowerEdge R740
SKU: SRV-DEL-740
Category: Server
Stock: 8
UnitCost: 4500.00
Location: Rack-A1

Item: Cisco Catalyst 9300
SKU: NET-CIS-9300
Category: Network
Stock: 3
UnitCost: 3200.00
Location: Rack-A2

Item: APC Smart-UPS RT 5000VA
SKU: PWR-APC-5000
Category: Power
Stock: 12
UnitCost: 1850.00
Location: Floor-B

Item: Ubiquiti UniFi Pro AP
SKU: NET-UBI-PRO
Category: Network
Stock: 25
UnitCost: 199.00
Location: Storage-C

Item: HP ProLiant DL380 Gen10
SKU: SRV-HP-380
Category: Server
Stock: 2
UnitCost: 5100.00
Location: Rack-A3

Item: Synology RackStation RS3621xs+
SKU: STR-SYN-3621
Category: Storage
Stock: 4
UnitCost: 4100.00
Location: Rack-B1
"""
    with open(f"{BASE_DIR}/03_awk/multi_record/inventory.txt", "w", encoding="utf-8") as f:
        f.write(inventory_content)

    # 03_awk/reports/orders.txt
    orders = [
        "ORD_ID CLIENT CATEGORY QTY PRICE STATUS DATE",
        "ORD-101 ACME_Corp Hardware 5 350.00 Completed 2026-09-01",
        "ORD-102 Globex Software 12 49.99 Completed 2026-09-02",
        "ORD-103 Initech Hardware 2 1200.00 Pending 2026-09-03",
        "ORD-104 Umbrella Support 1 2500.00 Completed 2026-09-03",
        "ORD-105 ACME_Corp Software 20 89.00 Completed 2026-09-04",
        "ORD-106 Stark_Ind Hardware 8 750.00 Cancelled 2026-09-05",
        "ORD-107 Wayne_Ent Hardware 15 1100.00 Completed 2026-09-06",
        "ORD-108 Cyberdyne Support 4 1500.00 Completed 2026-09-07",
        "ORD-109 Globex Hardware 3 450.00 Pending 2026-09-08",
        "ORD-110 Initech Software 50 25.00 Completed 2026-09-09",
        "ORD-111 ACME_Corp Support 2 800.00 Completed 2026-09-10",
        "ORD-112 Stark_Ind Software 10 199.99 Completed 2026-09-11"
    ]
    with open(f"{BASE_DIR}/03_awk/reports/orders.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(orders) + "\n")

def generate_vim_files():
    # 04_vim/motions_and_operators.txt
    vim_motions = """# ==============================================================================
# ТРЕНУВАННЯ VIM: РУХИ (MOTIONS), ОПЕРАТОРИ ТА ШВИДКІСНЕ РЕДАГУВАННЯ
# Відкрийте цей файл у Vim: vim 04_vim/motions_and_operators.txt
# Виконуйте інструкції для кожного рядка!
# ==============================================================================

[Завдання 1: Видалення слова оператором 'dw']
Станьте курсором на слово DELETE_ME і натисніть 'dw':
The quick DELETE_ME brown fox jumps over the lazy dog.

[Завдання 2: Зміна слова оператором 'cw' або 'ciw']
Станьте на слово WRONG_WORD і змініть його на 'CORRECT' через 'ciw':
This is a WRONG_WORD statement that needs fixing.

[Завдання 3: Видалення до кінця рядка 'd$' або 'D']
Станьте на символ '|' і видаліть решту рядка через 'D':
Збережіть цю першу половину | А ВСЕ ЩО ПІСЛЯ ЦЬОГО СИМВОЛУ ТРЕБА ВИДАЛИТИ геть!

[Завдання 4: Стрибки між парними дужками через '%']
Станьте на першу круглу дужку '(' і натискайте '%', щоб стрибати до відповідної закриваючої:
result = ( [ a + b ] * ( c - { d / ( e + f ) } ) )

[Завдання 5: Швидкий перехід у рядку через 'f', 't', ';', ',']
Станьте на початок рядка. Знайдіть символ ':' натиснувши 'f:'. Натисніть ';' щоб перейти до наступного:
alpha:100; beta:200; gamma:300; delta:400; omega:500

[Завдання 6: Повторення останньої зміни крапкою '.']
Видаліть перше зайве слово 'BAD' через 'dw'. Перейдіть до наступного 'w' і натисніть '.' щоб повторити:
Word1 BAD Word2 BAD Word3 BAD Word4 BAD Word5.

[Завдання 7: Перехід на початок рядка '^' (до першого символу) та '0', і в кінець '$']
        Цей рядок має відступ у 8 пробілів. Перевірте різницю між '0' та '^'.
"""
    with open(f"{BASE_DIR}/04_vim/motions_and_operators.txt", "w", encoding="utf-8") as f:
        f.write(vim_motions)

    # 04_vim/text_objects.txt
    vim_objects = """# ==============================================================================
# ТРЕНУВАННЯ VIM: ТЕКСТОВІ ОБ'ЄКТИ (TEXT OBJECTS)
# Команди структури: <operator><i/a><object>
# i = inner (всередині), a = around (разом з межами)
# ==============================================================================

--- 1. Лапки (ci", da", ci', ca') ---
Рядок 1: Станьте всередину подвійних лапок і натисніть ci", щоб замінити текст:
message = "Тут знаходиться старе довге повідомлення яке треба переписати"

Рядок 2: Станьте всередину одинарних лапок і натисніть da', щоб видалити разом з лапками:
config_key = 'temporary_deprecated_setting'

Рядок 3: Вкладені лапки - змініть внутрішнє слово 'TARGET':
log_entry = "Помилка при виклику 'TARGET' у сервісі"

--- 2. Дужки (ci(, da(, ci{, da{, ci[, da[) ---
Рядок 4: Видаліть аргументи функції через ci(:
def calculate_metrics(old_arg1, old_arg2, old_arg3, old_flags=None):
    pass

Рядок 5: Видаліть весь блок списку разом з квадратними дужками через da[:
allowed_roles = ["admin", "superadmin", "moderator", "auditor"]

Рядок 6: Змініть вміст словника через ci{:
user_data = { id: 101, username: "oleg", active: true }

--- 3. HTML/XML Теги (cit, dat) ---
Рядок 7: Замініть текст всередині тегу h1 через cit:
<h1 class="header-main">Цей заголовок має стати 'Вітаємо на платформі!'</h1>

Рядок 8: Видаліть увесь тег span разом з тегами через dat:
<p>Звичайний текст <span class="badge warning">Застарілий бейдж</span> продовження речення.</p>
"""
    with open(f"{BASE_DIR}/04_vim/text_objects.txt", "w", encoding="utf-8") as f:
        f.write(vim_objects)

    # 04_vim/macros_practice.txt
    vim_macros = """# ==============================================================================
# ТРЕНУВАННЯ VIM: МАКРОСИ (MACROS) ТА ПАКЕТНА ОБРОБКА
# Завдання:
# 1. Станьте на перший рядок зі списку нижче.
# 2. Почніть запис макросу в регістр 'a': qa
# 3. Перетворіть рядок у формат SQL:
#    INSERT INTO users (username, role, city) VALUES ('john', 'admin', 'kyiv');
# 4. Зупиніть запис: q
# 5. Застосуйте макрос до решти рядків: 20@a (або виділіть візуально Shift-V і :norm @a)
# ==============================================================================

john admin kyiv
maria developer lviv
oleg devops odesa
anna qa dnipro
dmytro security kharkiv
serhiy analyst poltava
yulia pm vinnytsia
andriy architect ternopil
natalia designer lutsk
ivan sysadmin sumy
tetiana hr chernihiv
viktor lead uzhhorod
olena support rivne
denys dba zaporizhzhia
iryna manager mykolaiv
bohdan sre cherkasy
svitlana lead zhytomyr
maksym frontend kyiv
taras backend lviv
roman devops odesa
"""
    with open(f"{BASE_DIR}/04_vim/macros_practice.txt", "w", encoding="utf-8") as f:
        f.write(vim_macros)

    # 04_vim/refactor_challenge.py
    vim_refactor = """# ==============================================================================
# VIM REFACTORING CHALLENGE
# Завдання для тренування складних команд Vim:
# 1. Вирівняйте знаки '=' за допомогою Visual Block mode (Ctrl-v).
# 2. Замініть print(...) на logger.info(...) за допомогою :%s/print(\\([^)]*\\))/logger.info(\\1)/g
# 3. Видаліть усі рядки коментарів з '#' через :g/^\\s*#/d
# 4. Відсортуйте імпорти алфавітно через візуальне виділення і :sort
# ==============================================================================

import sys
import json
import os
import requests
import time
import math

# Temporary debug variables
db_host = "127.0.0.1"
db_port = 5432
db_user = "postgres"
db_password = "very_secret_password"
db_timeout_seconds = 30

# Calculate some settings
def run_diagnostics():
    # Print statement 1
    print("Starting diagnostics pipeline...")
    # Print statement 2
    print("Checking connection to database...")
    # Print statement 3
    print("Diagnostics completed successfully.")

# Extra junk comments to remove
# Junk line 1
# Junk line 2
# Junk line 3

def process_data(items):
    total = 0
    for item in items:
        # Debug print
        print(f"Processing item: {item}")
        total += item
    return total
"""
    with open(f"{BASE_DIR}/04_vim/refactor_challenge.py", "w", encoding="utf-8") as f:
        f.write(vim_refactor)

def generate_cheatsheets():
    # 05_cheatsheets/regex_cheatsheet.md
    regex_cs = """# Шпаргалка з RegEx (Регулярні вирази)

## 1. Базові класи та символи
| Символ | Опис | Приклад |
|---|---|---|
| `.` | Будь-який символ (крім нового рядка) | `a.c` -> `abc`, `a-c` |
| `\\d` / `\\D` | Цифра `[0-9]` / Не цифра `[^0-9]` | `\\d+` -> `1234` |
| `\\w` / `\\W` | Словоподібний символ `[a-zA-Z0-9_]` / Не слово | `\\w+` -> `var_1` |
| `\\s` / `\\S` | Пробільний символ `[ \\t\\r\\n\\f]` / Не пробіл | `\\s*` |
| `[abc]` | Один із зазначених символів | `[aeiou]` |
| `[^abc]` | Будь-який символ, крім зазначених | `[^0-9]` |
| `[a-z]` | Діапазон символів від a до z | `[0-9a-fA-F]` |

## 2. Квантифікатори (Повторення)
| Квантифікатор | Опис | Тип |
|---|---|---|
| `*` | 0 або більше разів | Жадібний (greedy) |
| `+` | 1 або більше разів | Жадібний |
| `?` | 0 або 1 раз (необов'язковий) | Жадібний |
| `{n}` | Рівно n разів | Точний |
| `{n,}` | Від n і більше разів | Жадібний |
| `{n,m}` | Від n до m разів | Жадібний |
| `*?`, `+?`, `??` | Ліниві квантифікатори (мінімальна відповідність) | Lazy / Non-greedy |

## 3. Якорі та межі (Anchors & Boundaries)
| Символ | Опис |
|---|---|
| `^` | Початок рядка (або початок тексту) |
| `$` | Кінець рядка (або кінець тексту) |
| `\\b` | Межа слова (word boundary) |
| `\\B` | Не межа слова |

## 4. Групи та зворотно-посилання (Groups & Lookarounds)
| Конструкція | Опис |
|---|---|
| `(...)` | Група захоплення (Capturing group, доступна через `\\1`, `$1`) |
| `(?:...)` | Група без захоплення (Non-capturing group) |
| `(?=...)` | Positive Lookahead (перевіряє наявність попереду) |
| `(?!...)` | Negative Lookahead (перевіряє відсутність попереду) |
| `(?<=...)` | Positive Lookbehind (перевіряє наявність позаду) |
| `(?<!...)` | Negative Lookbehind (перевіряє відсутність позаду) |
"""
    with open(f"{BASE_DIR}/05_cheatsheets/regex_cheatsheet.md", "w", encoding="utf-8") as f:
        f.write(regex_cs)

    # 05_cheatsheets/grep_cheatsheet.md
    grep_cs = """# Шпаргалка з grep

## Найважливіші прапорці
| Прапорець | Призначення | Приклад |
|---|---|---|
| `-E` | Extended Regex (підтримка `+`, `?`, `|`, `()` без екранування) | `grep -E "error|fail" file.log` |
| `-P` | Perl-Compatible Regex (підтримка `\\d`, `\\s`, lookarounds) | `grep -P "(?<=\\$)\\d+" file.txt` |
| `-i` | Нечутливість до регістру (case-insensitive) | `grep -i "warning" app.log` |
| `-v` | Інверсія пошуку (показати рядки, що НЕ збігаються) | `grep -v "^#" config.conf` |
| `-n` | Виводити номери рядків у файлі | `grep -n "TODO" main.py` |
| `-c` | Підрахувати кількість збігів | `grep -c "404" access.log` |
| `-o` | Виводити ТІЛЬКИ ту частину, що збіглась | `grep -oE "[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+" access.log` |
| `-w` | Пошук цілого слова (word match) | `grep -w "db" code.py` |
| `-r` / `-R` | Рекурсивний пошук у директоріях | `grep -rn "FIXME" ./src/` |
| `-l` | Вивести тільки назви файлів зі збігами | `grep -rl "secret" ./codebase/` |
| `-L` | Вивести назви файлів БЕЗ збігів | `grep -rL "license" ./codebase/` |
| `-A <N>` | Показати N рядків ПІСЛЯ збігу (After) | `grep -A 3 "ERROR" app.log` |
| `-B <N>` | Показати N рядків ДО збігу (Before) | `grep -B 2 "Exception" app.log` |
| `-C <N>` | Показати N рядків контексту (Before + After) | `grep -C 2 "CRITICAL" app.log` |
| `--include` | Обмежити пошук певними файлами | `grep -rn --include="*.py" "import" .` |
"""
    with open(f"{BASE_DIR}/05_cheatsheets/grep_cheatsheet.md", "w", encoding="utf-8") as f:
        f.write(grep_cs)

    # 05_cheatsheets/sed_cheatsheet.md
    sed_cs = """# Шпаргалка з sed (Stream Editor)

## Базовий синтаксис
`sed [options] 'command' input_file`

## Основні команди
| Команда | Опис | Приклад |
|---|---|---|
| `s/old/new/` | Заміна першого входження в рядку | `sed 's/foo/bar/' file.txt` |
| `s/old/new/g` | Глобальна заміна всіх входжень у рядку | `sed 's/foo/bar/g' file.txt` |
| `s/old/new/2` | Заміна лише 2-го входження в рядку | `sed 's/foo/bar/2' file.txt` |
| `d` | Видалення рядка | `sed '5d' file.txt` (видалити 5-й рядок) |
| `p` | Друк рядка (разом з `-n`) | `sed -n '10,20p' file.txt` (надрукувати 10-20 рядки) |
| `i\\text` | Вставити текст ПЕРЕД вказаним рядком | `sed '1i\\# HEADER' file.txt` |
| `a\\text` | Додати текст ПІСЛЯ вказаного рядка | `sed '$a\\# FOOTER' file.txt` |
| `c\\text` | Замінити весь рядок зазначеним текстом | `sed '3c\\New line content' file.txt` |

## Адресація та діапазони
- `sed '1,5d' file.txt` — видалити з 1 по 5 рядок.
- `sed '$d' file.txt` — видалити останній рядок.
- `sed '/^#/d' file.txt` — видалити всі рядки-коментарі, що починаються з `#`.
- `sed '/^$/d' file.txt` — видалити всі порожні рядки.
- `sed '/START/,/END/s/foo/bar/g' file.txt` — замінити між блоками START і END.

## Прапорці sed
- `-i` — редагування файлу на місці (in-place). З бекапом: `-i.bak`.
- `-E` — розширені регулярні вирази (Extended Regex).
- `-n` — придушити автоматичний вивід (виводити тільки явні команди `p`).
"""
    with open(f"{BASE_DIR}/05_cheatsheets/sed_cheatsheet.md", "w", encoding="utf-8") as f:
        f.write(sed_cs)

    # 05_cheatsheets/awk_cheatsheet.md
    awk_cs = """# Шпаргалка з awk

## Базова структура
`awk 'BEGIN { ... } condition { action } END { ... }' file`

## Вбудовані змінні
| Змінна | Значення |
|---|---|
| `$0` | Весь поточний рядок цілком |
| `$1, $2..$NF` | Окремі поля (стовпчики) рядка |
| `NF` | Кількість полів у поточному рядку (Number of Fields) |
| `NR` | Номер поточного рядка від початку (Number of Records) |
| `FNR` | Номер рядка в поточному файлі |
| `FS` | Розділювач вхідних полів (Field Separator, за замовчуванням пробіл/таб) |
| `OFS` | Розділювач вихідних полів (Output Field Separator) |
| `RS` | Розділювач вхідних записів (за замовчуванням `\\n`) |
| `ORS` | Розділювач вихідних записів |

## Корисні патерни
- Друк колонок: `awk '{print $1, $3}' file.txt`
- Зазначення розділювача: `awk -F: '{print $1, $7}' /etc/passwd`
- CSV розділювач: `awk -F, '{print $2, $6}' users.csv`
- Фільтр за умовою: `awk -F, '$6 > 4000 {print $2, $6}' users.csv`
- Сума стовпчика: `awk -F, '{sum += $6} END {print "Total:", sum, "Avg:", sum/NR}' users.csv`
- Асоціативні масиви (групування):
  ```bash
  awk -F, 'NR>1 {dept[$5] += $6; count[$5]++} END {for (d in dept) print d, dept[d]/count[d]}' users.csv
  ```
- Форматований вивід: `awk '{printf "%-20s %10.2f\\n", $1, $2}'`
"""
    with open(f"{BASE_DIR}/05_cheatsheets/awk_cheatsheet.md", "w", encoding="utf-8") as f:
        f.write(awk_cs)

    # 05_cheatsheets/vim_cheatsheet.md
    vim_cs = """# Шпаргалка з Vim

## Режими
- `Normal` (Esc) — навігація, команди, видалення, копіювання.
- `Insert` (`i`, `I`, `a`, `A`, `o`, `O`) — введення тексту.
- `Visual` (`v` — посимвольний, `V` — рядковий, `Ctrl-v` — блоковий/стовпчиковий).
- `Command` (`:`) — збереження, заміна, системні команди.

## Навігація в Normal Mode
| Команда | Дія |
|---|---|
| `h, j, k, l` | Вліво, вниз, вгору, вправо |
| `w / b` | Стрибок на слово вперед / назад |
| `e / ge` | Стрибок на кінець слова вперед / назад |
| `0 / ^ / $` | Початок рядка / перший непробільний символ / кінець рядка |
| `gg / G / <N>G` | Початок файлу / кінець файлу / перехід на рядок N |
| `f<char> / t<char>` | Стрибок у рядку до символу / перед символом |
| `%` | Стрибок до парної дужки `()`, `{}`, `[]` |
| `* / #` | Пошук слова під курсором вперед / назад |

## Оператори та текстові об'єкти
- Оператори: `d` (delete), `c` (change), `y` (yank/copy), `v` (select), `>` (indent).
- Текстові об'єкти:
  - `iw` / `aw` — inner / around word
  - `i"` / `a"` — inner / around quotes
  - `i(` / `a(` — inner / around parentheses
  - `i{` / `a{` — inner / around curly braces
  - `it` / `at` — inner / around HTML/XML tags
- Комбінації: `ciw`, `da"`, `ci(`, `dat`, `vip`.

## Пошук і заміна
- `:%s/старе/нове/g` — замінити у всьому файлі.
- `:%s/старе/нове/gc` — замінити з підтвердженням кожного збігу.
- `:10,25s/старе/нове/g` — замінити у діапазоні рядків 10-25.
- `:g/pattern/d` — видалити всі рядки, що містять pattern.
- `:v/pattern/d` — видалити всі рядки, що НЕ містять pattern.

## Макроси
1. `qa` — почати запис у регістр `a`.
2. Виконати послідовність дій.
3. `q` — зупинити запис.
4. `@a` — виконати макрос.
5. `10@a` — виконати 10 разів.
"""
    with open(f"{BASE_DIR}/05_cheatsheets/vim_cheatsheet.md", "w", encoding="utf-8") as f:
        f.write(vim_cs)

if __name__ == "__main__":
    make_dirs()
    generate_regex_files()
    generate_grep_files()
    generate_sed_files()
    generate_awk_files()
    generate_vim_files()
    generate_cheatsheets()
    print("All files generated successfully!")
