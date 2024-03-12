function WelcomeText(props) {
    const username = props.username || 'Music Lover'; // Handle default value
    return (
        <h2 className='flex flex-grow flex-wrap justify-around p-4'>Welcome back, {username}!</h2>
    );
}

export default WelcomeText;