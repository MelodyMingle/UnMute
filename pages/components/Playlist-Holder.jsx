function Playlist({ title, children }) {
    return (
        <div className="flex flex-grow flex-wrap justify-around p-4">
            <div>{title}</div>
            {children}
        </div>
    );
}

export default Playlist;