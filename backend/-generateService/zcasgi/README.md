# zcasgi: Zero-Copy ASGI WebSocket Server

## 1. Overview

`zcasgi` is a high-performance, specialized ASGI-compliant server written in Rust, designed to be used as a library within a Python application. Its sole purpose is to handle WebSocket connections with maximum efficiency by leveraging Rust's performance characteristics and memory safety.

The name `zcasgi` stands for **Z**ero-**C**opy **A**SGI. It is engineered to minimize or eliminate the data copying that typically occurs when a high-level language like Python interfaces with low-level network sockets, which is a common performance bottleneck.

This module is the performance core of the `-chatService`.

## 2. The Problem Solved

Standard Python ASGI servers like Uvicorn or Daphne are excellent for general-purpose use. However, under extremely high-concurrency scenarios with thousands of persistent WebSocket connections (e.g., a large-scale chat application), the overhead of the Python Global Interpreter Lock (GIL) and data marshalling between the network buffer and Python objects can become a limiting factor.

`zcasgi` solves this by:
1.  **Handling the WebSocket protocol entirely in Rust:** Bypassing Python for the frame parsing, masking, and protocol management.
2.  **Using a Zero-Copy approach:** Data is passed between the operating system's socket buffer and the Python application with minimal copying, reducing CPU load and latency.
3.  **Leveraging Rust's concurrency:** Utilizing Rust's fearless concurrency to manage many connections simultaneously without the limitations of the Python GIL.

This results in significantly higher throughput, lower memory usage per connection, and greater stability under heavy load compared to a pure-Python implementation.

## 3. Architecture & Usage

`zcasgi` is not a standalone server. It is compiled as a Rust library with a Python-compatible foreign function interface (FFI).

1.  The main Python application in the `-chatService` (e.g., `start_zcasgi.py`) imports and initializes this Rust library.
2.  The library is passed the Python `socketio` application object.
3.  `zcasgi` takes over the low-level socket handling, listening for and accepting new WebSocket connections.
4.  When a new message arrives, `zcasgi` processes the WebSocket frame and passes the clean, unmasked payload up to the Python `socketio` application for business logic processing.
5.  When the Python application sends a message, it hands it off to the `zcasgi` library, which handles the WebSocket framing and sends it over the socket.

## 4. Building the Module

The module is built using Rust's standard build tool, `cargo`.

**Prerequisites:**
- Rust toolchain (install via `rustup`)

**Build Command:**
From within this directory (`backend/-chatService/zcasgi/`), run:
```bash
cargo build --release
```

This will produce a compiled library file (e.g., `libzcasgi.so` or `libzcasgi.dylib`) in the `target/release` directory. The Python application is configured to load this shared library. The build process is automatically handled by the service's `Dockerfile`.
