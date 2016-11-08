import movie
import fresh_tomatoes

"""
#######################################
#   Udacity Fullstack Nanodegree      #
#   Project 1 Movie Trailer Website   #
#                                     #
#   Zeyuan (Zee) Chen                 #
#   November 8, 2016                  #
#                                     #
#   Movie Constructor                 #
#######################################

Movie constructor calls on:
    movie.py >>> movie class
    fresh_tomatoes.py >>> creates website

"""

deadpool = movie.Movie("Deadpool",
                        "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge",
                        "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                        "https://www.youtube.com/watch?v=Xithigfg7dA")
pets = movie.Movie("Secret Life Of Pets",
                     "The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes",
                     "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                     "https://www.youtube.com/watch?v=UZ4WBlveGfw")
imitation = movie.Movie("The Imitation Game",
                     "During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians",
                     "http://cdn5.thr.com/sites/default/files/2014/09/the_imitation_game_a_p.jpg",
                     "https://www.youtube.com/watch?v=S5CjKEFb-sM")
strange = movie.Movie("Doctor Strange",
                     "A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts",
                     "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                     "https://www.youtube.com/watch?v=HSzx-zryEgM")
fist_of_legend = movie.Movie("Fist Of Legend",
                     "In 1937, a Chinese martial artist returns to Shanghai to find his teacher dead and his school harassed by the Japanese",
                     "http://forgottenflix.com/wp-content/uploads/2013/01/Fist-of-Legend-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=zfZXiw-lgMs")
ip_man = movie.Movie("Ip Man",
                     "During the Japanese invasion of 1937, when a wealthy martial artist is forced to leave his home and work to support his family, he reluctantly agrees to train others in the art of Wing Chun for self-defense",
                     "http://www.topchinesemovies.com/wp-content/uploads/2012/05/Ip-Man-Movie-Poster-Three.jpeg",
                     "https://www.youtube.com/watch?v=nhz4Jl6nf58")
ip_man_2 = movie.Movie("Ip Man 2",
                     "Centering on Ip Man's migration to Hong Kong in 1949 as he attempts to propagate his discipline of Wing Chun martial arts",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM2MjY1NzMxOF5BMl5BanBnXkFtZTcwNzQ1NTcxNA@@._V1_SX640_SY720_.jpg",
                     "https://www.youtube.com/watch?v=KHAh36XUDrA")
ip_man_3 = movie.Movie("Ip Man 3",
                     "When a band of brutal gangsters led by a crooked property developer make a play to take over a local school, Master Ip is forced to take a stand",
                     "https://files.graphiq.com/7522/media/images/Ip_Man_3_2015_8048938.jpg",
                     "https://www.youtube.com/watch?v=jckXscMwIOI")
big_hero_6 = movie.Movie("Big Hero 6",
                     "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes",
                     "http://vignette1.wikia.nocookie.net/disney/images/c/ca/Big_Hero_6_poster_2.jpg/revision/latest?cb=20140611014705",
                     "https://www.youtube.com/watch?v=z3biFxZIJOQ")
inside_out = movie.Movie("Inside Out",
                     "After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school",
                     "http://static.srcdn.com/wp-content/uploads/inside-out-poster.jpg",
                     "https://www.youtube.com/watch?v=yRUAzGQ3nSY")
finding_nemo = movie.Movie("Finding Nemo",
                     "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home",
                     "https://s-media-cache-ak0.pinimg.com/originals/76/e9/bb/76e9bb65c557b261bb2e71a0dc08bd55.jpg",
                     "https://www.youtube.com/watch?v=SPHfeNgogVs")
mulan = movie.Movie("Mulan",
                     "To save her father from death in the army, a young maiden secretly goes in his place and becomes one of China's greatest heroines in the process",
                     "https://s-media-cache-ak0.pinimg.com/originals/16/5b/29/165b29d1776590f53517fa7be139a7a8.jpg",
                     "https://www.youtube.com/watch?v=MsAniqGowKE")
lion_king = movie.Movie("The Lion King",
                     "Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble",
                     "http://vignette3.wikia.nocookie.net/disney/images/c/cb/The_Lion_King_Textless_poster_1.jpg/revision/latest?cb=20140810104158",
                     "https://www.youtube.com/watch?v=4sj1MT05lAA")
wonder_woman = movie.Movie("Wonder Woman",
                     "An Amazonian princess leaves her island home to explore the world and, in doing so, becomes one of the world's greatest heroes",
                     "http://digitalspyuk.cdnds.net/15/51/768x1137/gallery-1450367372-bvs-wonderwoman-poster.jpg",
                     "https://www.youtube.com/watch?v=1Q8fG0TtVAY")
zootopia = movie.Movie("Zootopia",
                     "In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy",
                     "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                     "https://www.youtube.com/watch?v=jWM0ct-OLsM")
wreck_it_ralph = movie.Movie("Wreck It Ralph",
                     "A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives",
                     "http://www.wearemoviegeeks.com/wp-content/uploads/WIR_Ralph_BS_v5.0_Online1.jpg",
                     "https://www.youtube.com/watch?v=87E6N7ToCxs")
movies = [deadpool, imitation, strange,  wonder_woman, fist_of_legend, ip_man, ip_man_2, ip_man_3, zootopia, big_hero_6, wreck_it_ralph, inside_out, finding_nemo, pets, mulan, lion_king]
fresh_tomatoes.open_movies_page(movies) # Opens movie trailer website
