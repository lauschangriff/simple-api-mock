class NetflixItem:
    def __init__(self, show_id, type, title, director, cast, country, date_added, release_year, rating, duration,
                 listed_in, description):
        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.duration = duration
        self.listed_in = listed_in
        self.description = description
        self

    def __repr__(self):
        return (
            'NetflixItem ('
            f'show_id: {self.show_id}, '
            f'type: {self.type}, '
            f'title: {self.title}, '
            f'director: {self.director}, '
            f'cast: {self.cast} ,'
            f'country: {self.country}'
            f'date_added: {self.date_added}, '
            f'release_year: {self.release_year}, '
            f'rating: {self.rating}, '
            f'duration: {self.duration}, '
            f'listed_in: {self.listed_in} ,'
            f'description: {self.description})'
        )

        def to_json(self):
            return self.__dict__
