#create a manifest that kills a process named killmenow
exec { 'killmenow':
  path    => '/usr/bin:/usr/sbin:/bin',
  onlyif  => 'pgrep -f killmenow'
  command => 'pkill -f killmenow',
}
