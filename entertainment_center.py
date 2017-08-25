import media
import fresh_tomatoes

#Movie 1 - Good Will Hunting
good_will_hunting = media.Movie("Good Will Hunting",
                                       "A janitor at M.I.T., has a gift for math, but needs help from a psychologist to find direction in his life.",
                                       "http://tinyurl.com/ycocjv3a",
                                       "https://www.youtube.com/watch?v=PaZVjZEFkRs")

#Movie 2 - Fight Club
fight_club = media.Movie("Fight Club",
                                       "An underground fight club that evolves into something much, much more.",
                                       "http://tinyurl.com/ycflbsae",
                                       "https://www.youtube.com/watch?v=BdJKm16Co6M")

#Movie 3 - Shawshank Redemption
shawshank = media.Movie("Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years.",
                                       "http://tinyurl.com/yb93kqvb",
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")

#Movie 4 - Stand By Me
stand_by_me = media.Movie("Stand By Me",
                                       "After the death of a friend, a writer recounts a boyhood journey to find the body of a missing boy.",
                                       "http://tinyurl.com/l7gcxkj",
                                       "https://www.youtube.com/watch?v=oYTfYsODWQo")

#Movie 5 -  The Dark Knight
dark_knight = media.Movie("The Dark Knight",
                                       "Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                                       "http://tinyurl.com/y8wj3zyu",
                                       "https://www.youtube.com/watch?v=EXeTwQWrcwY")

#Movie 6 -  The Raid
raid = media.Movie("The Raid Redepmtion",
                                       "A S.W.A.T. team becomes trapped in a tenement run by a ruthless mobster and his army of killers and thugs.",
                                       "http://tinyurl.com/y76rvwog",
                                       "https://www.youtube.com/watch?v=6f6f_kfp1Z8")

#Creating an array in which we can add all of our movie 'objects'
movies = [good_will_hunting, fight_club, shawshank, stand_by_me, dark_knight, raid]

#Passing the movie array into a function written in the fresh_tomatoes file which will open the website and load all of our movies
fresh_tomatoes.open_movies_page(movies)
