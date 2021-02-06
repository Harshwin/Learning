// Values are immutable constants
val hello : String = "Hola!"

// Variables are mutable

var hello_there : String = hello
//hello_there="hi"
println(hello_there)

// Data types

val number_one: Int =1
val truth: Boolean = true
val letter_a: Char='a'
val pi: Double=3.14159265
val pi_single_precision:Float = 3.14159265f
val small_number:Byte = 127
println(" here is a statement: " + truth+ pi )
println(f"Pi is about $pi_single_precision%.5f")

// Booleans

val check_greater = 1>2
val check_lesser = 1<2
val compare = check_greater && check_lesser
val compare_bitwise = check_greater & check_lesser

val compare_string = 'a'=='a'
val compare_string: Boolean = 'a'=='a'

// regular expressions

val ultimate_answer: String = "To life, universe and everything is 42"
val pattern = """.*([\d+]).*""".r
val pattern(answer_string) = ultimate_answer

val answer = answer_string.toInt
println(answer)

