Feature: Búsqueda de información académica en paginas de universidades
As a prospective student
I want to find career information on university websites
So that I can explore academic options

Scenario Outline: Búsqueda de terminos en diferentes universidades
  Given I am on the Google homepage
  When I search for "<University>"
  And I click the first Google result
  Then I should be on the "<Domain>" homepage
  When I search for "<SearchTerm>" within the university site
  Then the university site results should be related to "<SearchTerm>"

  Examples:
    | University | Domain    | SearchTerm |
    | iteso      | iteso.mx  | carreras   |
    | iteso      | iteso.mx  | posgrados  |
    | udg        | udg.mx    | carreras   |
    | unam       | unam.mx   | carreras   |

