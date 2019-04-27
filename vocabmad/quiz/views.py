from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, JsonResponse
from random import randint
import math
import codecs

from .models import contact_details, initial_details, basic_details, word_lists, quest_list, user_stats

# Create your views here.

def main_page(request):
    return render(request, "tab1.html",{})

def signup_page(request):
    return render(request, "signup.html", {})

def login_page(request):
    return render(request, "login.html", {})

def home_page(request):
    return render(request, "main.html", {})

def contact_page(request):
    return render(request, "contact.html", {})

def setting_page(request):
    return render(request, "setting.html", {})

def rough_page(request):
    return render(request, "rough.html", {})

def forget_password_page(request):
    return render(request, "forget_password.html", {})


def request_questions(request):
    if request.method == "POST":
        if request.method.is_ajax():
            username = request.POST.get("username")
            query = user_stats.objects.get(username = username)
            if query:
                word_location = query.words_completed
                query1 = quest_list.objects.all()[0:word_location]
                print query1
                c = 0
                total_questions = {}
                for quest in query1:
                    data  = {
                        "word" : quest.word,
                        "question" : quest.question,
                        "opt1" : quest.opt1,
                        "opt2" : quest.opt2,
                        "opt3" : quest.opt3,
                        "opt4" : quest.opt4,
                        "answer" : quest.ans,
                    }
                    total_questions[c] = data
                    c += 1
                return JsonResponse(total_questions)
            else:
                return HttpResponse("Invalid User")
    else:
        return HttpResponse("Page doesn't exist!!")

def request_word(request):
    if request.method == "POST":
        if request.method.is_ajax():
            username = request.POST.get("username")
            query = user_stats.objects.get(username = username)
            if query:
                word_location = query.words_completed
                query1 = word_lists.objects.all()[word_location]
                word_location += 1
                query.words_completed = word_location
                print query1.word
                query.save()
                data  = {
                    "word" : query1.word,
                    "pronunciation" : query1.pronunciation,
                    "english_meaning" : query1.english,
                    "hindi_meaning" : query1.hindi,
                    "example" : query1.example,
                    "synonym" : query1.synonym,
                    "mnemotrick" : query1.mnemotrick,
                }
                print data
                return JsonResponse(data)
            else:
                return HttpResponse("Invalid User")
    else:
        return HttpResponse("Page doesn't exist!!")

def submit_answers(request):
    if request.method == "POST":
        if request.is_ajax():
            word = request.POST.get("word")
            answer = request.POST.get("answer")
            query = quest_list.objects.get(word = word)
            if answer == query.ans:
                data = {
                    "result" : "Your answer is correct",
                }
            else:
                data = {
                    "result" : "Your answer is wrong",
                }
            return JsonResponse(data)
    else:
        return HttpResponse("Page doesn't exist")

def main_file(request):
    if request.method == "POST":
        if request.is_ajax():
            purpose = request.POST.get("purpose")
            working = request.POST.get("working")
            aware = request.POST.get("aware")
            data = {
                "purpose" : purpose,
                "working" : working,
                "aware" : aware
            }
            details = initial_details(purpose = purpose, working = working, aware = aware)
            details.save()
            return JsonResponse(data)
    return render(request, "signup.html",{})

def login_file(request):
    if request.method == "POST":
        if request.is_ajax():
            username = request.POST.get("user")
            password = request.POST.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                data = {
                    "message" : "requested user is logged in",
                    "signal" : 1,
                }
            else:
                data = {
                    "message" : "please enter correct details or go to signup page",
                    "signal" : 0,
                }
            return JsonResponse(data)

def signup_file(request):
    if request.method == "POST":
        if request.is_ajax():
            username = request.POST.get("user")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            password = request.POST.get("password")
            if User.objects.filter(email = email, username = username):
                data = {
                    "message" : "Account already exist, Please login!!!!",
                    "signal" : 0,
                }
            elif User.objects.filter(username = username):
                data = {
                    "message" : "Username already exist, use another username",
                    "signal" : 0,
                }
            elif User.objects.filter(email = email):
                data = {
                    "message" : "Email already exist, try to sign up with another email",
                    "signal" : 0,
                }
            else:
                main_otp = randint(300000,999999)
                print main_otp
                otp = 9454798442 + main_otp*47579117054007
                print otp
                data = {
                    "message" : "Welcome and experience our best content which brings you another world!!!",
                    "signal" : 1,
                    "otp" : otp,
                }
            return JsonResponse(data)

def otp_file(request):
    print "This function is working well"
    if request.method == "POST":
        if request.is_ajax():
            username = request.POST.get("user")
            email = request.POST.get("email")
            password = request.POST.get("password")
            mobile = request.POST.get("mobile")
            user_otp = int(request.POST.get("user_otp"))
            otp = int(request.POST.get("otp"))
            main_otp = (user_otp - 9454798442)/47579117054007
            print otp
            print main_otp
            if otp == main_otp:
                user = User.objects.create_user(username, email, password)
                user.save()
                query = basic_details(username = username, email = email, mobile = mobile)
                query.save()
                query1 = user_stats(username = username, email = email, mobile = mobile)
                query1.save()
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                data = {
                    "message" : "Entered otp get matched",
                    "signal" : 1
                }
            else:
                data = {
                    "message" : "Entered otp is wrong, Please signup again",
                    "signal" : 0,
                }
            return JsonResponse(data)

