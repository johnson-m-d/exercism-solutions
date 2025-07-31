/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Returns whether the lasagna is done based on a timer
 *
 * @param {number} remainingTime
 * @returns {string} cooking status or timer not set
 */
export function cookingStatus(remainingTime) {
  if (remainingTime === 0) {
    return 'Lasagna is done.';
  }
  if (remainingTime > 0) {
    return 'Not done, please wait.';
  }
  return 'You forgot to set the timer.';
}

/**
 * Works out time to prepare lasagna given the layers
 *   and the average time to prepare them.
 *
 * @param {array} layers
 * @param {number} avgTime, defaults to 2
 * @returns {number} total time per layers
 *   and average time per layer
 */
export function preparationTime(layers, avgTime = 2) {
  return layers.length * avgTime;
}

/**
 * Determines required volume of sauce and noodles
 *
 * @param {array} layers
 * @returns {object} with noodle and sauce volume
 */
export function quantities(layers) {
  let noodles = 0;
  let sauce = 0;
  for (const layer of layers) {
    switch (layer) {
      case 'noodles':
        noodles += 50;
        break;
      case 'sauce':
        sauce += 0.2;
        break;
    }
  }
  return {noodles, sauce};
}

/**
 * Add your friend's secret ingredient to your lasagna recipe
 *
 * @param {array} friendsList
 * @param {array} myList
 * @returns {undefined}
 */
export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length-1]);
}

/**
 * Scales recipe quantities for a given number of portions
 *
 * @param {object} recipe
 * @param {number} targetPortions
 * @returns {object} a new recipe with scaled quantities
 */
export function scaleRecipe(recipe, targetPortions) {
  const newRecipe = {};
  for (const item in recipe) {
    newRecipe[item] = recipe[item] / 2 * targetPortions;
  }
  return newRecipe;
}