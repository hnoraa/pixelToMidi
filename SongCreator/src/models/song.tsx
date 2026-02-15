import Track from "./track";

export default interface Song {
    song: string;
    tempo: number;
    outputFilename: string;
    size: number;
    tracks: Track[];
}
