Quick Start
===========

This section provides a quick start guide for using the library in different environments.

The library provides three ways to store and retrieve keys:

1. **Locally**: You can generate a key locally and save it to a `key.properties` file. This option is most suitable for local or educational projects.

2. **Retrieve the key from a remote store and save it locally**: This option is suitable when you are working in a local development environment and do not need to access the remote store every time.

3. **Retrieve the encryption key from a remote store without saving it**: 
   If you are using the library for educational purposes, you can use the option to generate encryption keys locally and store them in local files.

   Important: Do not forget to add the path to secrets in `.gitignore`.

.. toctree::
   :titlesonly:
   :glob:

   local
   remote

