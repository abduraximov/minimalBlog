from modeltranslation.translator import translator, TranslationOptions
from .models import Post


class PersonTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')


translator.register(Post, PersonTranslationOptions)
