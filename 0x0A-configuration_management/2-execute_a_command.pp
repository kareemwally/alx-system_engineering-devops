# kill all processes

exec { 'killmenow_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
