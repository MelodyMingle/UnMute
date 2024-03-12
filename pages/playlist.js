import React from "react";
import Head from "next/head";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Card from "./components/Playlist-Card";

export default function Playlist() {
  return (
    <div className="flex flex-col min-h-screen">
      <Head>
        <title>UnMute</title>
      </Head>
      <Navbar />
      <main className="flex flex-grow">
        <div className="flex flex-col flex-grow items-center justify-center">
            <Card content="Playlist 1" />
            <textarea className='border border-pink-800' placeholder="Leave a comment">

            </textarea>
        </div>
        <div className="w-1/4 p-4 bg-gray-200">Right side column</div>
      </main>
      <Footer />
    </div>
  );
}