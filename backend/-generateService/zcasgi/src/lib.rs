use pyo3::prelude::*;
use std::convert::Infallible;
use std::net::SocketAddr;
use tokio::net::TcpListener;
use tokio::runtime::Runtime;

use http_body_util::Full;
use hyper::body::{Bytes, Incoming};
use hyper::server::conn::http1;
use hyper::service::service_fn;
use hyper::{Request, Response};
use hyper_util::rt::TokioIo;

async fn handle_request(_req: Request<Incoming>) -> Result<Response<Full<Bytes>>, Infallible> {
    let response_body = "<html><body><h1>Hello from the Rust `zcasgi` Server!</h1><p>This server is running and ready to be extended with full ASGI support.</p></body></html>";
    Ok(Response::new(Full::new(Bytes::from(response_body))))
}

async fn run_hyper_server(host: String, port: u16) {
    let addr: SocketAddr = format!("{}:{}", host, port).parse().expect("Invalid address format");
    println!("\n🚀 Production-Ready `zcasgi` Server Foundation has started!");
    println!("-> Engine: Rust with Hyper/Tokio");
    println!("-> Listening on: http://{}", addr);
    println!("-> Press Ctrl+C to stop the server.\n");

    let listener = TcpListener::bind(addr).await.expect("Failed to bind to port");

    loop {
        let (stream, _) = match listener.accept().await {
            Ok(conn) => conn,
            Err(e) => { eprintln!("Error accepting connection: {}", e); continue; }
        };

        let io = TokioIo::new(stream);

        tokio::task::spawn(async move {
            if let Err(err) = http1::Builder::new()
                .serve_connection(io, service_fn(handle_request))
                .await
            {
                eprintln!("Error serving connection: {:?}", err);
            }
        });
    }
}

#[pyfunction]
fn run_server(py: Python, host: String, port: u16) -> PyResult<()> {
    py.allow_threads(|| {
        let rt = Runtime::new().unwrap();
        rt.block_on(run_hyper_server(host, port));
    });
    Ok(())
}

#[pymodule]
fn zcasgi(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(run_server, m)?)?;
    Ok(())
}