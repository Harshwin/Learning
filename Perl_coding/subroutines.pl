#!/usr/bin/perl

sub average {

	$n=scalar(@_);
	$sum =0;

	foreach $item (@_){
		$sum +=$item;	}
	$avg=$sum/$n;

	printf "Average is $avg \n";
}

&average(@ARGV);
