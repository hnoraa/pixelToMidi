import Octave from "../models/octave"

export const Octaves: Octave[] = [
    {
        octaveNumber: -1,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i),
        frequencyRange: { min: 8.18, max: 15.43 }
    },
    {
        octaveNumber: 0,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 12),
        frequencyRange: { min: 16.35, max: 30.87 }
    },
    {
        octaveNumber: 1,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 24),
        frequencyRange: { min: 32.70, max: 61.74 }
    },
    {
        octaveNumber: 2,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 36),
        frequencyRange: { min: 65.41, max: 123.47 }
    },
    {
        octaveNumber: 3,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 48),
        frequencyRange: { min: 130.81, max: 246.94 }
    },
    {
        octaveNumber: 4,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 60),
        frequencyRange: { min: 261.63, max: 493.88 }
    },
    {
        octaveNumber: 5,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 72),
        frequencyRange: { min: 523.25, max: 987.77 }
    },
    {
        octaveNumber: 6,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 84),
        frequencyRange: { min: 1046.50, max: 1975.53 }
    },
    {
        octaveNumber: 7,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 96),
        frequencyRange: { min: 2093.00, max: 3951.07 }
    },
    {
        octaveNumber: 8,
        midiNoteNumbers: Array.from({ length: 12 }, (_, i) => i + 108),
        frequencyRange: { min: 4186.01, max: 7902.13 }
    }
];