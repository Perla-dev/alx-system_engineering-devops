exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

# Ensure the Nginx service is enabled and running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Create an Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => '
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }

        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
',
  require => Package['nginx'],
  notify  => Service['nginx'],
}




