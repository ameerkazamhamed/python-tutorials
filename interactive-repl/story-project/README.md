notes: changing name to just 'story'

# Main Loop

1. Print the description (if never seen)
2. Prompt the player (You) for command input
3. Break up the command into action verb and predicate (story then custom)
4. Call the `on_<action>` handler for the Teller (meta and reserved commands)
5. Call the `begin_<action>` handler for the player (You)
6. Call the `on_<action>` method (if any) for the current Part/Area
7. Call the `on_<action>` method (if any) for the current target Item (if any)
8. Call the `on_<action>` method (if any) for any Characters in the Part/Area
9. Call the `on_<action>` method (if any) for the player (You)
10. Call the `end_<action>` method(if any) for the player (You)
11. Repeat

# Action Handler Methods

Handler methods are identified with the prefix `on_` or in the case of the
player (You) `begin_` and `end_` as well. Handlers are `@staticmethods`,
(which can optionally be decorated as such), and are always passed a single
Teller argument that they can use to get any information needed about the 
state of the current story, any areas, items or the player. Passing this
argument provides the easiest way to test individual action handlers without
the a fully initialized story.

Any one of the handlers might send the story/plot/flow to another node

# The Python Story Project

These files trace one possible path through the iterative development
of a project to create a framework for rich, interactive, text-based,
stories in which the player is the main protagonist, much like the Zork,
Myst, or the popular Stanley Parable but without graphics.

In class at SkilStak Coding Arts we simulate the challenges and efforts of
a development team from inception, through all the development iterations,
to packaging and delivery based on the idea to allow story authors to
use simple Python to write stories and code their own highly-personalized
rules, riddles, and branches coded directly in the highly readable Python
programming language (as opposed to using a limiting MUDD-like API or
learning a text-adventure pseudo-language.)

The final product of this effort is the Python 'pyrable' library,
(which itself can be used for the very reason it was conceived during
our project role-play).

This 'pyrable-project' repo contains the lesson material for each
iteration with ideas on how to role play different real-world challenges
and tasks throughout the development process including project goals,
identifying stakeholders, coming up with a domain language, then a
class model, and working through *seperation of concerns*, coupling,
decoupling, internationalization and the like.

The 'pyrable' repository is the actual, usable project itself for
those that simply want to write and code their own pyrables for others
to enjoy.

Hopefully both will provide something fun for Python coders and story
tellers of all ages.
