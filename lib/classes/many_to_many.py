class Article:
    all = []  # single source of truth for all articles

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        """Immutable string between 5 and 50 characters (but no strict validation here)."""
        return self._title

    @property
    def author(self):
        """Author instance (mutable)."""
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        """Magazine instance (mutable)."""
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Immutable string > 0 characters (but no strict validation here)."""
        return self._name

    def articles(self):
        """All articles written by this author."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Unique magazines this author has written for."""
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        """Create and return a new Article."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Unique categories of magazines the author has written for, or None."""
        if not self.articles():
            return None
        return list({mag.category for mag in self.magazines()})


class Magazine:
    all = []  # keep track of all magazines

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        """Mutable string between 2 and 16 chars (no strict validation)."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        """Mutable non-empty string (no strict validation)."""
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    def articles(self):
        """All articles in this magazine."""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Unique authors who wrote for this magazine."""
        return list({article.author for article in self.articles()})

    def article_titles(self):
        """List of article titles or None."""
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        """Authors who wrote more than 2 articles in this magazine."""
        authors = [article.author for article in self.articles()]
        result = [a for a in set(authors) if authors.count(a) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        """Magazine with most articles."""
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
