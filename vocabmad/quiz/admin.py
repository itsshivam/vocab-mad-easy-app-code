from django.contrib import admin
from .models import contact_details, initial_details, basic_details, word_lists, quest_list, user_stats

class initial_details_admin(admin.ModelAdmin):
    list_display = ["id", "purpose", "working", "aware", "timestamp"]
    class Meta:
        model = initial_details

class contact_details_admin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "message", "timestamp"]
    list_display_links = ["username"]
    # list_editable = ["message"]
    class Meta:
        model = contact_details

class basic_detail_admin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "name", "mobile", "profession", "gender", "timestamp", "updated"]
    list_display_links = ["username"]
    class Meta:
        model = basic_details

class word_lists_admin(admin.ModelAdmin):
    list_display = ["word", "pronunciation", "hindi", "english", "example", "synonym", "note", "mnemotrick"]
    list_display_links = ["word"]
    class Meta:
        model = word_lists

class quest_list_admin(admin.ModelAdmin):
    list_display = ["word", "question", "opt1", "opt2", "opt3", "opt4", "ans"]
    list_display_links = ["word"]
    class Meta:
        model = quest_list

class user_stats_admin(admin.ModelAdmin):
    list_display = ["username", "email", "words_completed", "questions_correct", "questions_wrong"]
    list_display_links = ["username"]
    class Meta:
        model = user_stats

admin.site.register(initial_details, initial_details_admin)
admin.site.register(basic_details, basic_detail_admin)
admin.site.register(contact_details, contact_details_admin)
admin.site.register(word_lists, word_lists_admin)
admin.site.register(quest_list, quest_list_admin)
admin.site.register(user_stats, user_stats_admin)
