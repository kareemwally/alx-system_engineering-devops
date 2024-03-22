file { '/tmp/school':
	ensue => 'file',
	owner =>'www-data',
	group =>'www-data',
	content =>'I love Puppet',
	moed =>'0744',
	}
