use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};


include!("lib.rs");
include!("server/server.rs");
include!("http/handler/handler.rs");

fn main() {
    start("127.0.0.1:8080".to_string());
}
