import scala.io.StdIn

object Main {
  def main(args: Array[String]): Unit = {
    var i = true
    while (i) {
      println("Enter real unit of first number")
      val r1 = StdIn.readInt()
      println("Enter imaginary unit of first number")
      val i1 = StdIn.readInt()
      println("Enter read unit of second number")
      val r2 = StdIn.readInt()
      println("Enter imaginary unit of second number")
      val i2 = StdIn.readInt()
      println("Enter operation")
      val line = StdIn.readChar()
      if (line == '+') {
        val rr = r1 + r2
        val ir = i1 + i2
        println(s"result: $rr + $ir * i")
      }
      if (line == '-') {
        val rr = r1 - r2
        val ir = i1 - i2
        println(s"result: $rr + $ir * i")
      }
      if (line == '*') {
        val rr = r1 * r2
        val ir = i1 * i2
        println(s"result: $rr + $ir * i")
      }
      println("Continue?")
      if (line != 'Y') {
        i = false
      }
    }
  }
}