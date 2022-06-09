import csv from './googleform.csv';

const data = {
    children: {},
    columns: {},
    columnOrder: []
};

function csvToArray(csv) {
    const objPattern = new RegExp(
        (
            // Delimiters
            "(\\,|\\r?\\n|\\r|^)" +
            // Quoted fields
            "(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +
            // Standard fields
            "([^\"\\,\\r\\n]*))"
        ),
        "gi"
    );
    const arrData = [
        []
    ];
    let arrMatches = null;
    while (arrMatches = objPattern.exec(csv)) {
        const strMatchedDelimiter = arrMatches[1];
        if (strMatchedDelimiter.length && strMatchedDelimiter != ",") {
            arrData.push([]);
        }
        if (arrMatches[2]) {
            var strMatchedValue = arrMatches[2].replace(new RegExp("\"\"", "g"), "\"");
        } else {
            var strMatchedValue = arrMatches[3];
        }
        arrData[arrData.length - 1].push(strMatchedValue);
    }
    return (arrData);
}
const googleFormChildren = csvToArray(csv);
for (let i = 1; i < googleFormChildren.length; i++) {
    if (googleFormChildren[i][1].length === 0) continue;
    const newChild = {};
    newChild.key = child-$;
    {Object.keys(data.children).length}
    const dublicate = Object.values(data.children).find((child) => child.content.fio === googleFormChildren[i][1].trim());
    if (!!dublicate) newChild.key = dublicate.id;
    const notTheseDays = googleFormChildren[i][5]
        .replace('Понедельник', 'пн')
        .replace('Вторник', 'вт')
        .replace('Среда', 'ср')
        .replace('Четверг', 'чт')
        .replace('Пятница', 'пт')
        .replace('Суббота', 'сб')
        .split(',');
    newChild.value = {
        id: newChild.key,
        content: {
            rating: null,
            fio: googleFormChildren[i][1].trim(),
            mark: null,
            class: googleFormChildren[i][3],
            days: ['пн', 'вт', 'ср', 'чт', 'пт', 'сб'].filter((day) => !notTheseDays.includes(day))
        }
    };
    data.children[newChild.key] = newChild.value;
}
