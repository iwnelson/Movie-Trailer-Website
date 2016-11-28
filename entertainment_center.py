import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        ("A boy's LSD induced dream sequence about his world "
                         "becoming an animated one where his toys come to "
                         "life and realize the stories they have been fed "
                         "their whole lives are a sham"),
                        ("https://upload.wikimedia.org/wikipedia/en/1/13/"
                         "Toy_Story.jpg"),
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

road_house = media.Movie("Road House",
                         ("Swayze is a bouncer with a troubled past that can "
                          "save the fate of any bar he walks into .... this "
                          "time, he tries to save his world."),
                         ("https://static1.squarespace.com/static/"
                          "53323bb4e4b0cebc6a28ffa2/t/55f06c09e4b0a5f28739f4bf"
                          "/1441819658462/"),
                         "https://www.youtube.com/watch?v=CO44a96lyWE")

your_highness = media.Movie("Your Highness",
                            ("idk .... there really isn't any plot good enough"
                             "to spend time writing about"),
                            ("https://upload.wikimedia.org/wikipedia/en/thumb/"
                             "3/31/Your_Highness_Poster.jpg/"
                             "220px-Your_Highness_Poster.jpg"),
                            "https://www.youtube.com/watch?v=FplWxtPzWY8")

the_interview = media.Movie("The Interview",
                            ("James Franco is a celebrity news anchor and "
                             "Seth Rogen has annoying laugh .... some other "
                             "stuff happens and they get to ride in a boat "
                             "with a cute puppy"),
                            ("https://upload.wikimedia.org/wikipedia/en/2/27/"
                             "The_Interview_2014_poster.jpg"),
                            "https://www.youtube.com/watch?v=frsvWVEHowg")

imitation_game = media.Movie("The Imitation Game",
                             "BAHHHHHHH! CHRISTOPHER!!!! BAHHHHHHH!",
                             ("https://images-na.ssl-images-amazon.com/images"
                              "/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk"
                              "3MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg"),
                             "https://www.youtube.com/watch?v=S5CjKEFb-sM")

top_gun = media.Movie("Top Gun",
                      "Goose totally survives",
                      ("https://images-na.ssl-images-amazon.com/images/I/"
                       "710nsn-AYoL._SY445_.jpg"),
                      "https://www.youtube.com/watch?v=qAfbp3YX9F0")

movies = [toy_story, road_house, your_highness, the_interview,
          imitation_game, top_gun]

fresh_tomatoes.open_movies_page(movies)
