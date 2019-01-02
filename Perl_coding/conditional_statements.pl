#!/usr/bin/perl

if($ARGV[0]&&$ARGV[1]){
	printf "two input arguments";}
elsif($ARGV[1]||$ARGV[0]){
	printf "atleast one input argument";	}

else
{	printf "no input argument";	}


