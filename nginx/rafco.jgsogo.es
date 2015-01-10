server {
    listen 80;
    server_name rafco.jgsogo.es;
    access_log /home/javi/projects/muia_linkeddata/logs/nginx_access.log;
    error_log /home/javi/projects/muia_linkeddata/logs/nginx_error.log;

    # Make sure files with the following extensions do not get loaded by nginx because nginx would display the source code, and these files can contain PASSWORDS!
    location ~* \.(engine|inc|info|install|make|module|profile|test|po|sh|.*sql|theme|tpl(\.php)?|xtmpl)$|^(\..*|Entries.*|Repository|Root|Tag|Template)$|\.php_ {
        deny all;
        }

    # Deny all attempts to access hidden files such as .htaccess, .htpasswd, .DS_Store (Mac).
    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
        }

    # Virtuoso SPARQL endpoint
    location /sparql/ {
	proxy_pass http://localhost:8890;
	include /etc/nginx/proxy.conf;
	}

    # phpMyAdmin
    location /phpmyadmin/ {
	proxy_pass http://127.0.0.1:8080;
	include /etc/nginx/proxy.conf;
        }

    # Ontology
    location =/datosabiertos/def/rafco.rdf { alias /home/javi/projects/muia_linkeddata/ontology/rafco.rdf;	}
    location =/datosabiertos/def/rafco.owl { alias /home/javi/projects/muia_linkeddata/ontology/rafco.owl; }
    location =/datosabiertos/def/rafco.ttl { alias /home/javi/projects/muia_linkeddata/ontology/rafco.ttl; }

    # Django resolves content negotiation for the ontology file
    location =/datosabiertos/def/rafco {
	proxy_pass http://127.0.0.1:9011;
        include /etc/nginx/proxy.conf;
        }

    # Elda
    location /standalone/ {
	rewrite ^/standalone/(.*)$ /datosabiertos/$1 permanent;
	}
    location /datosabiertos/ {
	proxy_set_header Host $http_host;
        proxy_pass http://localhost:8891/standalone/;
	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        #include /etc/nginx/proxy.conf;
        }

    # Django
    location / {
        proxy_pass http://127.0.0.1:9011;
        include /etc/nginx/proxy.conf;
        }
    location /static/ {
        root /home/javi/projects/muia_linkeddata/webapp/;
        }

}
