import fresh_tomatoes
import media
arrival = media.Movie("Arrival", "https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2411622421.jpg", "Jeremy Renner", "https://movie.douban.com/trailer/210754/#content")

lalaland = media.Movie("La La Land", "https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2425658570.jpg", "romatic love", "https://movie.douban.com/trailer/211786/#content")

movies = [arrival, lalaland]
# fresh_tomatoes.open_movies_page(movies)

print (media.Movie.__dict__)
