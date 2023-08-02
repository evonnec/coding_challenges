package scala
import scala.collection.Iterable

object LanguageTeaching {
  
  class LanguageStudent {
    var languages: Iterable[String] = Iterable()

    def getLanguages(): Iterable[String] = {
      languages
    }
    def addLanguage(language: String): Unit = {
      languages = languages ++ Iterable[String](language)
      println(s"languages are now $languages")
    }
   }

  class LanguageTeacher extends LanguageStudent { 

    def teach(student: LanguageStudent, languageToLearn: String): Boolean = {
      if (languages.toSeq.contains(languageToLearn)) {
        student.addLanguage(languageToLearn)
        true
      } else {
        false
      }
    }
    
  }
  
  def main(args: Array[String]): Unit = {
    // Example case

    val teacher = new LanguageTeaching.LanguageTeacher
    teacher.addLanguage("English")
    teacher.addLanguage("Spanish")
    
    val student = new LanguageTeaching.LanguageStudent
    student.addLanguage("Cantonese")
    teacher.teach(student, "English")
 
    for(language <- student.getLanguages())
      System.out.println(s"student language: $language");

    for(language <- teacher.getLanguages())
      System.out.println(s"teacher language: $language");
    
  }
   
}