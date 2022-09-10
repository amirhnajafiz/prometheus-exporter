pub fn start(address: String) {
    // creating a TCP listener
    let listener = TcpListener::bind(address).unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }
}