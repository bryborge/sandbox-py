# Sandbox (Python Edition)

A portable Python Development Environment for experimentation and glory.

## ⚙️ Dependencies

-   [Podman](https://podman.io/)

## 🔧 Up and Running

These instructions assume you have the above dependencies installed, configured,
and running.

1.  Build and run the container.

    ```sh
    make up
    ```

That's it. If you want to drop into the container at a shell, run:

```sh
make shell
```

And when you are all done using the container, spin it down:

```sh
make down
```

## 📚 Resources

-   ["Official" Python Documentation](https://www.python.org/doc/)
