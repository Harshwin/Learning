#!/usr/bin/perl

%data = ('John' , 23 , 'Paul' , 10 , 'Lisa',41);
print "\$data{'John'} = $data{'John'}\n";
print "$data{'Lisa'}\n";

@names = keys %data;
print "@names\n";

$size = @names;
print "Hash ize - $size \n";

#adding elements to hash
$data{'Ali'} = 55;
@names = keys %data;
$size = @names;
print "@names\n";
print "Hash size - $size \n";

# removing elements from hash
delete $data{'Lisa'};
@names = keys %data;
$size = @names;
print "@names\n";
print "Hash size - $size\n";
