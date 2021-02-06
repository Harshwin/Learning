// flow control

// if else
if(1>3) println("impossible") else println("The world makes sense.")

if(1>3) {
  println("impossible")
}
else {
  println("The world makes sense.")
}

// matching
val number = 3
number match {
  case 1 => println("one")
  case 2 => println("two")
  case 3 => println("three")
  case _ => println("Something else")

}

// loops
// for loop
for (x <- 1 to 4){
  val squared = x*x
  println(squared)
}

// while
var x=10
while (x >= 0) {
  println(x)
  x-=1
}

// do while
x=0
do { println(x); x+=1}while (x<=10)

// Expressions
// to note: this below line returns a value(last line only) without
// explicitly specifying

{val x=10; x+20}

// Functions
// format def <function name>(parameter name: type...): return type={}

def square_it(x:Int):Int={
  x*x
}

square_it(2)

//functions can also take another function as input

def transform_int(x:Int, f:Int=>Int):Int={
  f(x)
}

transform_int(3, square_it)

// lambda functions or anonymous function of function literal
// using fucntions without even assigning name to it.
transform_int(3, x=> x*x)

transform_int(10, x=>x/2)



def transform_string(x:String, f:String=>String):String={
  f(x)
}

transform_string("foo", x=>x.toUpperCase)