def verify_email(request):
    if request.method == "POST":
        if request.is_ajax():
            email = request.POST.get("email")
            query = User.objects.filter(email = email)
            if query:
                main_otp = randint(300000,999999)
                print main_otp
                otp = 9454798442 + main_otp*47579117054007
                print otp
                data = {
                    "message" : "Your account is registerd, please enter otp which we sent on your email id",
                    "signal" : 1,
                    "otp" : otp,
                    "email" : email,
                }
            else:
                data = {
                    "message" : "Your account is not registered, please signup or login with other account",
                    "signal" : 0,
                }
            return JsonResponse(data)

def verify_otp(request):
    if request.method == "POST":
        if request.is_ajax():
            otp = int(request.POST.get("otp"))
            main_otp = int(request.POST.get("main_otp"))
            real_otp = (otp - 9454798442)/47579117054007 #int(math.ceil())
            print real_otp
            print main_otp
            if real_otp == main_otp:
                data={
                    "message" : "Your entered otp get matched!!",
                    "signal" : 1,
                }
            else:
                data = {
                    "message" : "Your entered otp didn't get matched!! Try again!",
                    "signal" : 0,
                }
            return JsonResponse(data)

def change_password(request):
    if request.method == "POST":
        if request.is_ajax():
            password = request.POST.get("password")
            email = request.POST.get("email")
            query = User.objects.get(email = email)
            query.set_password(password)
            query.save()
            data = {
                "message" : "Your password has been changed!!",
            }
            return JsonResponse(data)

def contact_file(request):
    if request.method == "POST":
        if request.is_ajax():
            username = request.POST.get("user")
            email = request.POST.get("email")
            message = request.POST.get("message")
            contact = contact_details(username = username, email = email, message = message)
            contact.save()
            data = {
                "message" : "Your message has been sent to us!!, We'll reply soon",
            }
            return JsonResponse(data)

def setting_file(request):
    if request.method == "GET":
        if request.is_ajax():
            username = request.user.get_username()
            print username
            query = basic_details.objects.get(username = username)
            data = {
                "email" : query.email,
                "name" : query.name,
                "mobile" : query.mobile,
                "profession" : query.profession,
                "gender" : query.profession,
            }
            return JsonResponse(data)
    elif request.method == "POST":
        if request.is_ajax():
            email = request.POST.get("email")
            name = request.POST.get("name")
            mobile = request.POST.get("mobile")
            profession = request.POST.get("profession")
            gender = request.POST.get("gender")
            query = basic_details.objects.get(email = email)
            query.name = name
            query.mobile = mobile
            query.profession = profession
            query.gender = gender
            query.save()
            return HttpResponse("Your details have been saved")

def upload_quest(request):
    if request.user.is_superuser:
        f1 = codecs.open("quest_initial.txt", encoding = "utf-8")
        question_list = []
        def new_quest(line):
            if "Q." in line:
                return 1
            elif "1." in line:
                return 2
            elif "2." in line:
                return 3
            elif "3." in line:
                return 4
            elif "4." in line:
                return 5
            elif "Ans." in line:
                return 6
            else:
                return 0
        quest = []
        for line in f1:
            verify = new_quest(line)
            if verify == 0:
                quest.append(line)
            elif verify == 1:
                quest.append(line[3:])
            elif verify == 2:
                quest.append(line[3:])
            elif verify == 3:
                quest.append(line[3:])
            elif verify == 4:
                quest.append(line[3:])
            elif verify == 5:
                quest.append(line[3:])
            elif verify == 6:
                quest.append(line[5:])
                question_list.append(quest)
                quest = []
            else:
                quest.append(line)
        f1.close()
        for quest in question_list:
            word = quest[0]
            find_word = quest_list.objects.filter(word = word)
            if find_word:
                continue
            else:
                question = quest[1]
                opt1 = quest[2]
                opt2 = quest[3]
                opt3 = quest[4]
                opt4 = quest[5]
                ans = quest[6]
                query = quest_list(word = word, question = question, opt1 = opt1, opt2 = opt2, opt3 = opt3, opt4 = opt4, ans = ans)
                query.save()
        return HttpResponse("Questions have been uploaded")
    else:
        return HttpResponse("Page not found")

def upload_words(request):
    if request.user.is_superuser:
        f1 = codecs.open("word_list.txt", encoding = "utf-8")
        def word(line):
            if "Word:" in line:
                return True
            else:
                return False
        word_knowledge = []
        word_list = []
        for line in f1:
            if word(line):
                word_list.append(word_knowledge)
                word_knowledge = []
                word_knowledge.append(line)
            else:
                word_knowledge.append(line)
        f1.close()
        word_list.pop(0)
        for word in word_list:
            main_word = ""
            hindi = ""
            pronunciation = ""
            mnemotrick = ""
            synonym = ""
            note = ""
            english = ""
            example = ""
            for line in word:
                if "Word:" in line:
                    main_word = line[5:]
                if "Hindi meaning:" in line:
                    hindi = line[15:]
                if "Pronunciation:" in line:
                    pronunciation = line[15:]
                if "Mnemonic trick" in line:
                    mnemotrick += "@ "
                    mnemotrick += line[15:]
                if "Synonym:" in line:
                    synonym = line[9:]
                if "EngMean" in line:
                    if " Ex " in line:
                        example += "@"
                        example += line[10:]
                    else:
                        english += "@"
                        english += line[7:]
                if "Note:" in line:
                    note = line[5:]
            find_word = word_lists.objects.filter(word = main_word)
            if find_word:
                continue
            else:
                query = word_lists(word = main_word, hindi = hindi, pronunciation = pronunciation, mnemotrick = mnemotrick, synonym = synonym, note = note, example = example, english = english)
                query.save()
        return HttpResponse("Your words have been uploaded")
    else:
        return HttpResponse("Page not found")
