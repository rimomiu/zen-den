import {
    AppBar,
    Box,
    Toolbar,
    Stack,
    Typography,
    Button,
    IconButton,
} from '@mui/material'
import logo from './assets/logo.png'

function Nav() {
    return (
        <AppBar>
            <Toolbar>
                <Box
                    component="img"
                    sx={{
                        height: 64,
                    }}
                    src={logo}
                />
                <IconButton
                    size="large"
                    edge="start"
                    color="inherit"
                    aria-label="logo"
                ></IconButton>
                <Typography
                    variant="h6"
                    component="div"
                    sx={{ flexGrow: 1 }}
                ></Typography>
                <Stack direction="row" spacing={2}>
                    <Button color="inherit">Blogs</Button>
                    <Button color="inherit">Login</Button>
                </Stack>
            </Toolbar>
        </AppBar>
    )
}

export default Nav
