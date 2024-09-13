Discussion board for cs50w projects.

Wiriting this Read Me as I go along, will be refactored in the end of the project


Features to implement:

Login -> Done
Register -> Done
Logout - > Done
Homepage with each project picture -> In progress
    * Clickable cards
    * More info button
Individual Project Page
Chat for each project


Dependencies:
 Channels
    Channels help us to create a socket application and enable us to do real-time chat applications. Channels in Django help maintain the normal synchronous behavior of the framework while also allowing for asynchronous protocols. This means developers can create views that are either synchronous, asynchronous, or a mix of both. Channels enable applications to handle "long-running connections," which can be crucial for tasks like real-time updates.

 Daphne
    We also need Daphne to make the channel work in development mode

Websockets
    WebSocket is a computer communications protocol, providing a simultaneous two-way communication channel over a single Transmission Control Protocol (TCP) connection.
    In Django Channels, a WebSocket consumer is a class that handles the WebSocket connections and defines how to respond to incoming messages. To create a consumer, you’ll need to create a new file in your Django app’s consumers directory: