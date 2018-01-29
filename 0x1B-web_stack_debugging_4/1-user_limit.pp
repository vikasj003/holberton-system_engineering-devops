#set limits https://access.redhat.com/solutions/61334 
exec { 'limits':
  command => "sudo sed -i 's/4/6000/' /etc/security/limits.conf",
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/sbin:/usr/local/bin:/bin:/sbin',
}
