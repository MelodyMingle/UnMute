import React from 'react';
import Playlist from './components/Playlist-holder';
import Head from "next/head";
import Navbar from './components/Navbar';
import Card from './components/Playlist-Card';
import Footer from './components/Footer';
import WelcomeText from './components/Welcome-Message';

export default function Home() {
    return (
        <div className="flex flex-col min-h-screen">
            <Head>
                <title>UnMute</title>
            </Head>
            <Navbar />
            <main className="flex flex-grow">
                <div className="flex flex-col flex-grow">
                    <WelcomeText username="Andrea" /> {/* TODO pass username prop  */}
                    <Playlist title="My playlists">
                        <Card content="Playlist 1" />
                        <Card content="Playlist 2" />
                        <Card content="Playlist 3" />
                    </Playlist>
                    <Playlist title="Top playlists">
                        <Card content="Playlist 1" />
                        <Card content="Playlist 2" />
                        <Card content="Playlist 3" />
                    </Playlist>
                    <Playlist title="Friend playlists">
                        <Card content="Playlist 1" />
                        <Card content="Playlist 2" />
                        <Card content="Playlist 3" />
                    </Playlist>
                </div>
                <div className="w-1/4 p-4 bg-gray-200">Right side column</div>
            </main>
            <Footer />
        </div>
    )
}



