from django.db import models


class Books(models.Model):
    GENRE_CHOICES = (
        ("Фантастика", "Фантастика"),
    )
    name = models.TextField(verbose_name='Укажите название книги:')
    description = models.TextField(verbose_name='Укажите описание книги:', blank=True)
    price = models.PositiveIntegerField(default=20, verbose_name='Укажите цену книги:')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода:')
    genre = models.CharField(max_length= 100, choices=GENRE_CHOICES, verbose_name='Укажите жанр книги:')
    author_email = models.EmailField(verbose_name="Укажите почту автора:", blank=True)
    author_name = models.TextField(verbose_name="Укажите имя автора:")

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "список книг"

    def __str__(self):
        return f"{self.price} $"