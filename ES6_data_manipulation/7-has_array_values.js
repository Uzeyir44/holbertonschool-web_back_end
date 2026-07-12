export default function hasValuesFromArray(sett, arr) {
    return arr.every(number => sett.has(number));
}