from urllib.parse import quote_plus as urlquote

elk_base_url = 'elasticsearch://{user_name}:{password}@{host_ip}:{host_port}'
elastic_search_url = elk_base_url.format(user_name='derya',
                                         password=urlquote('derya17'),                                         
                                         host_ip='localhost',
                                         host_port=9200)