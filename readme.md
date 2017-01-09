COMP3207 second coursework

# API Specification
All calls are to the root of the project (/). The calls are all POST only (although GET requests are often used to the same URLs in other places) and return plain text.

## Graphics processing

### /draw
Adds a graphic to a Mathboard

Input:
 - Room name [room::integer] - The 4 digit identifier of the room to be drawn too
 - Data string of all graphics [data::string] - The data string (see description below..)

Output:
 - Nothing, this call should just return a blank page

### /view
Retrieves the graphics of a Mathboard

Input:
 - Room name [room::integer] - The 4 digit identifier of the room to be drawn too

Output:
 - Data string of all graphics [data::string] - The data string (see description below..)
 
## Comments (chat) processing
 
### /comment
Retrieves the graphics of a Mathboard

Input:
 - Room name [room::integer] - The 4 digit identifier of the room to be drawn too
 - New comment [comment::string] - The new comment written by the client

Output:
 - All comments (as one string) [plain text] - All the comments to be printed on the client

# The data string
This is very big and a tad ugly, but it simply contains the entire graphics data of a Mathboard. The individual objects are JSON encoded strings, and are delimited by a fairly long string that should never be in the graphics data.
