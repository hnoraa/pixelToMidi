import NoteDuration from "../models/noteDuration";

// 4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125
export const NoteDurations: NoteDuration[] = [
    {
        fraction: 4.0,
        friendly: "Longa",
        short: "L"
    },
    {
        fraction: 2.0,
        friendly: "Double Whole Note",
        short: "D"
    },
    {
        fraction: 1.0,
        friendly: "Whole Note",
        short: "W"
    },
    {
        fraction: 0.5,
        friendly: "Half Note",
        short: "1/2"
    },
    {
        fraction: 0.25,
        friendly: "Quarter Note",
        short: "1/4"
    },
    {
        fraction: 0.125,
        friendly: "Eighth Note",
        short: "1/8"
    },
    {
        fraction: 0.0625,
        friendly: "Sixteenth Note",
        short: "1/16"
    },
    {
        fraction: 0.03125,
        friendly: "Thirty-Second Note",
        short: "1/32"
    },
    {
        fraction: 0.015625,
        friendly: "Sixty-Fourth Note",
        short: "1/64"
    },
    {
        fraction: 0.0078125,
        friendly: "One Hundred Twenty-Eighth Note",
        short: "1/128"
    }
];