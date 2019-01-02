#!/usr/bin/perl

@num = (1..20);
print "@num\n";

splice (@num,3,4);
print "@num\n";

splice(@num,5,3, "a","B",0000);
print "@num\n";

@food =("pizza", "burger", "steak", "chicken");
print "@food\n";

@food = sort(@food);
print"@food\n";

@food =("pizza", "burger", "steak", "chicken","Chicken","Dosa");
print "@food\n";

@food = sort(@food);
print"@food\n";

@merged=(@food, @num);
print"@merged\n";


@var =(5,4,3,2,1,0)[0..2];
print "@var\n";

