# Fixes error 500 on wordpress runnig on apache2
exec { 'fix error 500':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
