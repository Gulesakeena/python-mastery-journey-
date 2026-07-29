# 40 - Polymorphism

## Theory

1. What is polymorphism?
2. Why do we use polymorphism?
3. Explain "One Interface, Many Forms."
4. Difference between polymorphism and inheritance.
5. What is runtime polymorphism?
6. What is duck typing?
7. Explain operator overloading.
8. Is Python compile-time or runtime polymorphic?
9. Give three real-world examples of polymorphism.
10. Why is polymorphism better than many if-else statements?

---

## Coding Questions

1. Create Animal, Dog, and Cat classes using polymorphism.
2. Demonstrate method overriding.
3. Create two classes with the same method and use duck typing.
4. Show polymorphic behavior using a list of objects.
5. Demonstrate operator overloading using built-in types.

---

## Interview Challenge

Build a Notification System.

Classes:

- Notification (Base Interface)
- EmailNotification
- SMSNotification
- PushNotification

Requirements:

- Each class must implement a send() method.
- Store all notification objects in one list.
- Iterate through the list and call send().
- No if-else statements should be used to determine the notification type.
- Explain why this demonstrates polymorphism.