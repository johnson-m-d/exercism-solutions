
/**
 * Overrides the default comparison method of sort for Arrays.
 *
 * @param {object[]} data
 * @param {string} pointsKey
 * @param (string) nameKey
 * @returns {object[]} sorted with descending points
 *                     or ascending names for ties
 */
function sort(data, pointsKey, nameKey) {
  return data.sort((a, b) => {
    const pointsComparison = b[pointsKey] - a[pointsKey];
    if (pointsComparison != 0) {
      return pointsComparison;
    }
    return a[nameKey].localeCompare(b[nameKey]);
  })
}
/**
 * Prepares tally attributes for a scoreboard
 *   based on points for win, loss, and draw.
 *
 * @param {string} outcome
 * @returns {object} A dictionary of score attributes
 */
function processOutcome(outcome) {
  let processedOutcome = {};
  if (outcome === 'win') {
    processedOutcome['W'] = 1;
    processedOutcome['D'] = 0;
    processedOutcome['L'] = 0;
    processedOutcome['P'] = 3;
  } else if (outcome == 'loss') {
    processedOutcome['W'] = 0;
    processedOutcome['D'] = 0;
    processedOutcome['L'] = 1;
    processedOutcome['P'] = 0;
  } else {
    processedOutcome['W'] = 0;
    processedOutcome['D'] = 1;
    processedOutcome['L'] = 0;
    processedOutcome['P'] = 1;
  }
  return processedOutcome;
}
/**
 * Assembles a scoreboard string
 *
 * @param {string} header
 * @param {object[]} scoreBoardOrder
 * @param {object} scoreBoard
 * @returns {string} The complete scoreboard string
 */
function buildScoreBoard(header, scoreBoardOrder, scoreBoard) {
  let result = header.concat('\n');
  let i = 0;
  for (const team of scoreBoardOrder) {
    let name = team.name;
    result += name + ' |  '.padStart(34-name.length) + scoreBoard[name].MP + ' |  ' + scoreBoard[name].W + ' |  ' + scoreBoard[name].D + 
              ' |  ' + scoreBoard[name].L + ' | ' + ''.padEnd(2-scoreBoard[name]['P'].toString().length) + scoreBoard[name].P;
    if (i < scoreBoardOrder.length-1) {
      result = result.concat('\n');
    }
    i++;
  }
  return result;
}

/**
 * Creates a scoreboard with a string of teams and the game outcome for the first team on every line
 * 
 * @param {string} input
 * @return {string} A complete scoreboard.
 */
export const tournamentTally = (input) => {
  const header = "Team ".padEnd(30) + " | MP |  W |  D |  L |  P";
  const gameOutcomes = {win: 'loss', loss: 'win', draw: 'draw'}; // Outcome mapping for the second team per match
  let outcomeA;
  let outcomeB;
  let match;
  let matches;
  const scoreBoard = {};
  let scoreBoardOrder;
  const teams = [];
  if (input === "") {
    return header;
  }
  if (! input.includes('\n')) {
    match = input.split(';');
    outcomeA = match[2];
    outcomeB = processOutcome(gameOutcomes[outcomeA]);
    outcomeA = processOutcome(outcomeA);
    scoreBoard[match[0]] = {MP: 1, W: outcomeA['W'], D: outcomeA['D'], L: outcomeA['L'], P: outcomeA['P']};
    scoreBoard[match[1]] = {MP: 1, W: outcomeB['W'], D: outcomeB['D'], L: outcomeB['L'], P: outcomeB['P']};
    for (const team in scoreBoard) {
      teams.push({name: team, points: scoreBoard[team].P});
    }
    scoreBoardOrder = sort(teams, 'points', 'name');
    return buildScoreBoard(header, scoreBoardOrder, scoreBoard);
  } else {
    matches = input.split('\n');
    for (const toSemiSplit of matches) {
      match = toSemiSplit.split(';');
      outcomeA = match[2];
      outcomeB = processOutcome(gameOutcomes[outcomeA]);
      outcomeA = processOutcome(outcomeA);
      if (! scoreBoard.hasOwnProperty(match[0])) {
        scoreBoard[match[0]] = {MP: 1, W: outcomeA['W'], D: outcomeA['D'], L: outcomeA['L'], P: outcomeA['P']};
      } else {
        scoreBoard[match[0]]['MP']++;
        scoreBoard[match[0]]['W'] += outcomeA['W'];
        scoreBoard[match[0]]['D'] += outcomeA['D'];
        scoreBoard[match[0]]['L'] += outcomeA['L'];
        scoreBoard[match[0]]['P'] += outcomeA['P'];
      }
      if (! scoreBoard.hasOwnProperty(match[1])) {
        scoreBoard[match[1]] = {MP: 1, W: outcomeB['W'], D: outcomeB['D'], L: outcomeB['L'], P: outcomeB['P']};
      } else {
        scoreBoard[match[1]]['MP']++;
        scoreBoard[match[1]]['W'] += outcomeB['W'];
        scoreBoard[match[1]]['D'] += outcomeB['D'];
        scoreBoard[match[1]]['L'] += outcomeB['L'];
        scoreBoard[match[1]]['P'] += outcomeB['P'];
      }
    }
    for (const team in scoreBoard) {
      teams.push({name: team, points: scoreBoard[team].P});
    }
    scoreBoardOrder = sort(teams, 'points', 'name');
    return buildScoreBoard(header, scoreBoardOrder, scoreBoard);
  }
}