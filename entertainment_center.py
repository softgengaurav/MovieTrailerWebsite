#importing media module to create objects of the Movie class
import media
#importing the fresh_tomatoes.py file to access its functions
import fresh_tomatoes

#Creating an object of Movie class for the movie 'The Wizard of Oz'
TheWizardOfOz=media.Movie("The Wizard of Oz",
                          "https://imgc.allpostersimages.com/img/print/u-g-P99XZH0.jpg?w=338&h=450",
                          "https://www.youtube.com/watch?v=H_3T4DGw10U")

#Creating an object of Movie class for the movie 'Jaws'
Jaws=media.Movie("Jaws",
                 "https://previews.magnoliabox.com/magnoliabox/mb_hero/jaws001/MUS-FAPC1114_850.jpg",
                 "https://www.youtube.com/watch?v=U1fu_sA7XhE")

#Creating an object of Movie class for the movie 'The Terminator'
TheTerminator=media.Movie("The Terminator",
                          "https://cdn.shopify.com/s/files/1/1416/8662/products/terminator_1984_french_original_film_art_a_2000x.jpg?v=1539681185",
                          "https://www.youtube.com/watch?v=S9ugN8-Wsng")

#Creating an object of Movie class for the movie 'Ghost Protocol'
GhostProtocol=media.Movie("Ghost Protocol",
                         "https://m.media-amazon.com/images/M/MV5BMTY4MTUxMjQ5OV5BMl5BanBnXkFtZTcwNTUyMzg5Ng@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=hR-0po0hzDQ")

#Creating an object of Movie class for the movie 'Inception'
Inception=media.Movie("Inception",
                      "https://images-na.ssl-images-amazon.com/images/I/51ShRC1YMrL.jpg",
                      "https://www.youtube.com/watch?v=YoHD9XEInc0")

#Creating a list of all the objects of Movie class created above
movies=[TheWizardOfOz,Jaws,TheTerminator,GhostProtocol,Inception]

#calling the open_movies_page function from fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
