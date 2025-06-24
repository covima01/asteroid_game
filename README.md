Asteroid Game

Python / Pygame 2.6.1

Asteroid Game was my first attempt at creating a Python program using Pygame. The goal was to familiarize myself with the Pygame library and learn how to write clean code spread across multiple files using
object oriented programming. As you can imagine, this is a basic replica of the classic game "Asteroids". As such it borrows the style of gameplay, the physics, and the overall flow and gameplay of the original.

Key Features - Modular Multi-File Architecture - This project is structured across multiple Python files to emphasize clean code and scalability.

Object Oriented Design - The focus of this project revolved around learning how classes, objects, and inheritance work. As such, some of the more complex lines of code were provided by Boot.dev, while the rest of it was written by myself.

Skills Demonstrated - Writing, organizing, and managing multi-file Python projects. Implementing object-oriented principles. 

Challenges and Solutions - The biggest challenge I faced was learning how all of the different classes and objects interact with each other to create a cohesive game. I went through this project as a complete beginner, so this was a real challenge. The solution included extensive external research, trial and error, and gradual familiarization with OOP and what it entails. Specifically, I ran into an issue when incpororating shot velocity. Initially, when I would shoot, my entire player object would shoot forward with the projectile. I learned that self.position is a pygame.Vector2.object. When I was passing it to shot, both the player and the shot were sharing the same Vector2 instance. I had to create a copy of the Vector2 instance for each shot to get it to work properly.

Outcome - By the end of this project, I had built a fully functional game that utilized the foundational principles of OOP. I learned so much and, although frustrating at times, I persevered and am better for it. I look forward to moving on to a new project for now and will return to this asteroid game for updates in the future.

 
