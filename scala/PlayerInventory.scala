package scala

class PlayerInventory {
  protected var items: Vector[String] = Vector("lumber", "stone", "magic potion")
    
  def addToInventory(item: String): Unit = {
    items = items :+ item
    println(s"Player Inventory $item has been added so items has been changed to $items")
  }
    
  def dropFromInventory(item: String): Unit = {
    items = items.filterNot(_ == item) 
    println(s"Player Inventory $item has been dropped so items has been changed to $items")
  }

  def getItems(): Vector[String] = {
    items
  }

}

object PlayerInventory {   
  def main(args: Array[String]) = {
    
    var p: PlayerInventory = new PlayerInventory
    
    p.addToInventory("lumber")
    println(p.getItems())
    
    p.dropFromInventory("stone")
    println(p.getItems())
    
  }
}