#! /usr/bin/perl

@coins = ("quarter", "dime", "nickel");
print "@coins\n";

unshift(@coins, "dollar");
print"@coins\n";

push(@coins, "Penny");
print "@coins\n";

pop(@coins);
print "@coins\n";

shift(@coins);
print"@coins\n";
