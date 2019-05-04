# django-chat

## Summary
django-chat is a small application built with django 1.9, which allows users
to create an account, follow and message each other.

Demo - [django-chat](https://brightest-django-chat.herokuapp.com "djangochat")
![djangochat](https://github.com/demesvardestin/django-chat/blob/master/static/images/django_chat.png "djangochat")

## Stack
- django 1.9
- python 2.7
- bootstrap
- jQuery

## Features
- create account
- follow users
- message users

## Design
The overall app comprises 3 main components:
- authentication, with the built-in django authentication
- friendships, which allows users to follow each other 
- chatrooms, which allow users to send messages to each other

The friendship system is built using a Frienship model with two key attributes:
**created_by** and **created_for**, denoting the initiator of the follow, as well
as the recipient, respectively. The chatrooms and messages follow a one-to-many
association model. A chatroom can have many messages, while a message can belong
to only one chatroom. Users and messages also follow the same association.

## Todo
UI is currently super basic and could use some work, mostly as far as realtime
functionalities (using a framework like React or Vue). The follow functionality
needs some adjustment as far as a user's ability to unfollow a user, or accepting
or denying a follow request.