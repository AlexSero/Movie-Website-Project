import media
import fresh_tomatoes


def main():

    """defines a function which stores moveis that can be displayed on the website"""  # noqa

    toy_story_3 = media.Movie(
        'Toy Story 3',
        'A story of a boy and his toys that come to life',
        'https://pics.filmaffinity.com/toy_story_3-691147043-large.jpg',
        'https://www.youtube.com/watch?v=JcpWXaA2qeg',
        'G',
        'June 18, 2010',
        )

    transformers_5 = media.Movie(
        'Transformers 5',
        'Optimus Prime goes evil',
        'https://i2.wp.com/teaser-trailer.com/wp-content/uploads/Transformers-5-Two-Worlds-Collide.jpg?ssl=1',  # noqa
        'https://www.youtube.com/watch?v=o208m8c1jow',
        'PG-13',
        'June 21, 2017',
        )

    matrix = media.Movie(
        'The Matrix',
        'The world is a simulation',
        'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
        'https://www.youtube.com/watch?v=vKQi3bBA1y8',
        'R',
        'March 31, 1999',
        )

    Schindler_s_List = media.Movie(
        "Schindler's List",
        'Businessman Oskar Schindler saves hundreds of innocent jews',
        'https://lh3.googleusercontent.com/-WrkylZR-_JU/Vm_lwcO7hcI/AAAAAAAAjVg/ocoIjZ7GUZA/w1024-h1516/schindlers%2Blist%2Bposter.png',  # noqa
        'https://www.youtube.com/watch?v=x4mxQV_NH1g',
        'R',
        'December 15, 1993',
        )

    spectre = media.Movie(
        'Spectre',
        'A James Bond movie',
        'https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg',
        'https://www.youtube.com/watch?v=vBnGxAkdh_k',
        'PG-13',
        'October 26, 2015',
        )

    res_evil = media.Movie(
        'Resident Evil',
        'Zombie-causing virus escapes from the lab',
        'https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg',  # noqa
        'https://www.youtube.com/watch?v=u6uDnd_v5Bw',
        'R',
        'March 15, 2002',
        )

    movies = [
        toy_story_3,
        transformers_5,
        matrix,
        Schindler_s_List,
        spectre,
        res_evil,
        ]

    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
