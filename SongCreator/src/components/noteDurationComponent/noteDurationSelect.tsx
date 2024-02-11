import { NoteDurations } from '../../data/noteDurations';
import NoteDuration from '../../models/noteDuration';

interface Props {
  currentNoteDuration: number;
  onNoteDurationChange: any;
}
export default function NoteDurationSelect({ currentNoteDuration, onNoteDurationChange }: Props) {
  const handleNoteDurationChange = (e: any) => {
    const selectedNoteDuration = parseInt(e.target.value);
    onNoteDurationChange(selectedNoteDuration);
  };

  return (
    <div>
      <label htmlFor="note-duration-select">Select Note Duration:</label>
      <select id="note-duration-select" value={currentNoteDuration} onChange={handleNoteDurationChange}>
        {NoteDurations.map((noteDuration: NoteDuration, index: number) => (
          <option key={index} value={index}>
            {noteDuration.friendly}
          </option>
        ))}
      </select>
    </div>
  )
}
