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

2.  Install dependencies (inside the container):

    ```sh
    pip install -e .
    pip install -e .[dev]
    ```

## Spinning Down

When you are all done using the container, spin it down:

```sh
make down
```

And if you'd like to clean up all the cache and generated files:

```sh
make clean
```

## 📚 Resources

-   ["Official" Python Documentation](https://www.python.org/doc/)
