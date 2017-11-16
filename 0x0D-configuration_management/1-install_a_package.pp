#Using Puppet, install puppet-lint

package {'puppet-lint':
  ensure => installed,
  require => '2.1.1',
  provider => gem,
}

