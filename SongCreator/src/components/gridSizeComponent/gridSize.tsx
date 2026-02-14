interface Props {
    onGridSizeChange: (width: number, height: number) => void;
}

export default function GridSize({ onGridSizeChange }: Props) {
    const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        const size = event.target.value;
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

    return (
        <div>
            <label htmlFor="gridSizeSelect">Grid Size: </label>
            <select id="gridSizeSelect" onChange={handleChange} defaultValue="16">
                <option value="16">16 x 16</option>
                <option value="32">32 x 32</option>
                <option value="64">64 x 64</option>
            </select>
        </div>
    );
}
