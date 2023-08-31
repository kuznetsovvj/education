import scala.io.StdIn.readInt

object Main {
  def main(args: Array[String]): Unit = {
    val v1 = readInt()
    val v2 = readInt()
    val v3 = readInt()
    val v4 = v1 * v2 * v3
    println(v4)
  }
}