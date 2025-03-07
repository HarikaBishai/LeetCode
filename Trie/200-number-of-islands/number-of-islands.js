/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const ROWS = grid.length
    const COLS = grid[0].length
    let visited = new Set()
    let islands = 0

    const dfs = (r, c) => {
        visited.add(`${r},${c}`)
        let dir = [[-1,0],[1,0],[0,-1],[0,1]]
        for( let [dx, dy] of dir) {
            const new_r = r + dx
            const new_c = c + dy

            if ( new_r >= 0 && new_r <= ROWS-1 && new_c >= 0 && new_c <= COLS-1 && !visited.has(`${new_r},${new_c}`) && grid[new_r][new_c] === '1') {
                dfs(new_r, new_c)
            }
        }
            
    
    }
    for(let i=0; i<ROWS; i++ ) {
        for (let j=0;j<COLS; j++) {
            if (!visited.has(`${i},${j}`) && grid[i][j] === "1") {
                dfs(i,j)
                islands+=1
            }
        }
    }
    return islands


};