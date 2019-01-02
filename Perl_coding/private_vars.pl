#! /usr/bin/perl
$string = "hehehe";

sub rand{
	my $string = "hello";
	printf "inside function : $string \n";
}

&rand();

printf "outside function : $string \n";
