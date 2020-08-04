#file to kill a process

exec { 'killProcess':
  path    => '/usr/bin/',
  command => 'pkill -f ./killmenow',
}

