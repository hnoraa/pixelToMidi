import './pixelGrid.css';
import { useState, useEffect, useRef } from 'react';

interface Props {
    height: number;
    width: number;
    currentNote?: string;
    currentOctave?: number;
    currentMidiNumber?: number;
    currentNoteDuration?: number;
    keyPressId?: number;
    onCellSelect?: (cellIndex: number) => void;
};

export default function PixelGrid({ height, width, currentNote, currentOctave, currentMidiNumber, currentNoteDuration, keyPressId, onCellSelect }: Props) {
    const [clickedCell, setClickedCell] = useState<number>(0);
    const [cellNotes, setCellNotes] = useState<Map<number, { note: string; octave: number; midiNumber: number; duration: number }>>(new Map());
    const previousKeyPressIdRef = useRef<number>(-1);

    const handleClick = (i: number) => {
        setClickedCell(i);
        if (onCellSelect) {
            onCellSelect(i);
        }
    };

    // Update cell note when keyPressId changes (new key is clicked)
    useEffect(() => {
        if (currentNote && currentOctave !== undefined && currentMidiNumber !== undefined && currentNoteDuration !== undefined && keyPressId !== undefined && keyPressId !== previousKeyPressIdRef.current) {
            previousKeyPressIdRef.current = keyPressId;
            setCellNotes(prevCellNotes => {
                const newCellNotes = new Map(prevCellNotes);
                newCellNotes.set(clickedCell, { note: currentNote, octave: currentOctave, midiNumber: currentMidiNumber, duration: currentNoteDuration });
                return newCellNotes;
            });
        }
    }, [keyPressId, clickedCell, currentNote, currentOctave, currentMidiNumber, currentNoteDuration]);

    let gridItems: JSX.Element[] = [];
    for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
            const cellIndex = i * width + j;
            const cellNote = cellNotes.get(cellIndex);
            const isSelected = clickedCell === cellIndex;
            
            // Calculate background color: R=midiNumber, G=duration scaled to 0-255, B=100
            let backgroundColor = 'white';
            if (cellNote && !isSelected) {
                const r = Math.min(cellNote.midiNumber, 255);
                const g = Math.round((cellNote.duration / 9) * 255); // Scale 0-9 to 0-255
                const b = 100;
                backgroundColor = `rgb(${r}, ${g}, ${b})`;
            }
            
            gridItems.push(
                <div
                    key={cellIndex}
                    className={`grid-cell ${isSelected ? 'clicked' : ''}`}
                    style={{ backgroundColor }}
                    onClick={() => {
                        handleClick(cellIndex);
                    }}
                >
                    {cellNote && (
                        <div className="cell-content">
                            <div>{cellNote.note}</div>
                            <div>{cellNote.midiNumber}</div>
                        </div>
                    )}
                </div>
            );
        }
    }

    return (
        <div 
            id="gridArea"
            style={{
                gridTemplateColumns: `repeat(${width}, 1fr)`,
                gridTemplateRows: `repeat(${height}, 1fr)`,
                gridAutoRows: undefined,
            } as React.CSSProperties}
        >
            {gridItems}
        </div>
    )
}
