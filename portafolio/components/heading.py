import reflex as rx

def heading(text:str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        as_= "h1" if h1 else "h2"
    )