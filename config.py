import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

link={'https://urldefense.proofpoint.com/v2/url?u=https-3A__www.singtel.com_personal_products-2Dservices_mobile_cis-2Dplans-3FsessionToken-3Dd9842ed9-2D4858-2D446e-2D9d67-2D2ad0721b2df6&d=DwMCAg&c=j-EkbjBYwkAB4f8ZbVn1Fw&r=VvjWS1kvHI0IDtVN5nrS9SH1UlwQmnMqcMj7k4Xzdko&m=wsOOSKhhN54GkDgxY1d-bGgs1H8u8o3sAxBo_-j63sY&s=Kq5aouD7i7Jt8iHGMpVqxR-b6WJ0nDHilFL2zXj9wtI&e='}
