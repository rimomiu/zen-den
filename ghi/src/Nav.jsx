import {
    AppBar,
    Box,
    Toolbar,
    Stack,
    Typography,
    Button,
    IconButton,
} from '@mui/material'
import { Link } from 'react-router-dom'
import logo from './assets/logo.png'
import useAuthService from './hooks/useAuthService.js'

function Nav() {
    const { user, isLoggedIn } = useAuthService()
    return (
        <AppBar position="static">
            <Toolbar>
                <Box
                    component="img"
                    sx={{
                        height: 64,
                    }}
                    src={logo}
                    alt="Logo"
                />
                <IconButton
                    size="large"
                    edge="start"
                    color="inherit"
                    aria-label="logo"
                ></IconButton>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    MyApp
                </Typography>
                <Stack direction="row" spacing={2}>
                    <Button component={Link} to="/" color="inherit">
                        Home
                    </Button>
                    <Button component={Link} to="/blogs" color="inherit">
                        Blogs
                    </Button>
                    {isLoggedIn ? (
                        <Button
                            component={Link}
                            to={`/user/id/${user.user_id}`}
                            color="inherit"
                        >
                            Profile
                        </Button>
                    ) : (
                        <>
                            <Button
                                component={Link}
                                to="/signin"
                                color="inherit"
                            >
                                Sign In
                            </Button>
                            <Button
                                component={Link}
                                to="/signup"
                                color="inherit"
                            >
                                Sign Up
                            </Button>
                        </>
                    )}
                </Stack>
            </Toolbar>
        </AppBar>
    )
}

export default Nav
