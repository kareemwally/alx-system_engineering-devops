# creates file using puppet
file { '/tmp/school':
	ensue => 'file',
	group =>'www-data',
	content =>'I love Puppet',
	mode =>'0744',
	owner =>'www-data',
	}
