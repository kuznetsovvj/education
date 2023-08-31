import scala.io.StdIn.readInt

object Main {
  def main(args: Array[String]): Unit = {
    val v1 = readInt()
    val v2 = readInt()
    val v3 = v1 - v2
    println(v3)
  }
}