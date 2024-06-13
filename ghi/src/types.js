export {}

/**
 * @typedef {Object} AuthContextType
 * @property {Error} [error]
 * @property {(error:Error)=>void} setError
 * @property {UserDataResponse} [user]
 * @property {(user?:UserDataResponse)=>void} setUser
 * @property {boolean} isLoading
 * @property {(state:boolean)=>void} setIsLoading
 * @property {boolean} isLoggedIn
 */
/**
 * @typedef {Object} SignInRequest
 * @property {string} username
 * @property {string} password
 */
/**
 * @typedef {Object} SignUpRequest
 * @property {string} username
 * @property {string} password
 * @property {string} first_name
 * @property {string} last_name
 * @property {string} email
 */
/**
 * @typedef {Object} UserDataResponse
 * @property {number} user_id
 * @property {string} username
 * @property {string} email
 */
