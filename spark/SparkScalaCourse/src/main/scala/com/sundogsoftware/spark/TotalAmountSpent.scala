package com.sundogsoftware.spark

import com.sundogsoftware.spark.FriendsByAge.parseLine
import org.apache.log4j.{Level, Logger}
import org.apache.spark.SparkContext

object TotalAmountSpent {

  /** A function that splits a line of input into (user_ID, amount_spent) tuples. */
  def parseLine(line: String): (Int, Float) = {
    // Split by commas
    val fields = line.split(",")
    // Extract the age and numFriends fields, and convert to integers
    val user_ID = fields(0).toInt
    val amount_spent = fields(2).toFloat
    // Create a tuple that is our result.
    (user_ID, amount_spent)
  }

  /** Our main function where the action happens */
  def main(args: Array[String]): Unit ={
    Logger.getLogger("org").setLevel(Level.ERROR)

    // Create a SparkContext using every core of the local machine
    val sc = new SparkContext(master="local[*]", appName = "TotalAmountSpent" )

    // Load each line of the source data into an RDD
    val lines = sc.textFile("data/customer-orders.csv")

    // parselines to get to tuples (user_ID, amount_spent)
    val rdd = lines.map(parseLine)

    val totalsByUserID = rdd.reduceByKey( (x,y) => x+y)


    // Collect the results from the RDD (This kicks off computing the DAG and actually executes the job)
    val results = totalsByUserID.collect()

    // Sort and print the final results.
//    results.sortBy(_._2).foreach(println)

    val resultsFlipped = results.map( x => (x._2, x._1))
    resultsFlipped.foreach(println)

  }

}
