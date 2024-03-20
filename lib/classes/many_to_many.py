class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters inclusive")
        self._title = title
        
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        self._author = author
        
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = magazine
        
        author._add_article(self)
        magazine._add_article(self)

        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = value
        
class Author:
    def __init__(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []
        self._magazines = set()

    @property
    def name(self):
        return self._name

    def _add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("article must be an instance of Article")
        self._articles.append(article)
        self._magazines.add(article.magazine)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(self._magazines)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self._magazines)) if self._magazines else None

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)  
        return article 

class Magazine:
    def __init__(self, name, category):
        if not (2 <= len(name) <= 16) or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string of 2 to 16 characters")
        if not category or not isinstance(category, str):
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return  
        if not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be a string of 2 to 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def _add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributors(self):
        return list({article.author for article in self._articles})

    def contributing_authors(self):
        if not self._articles:
            return None 

        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        filtered_authors = [author if count > 2 else None for author, count in author_counts.items()]
        return filtered_authors
