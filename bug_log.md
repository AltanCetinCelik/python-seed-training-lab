Date: 2026-06-19

Project:
Temporary Seed Memory

Bug/Lesson:
My filter check was inside the for loop at first.

Cause:
I checked whether filtered_memories was empty before the loop had finished searching all memories.

Fix:
I moved the empty-check after the for loop.

Lesson:
When filtering, first collect/check all items. Only after the loop ends should I decide whether there were no matches.