import { Octaves } from '../../data/octaves';
import { NoteDurations } from '../../data/noteDurations';
import NoteDuration from '../../models/noteDuration';
import Song from '../../models/song';

interface Props {
    currentOctave: number;
    onOctaveChange: (octave: number) => void;
    currentNoteDuration: number;
    onNoteDurationChange: (noteDuration: number) => void;
    currentVelocity: number;
    onVelocityChange: (velocity: number) => void;
    onGridSizeChange: (width: number, height: number) => void;
    onGridDataChange?: (gridData: Map<number, { note: string; octave: number; midiNumber: number; duration: number; velocity?: number }>) => void;
    song?: Song;
    gridData?: Map<number, { note: string; octave: number; midiNumber: number; duration: number; velocity?: number }>;
    selectedNote?: string;
    selectedMidiNumber?: number;
    selectedOctave?: number;
    gridWidth?: number;
    gridHeight?: number;
}

export default function ConfigComponent({
    currentOctave,
    onOctaveChange,
    currentNoteDuration,
    onNoteDurationChange,
    currentVelocity,
    onVelocityChange,
    onGridSizeChange,
    song,
    gridData,
    onGridDataChange,
    selectedNote,
    selectedMidiNumber,
    selectedOctave,
    gridWidth = 16,
    gridHeight = 16
}: Props) {
    const currentOctaveObj = Octaves.find(o => o.octaveNumber === currentOctave);
    const handleOctaveChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const selectedOctave = parseInt(e.target.value);
        onOctaveChange(selectedOctave);
    };

    const handleNoteDurationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const selectedNoteDuration = parseInt(e.target.value);
        onNoteDurationChange(selectedNoteDuration);
    };

    const handleVelocityChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        let velocity = parseInt(e.target.value);
        if (isNaN(velocity)) velocity = 127;
        if (velocity < 0) velocity = 0;
        if (velocity > 127) velocity = 127;
        onVelocityChange(velocity);
    };

    const handleGridSizeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const size = e.target.value;
        switch (size) {
            case '16':
                onGridSizeChange(16, 16);
                break;
            case '32':
                onGridSizeChange(32, 32);
                break;
            case '64':
                onGridSizeChange(64, 64);
                break;
            default:
                onGridSizeChange(16, 16);
        }
    };

    const handleSave = () => {
        if (!song || !gridData) {
            alert('No data to save');
            return;
        }

        // Check if all cells are filled
        const totalCells = gridWidth * gridHeight;
        if (gridData.size !== totalCells) {
            alert(`Pixel grid not complete. Filled: ${gridData.size}/${totalCells}`);
            return;
        }

        // Save JSON
        const jsonString = JSON.stringify(song, null, 2);
        const jsonBlob = new Blob([jsonString], { type: 'application/json' });
        const jsonUrl = URL.createObjectURL(jsonBlob);
        const jsonLink = document.createElement('a');
        jsonLink.href = jsonUrl;
        jsonLink.download = `${song.song}.json`;
        jsonLink.click();
        URL.revokeObjectURL(jsonUrl);

        // Save pixel grid as bitmap
        const cellSize = 30;
        const canvas = document.createElement('canvas');
        canvas.width = gridWidth * cellSize;
        canvas.height = gridHeight * cellSize;
        const ctx = canvas.getContext('2d')!;

        for (let i = 0; i < gridHeight; i++) {
            for (let j = 0; j < gridWidth; j++) {
                const cellIndex = i * gridWidth + j;
                const cellNote = gridData.get(cellIndex);

                let color = 'white';
                if (cellNote) {
                    const r = Math.min(cellNote.midiNumber, 255);
                    const g = Math.round((cellNote.duration / 9) * 255);
                    const b = 100;
                    color = `rgb(${r}, ${g}, ${b})`;
                }

                ctx.fillStyle = color;
                ctx.fillRect(j * cellSize, i * cellSize, cellSize, cellSize);
            }
        }

        canvas.toBlob((blob) => {
            if (blob) {
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.download = 'pixel-grid.png';
                link.click();
                URL.revokeObjectURL(url);
            }
        });
    };

    const handleFill = () => {
        if (!onGridDataChange) {
            alert('Fill not available');
            return;
        }

        if (!selectedNote || selectedMidiNumber === undefined) {
            alert('No note selected to fill with');
            return;
        }

        const newMap = new Map<number, { note: string; octave: number; midiNumber: number; duration: number; velocity?: number }>();
        const total = gridWidth * gridHeight;
        for (let i = 0; i < total; i++) {
            newMap.set(i, { note: selectedNote, octave: selectedOctave ?? currentOctave, midiNumber: selectedMidiNumber, duration: currentNoteDuration, velocity: currentVelocity });
        }

        onGridDataChange(newMap);
    };

    const handleClear = () => {
        if (!onGridDataChange) {
            alert('Clear not available');
            return;
        }

        const confirmed = window.confirm('Clear entire grid? This will remove all notes. Continue?');
        if (!confirmed) return;

        onGridDataChange(new Map());
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', alignItems: 'stretch' }}>
            <div style={{ display: 'flex', flexDirection: 'column' }}>
                <label htmlFor="octave-select">Select Octave:</label>
                <select id="octave-select" value={currentOctave} onChange={handleOctaveChange}>
                    {Octaves.map((octave) => (
                        <option key={octave.octaveNumber} value={octave.octaveNumber}>
                            Octave {octave.octaveNumber}
                        </option>
                    ))}
                </select>
                <span><small>Range: {currentOctaveObj?.frequencyRange?.min}Hz - {currentOctaveObj?.frequencyRange?.max}Hz</small></span>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column' }}>
                <label htmlFor="gridSizeSelect">Grid Size:</label>
                <select id="gridSizeSelect" onChange={handleGridSizeChange} defaultValue="16">
                    <option value="16">16 x 16</option>
                    <option value="32">32 x 32</option>
                    <option value="64">64 x 64</option>
                </select>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column' }}>
                <label htmlFor="note-duration-select">Select Note Duration:</label>
                <select id="note-duration-select" value={currentNoteDuration} onChange={handleNoteDurationChange}>
                    {NoteDurations.map((noteDuration: NoteDuration, index: number) => (
                        <option key={index} value={index}>
                            {noteDuration.friendly}
                        </option>
                    ))}
                </select>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column' }}>
                <label htmlFor="velocity-input">Note Velocity:</label>
                <input 
                    id="velocity-input" 
                    type="number" 
                    min="0" 
                    max="127" 
                    value={currentVelocity} 
                    onChange={handleVelocityChange}
                    style={{ padding: '4px' }}
                />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                <div style={{ display: 'flex', gap: '8px' }}>
                    <button onClick={handleFill}>
                        Fill
                    </button>
                    <button onClick={handleClear}>
                        Clear
                    </button>
                </div>
                <div>
                    <button onClick={handleSave} disabled={!gridData || gridData.size !== (gridWidth * gridHeight)}>
                        Save ({gridData?.size || 0}/{gridWidth * gridHeight})
                    </button>
                </div>
            </div>
        </div>
    );
}
