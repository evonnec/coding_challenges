package scala

object MathUtils {
  def average(a: Float, b: Float): Float = (a + b) / 2

  def main(args: Array[String]) = {
    println(average(2, 1))
  }
}