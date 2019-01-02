#! /usr/bin/perl

@a = (1, 3, 'hI', "hello" );
@sent = qw/This is an array/ ;

$ar[0] = "hello";
@ar1 = qw/Mon
Tue/;
print "@a\n";
print "@sent\n";
print "@ar\n";
print"@ar1\n";

@var_10 = (1..10);
@var_20 = (1..20);

$index = 5;

@var_5 = (1..$index);
@alph = (a..z);
@alp = (A..b);

print"@var_10\n";
print"@var_20\n";
print"@var_5\n";
print"@alph\n";
print"@alp\n";
$size = @alph;
$size1 = $#alph;

print "size of alph",scalar @alph,"\n";
print "size of alph $size \n";
print "max index of $size1\n";

