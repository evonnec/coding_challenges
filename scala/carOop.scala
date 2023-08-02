package scala
/*
https://www.baeldung.com/scala/classes-objects
*/

object App {
  def main(args: Array[String]): Unit = {
    var engine: String = s"V6"
    var wheels: Int = 4
    var color: String = s"Red"
    var car: DIYCarBuilder = new DIYCarBuilder(DIYengine=engine, DIYwheels=wheels, DIYcolor=color)
  
    car.setEngine(engine)
    car.setWheels(wheels)
    car.setColor(color)
    car.build()
    println(car)
  }
}

// Builder Interface
trait CarBuilder {

  var engine: String = ""
  var wheels: Int = 0
  var color: String = ""
  
  case class Car(engine: String, wheels: Int, color: String)

  def setEngine(engine: String): Unit

  def setWheels(wheels: Int): Unit

  def setColor(color: String): Unit

  def build(): Car
}

// Concrete Builder
class DIYCarBuilder(var DIYengine: String, var DIYwheels: Int, var DIYcolor: String) extends CarBuilder {
  
  def setEngine(DIYengine: String): Unit = {
    engine = DIYengine
  }

  def setWheels(DIYwheels: Int): Unit = {
    wheels = DIYwheels
  }

  def setColor(DIYcolor: String): Unit = {
    color = DIYcolor
  }

  def build(): Car = {
    engine = engine;
    wheels = wheels;
    color = color;
    println(s"Car is built: engine is $engine, wheels is $wheels, color is $color")
    Car(engine=engine, wheels=wheels, color=color)
  }
}
