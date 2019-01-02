#!/usr/bin/perl

@thing ="/a:b/c/ef:ghi]jk/lmnopqrstuvw/xyz";
$check = \@thing;
$check1=\@_;

#print "@thing \n";
#print "$check\n";


#print "@_\n";
#print "$check1\n";

print split(':',@thing,-1);
#$arr1=split('b',@thing);

print "@thing\n";

print "@arr\n";
print "$arr1\n";

