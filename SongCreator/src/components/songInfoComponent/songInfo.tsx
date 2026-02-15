import Song from '../../models/song';

interface Props {
    song?: Song;
    gridHeight?: number;
    gridWidth?: number;
}

export default function SongInfo({ song, gridHeight, gridWidth }: Props) {
    if (!song) {
        return (
            <div id="songInfo">
                <p>No song data</p>
                {gridHeight && gridWidth && (
                    <p><strong>Grid Size:</strong> {gridWidth}x{gridHeight}</p>
                )}
            </div>
        );
    }

    return (
        <div id="songInfo">
            <div>
                <p><strong>Song:</strong> {song.song}</p>
                <p><strong>Tempo:</strong> {song.tempo}</p>
                {gridHeight && gridWidth && (
                    <p><strong>Grid Size:</strong> {gridWidth}x{gridHeight}</p>
                )}
                <p><strong>Output:</strong> {song.outputFilename}</p>
                <div>
                    <strong>Tracks:</strong>
                    <ul>
                        {song.tracks.map((track, index) => (
                            <li key={index}>
                                {track.name} (Program: {track.program})
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}
