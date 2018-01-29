#failed requests 
exec { 'failed requests':
  command => "sudo sed -i 's/15/15000/' /etc/default/ngnix; sudo service nginx restart",
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/sbin:/usr/local/bin:/bin:/sbin',
}
