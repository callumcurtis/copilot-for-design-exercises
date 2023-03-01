# Question 4

## Description

You are designing the software for a bookstore. There is a single object structure, `Book`, but the number of operations performable on instances of `Book` is likely to increase indefinitely. You are tasked with using the visitor pattern to support this requirement and implement the first visitor, which should find the total number of pages in the [`chapters`](Chapter.java) and [`dedication`](Dedication.java) (not [`title page`](TitlePage.java) or [`afterword`](Afterword.java)).

## Criteria

Add a main method to your visitor class that creates a book with:

* 7 page dedication
* 4 chapters
    * Chapter 1 having 675 pages
    * Chapter 2 having 98 pages
    * Chapter 3 having 842 pages
    * Chapter 4 having 524 pages
* 37 page afterword

and show that your visitor calculates the correct number of pages.