//Data structures
// tuples
// immutable Lists
//tuple can hold different data types

val random_stuff = ("hello", "this", "007")
println(random_stuff)

println(random_stuff._1)

// key value pair
val random_stuff_keys = "first"->"hello"
println(random_stuff_keys._2)

// lists
// must be of same data types
// zero based index

val num_list = List(1, 2, 3, 4, 5)
println(num_list(1))

for (num<-num_list){println(num)}

val str_list = List("one", "two", "three")
val backward_list = str_list.map((number:String)=>{number.reverse})

// reduce() to combine all the items in a collection

val sum = num_list.reduce((x:Int, y:Int)=> x+y )

// filter() removes stuff

val remove_even = num_list.filter((x:Int)=> x%2!=0)

// underscore is like a place holder for all elements in the list
val remove_even_another_way = num_list.filter(_ % 2 != 0)

val list_more_num = List(6, 7, 8)
val combine_list = list_more_num ++ num_list.reverse
val sorted = combine_list.sorted

// maps or dictionaries

val num_map = Map(1->"one", 2->"two", 3->"three")
println(num_map(2))

val rdd_val = sc.parallelize(List(1, 2, 3, 4))
val squares = rdd_val.map(x=>x*x)