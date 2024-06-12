function HomePage() {
    return (
        <>
            <header>
                <div className="container">
                    <div className="row align-items-center pt-2">
                        <div className="col-xl-3 col-lg-8 col-7 d-flex">
                            <div className="dropdown selectBox">
                                <a
                                    className="dropdown-toggle selectValue text-reset"
                                    href="javascript:void(0)"
                                    data-bs-toggle="dropdown"
                                    aria-expanded="false"
                                >
                                    USD $
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
            <div className="input-group">
                <input
                    className="form-control"
                    type="search"
                    placeholder="Search for products"
                    aria-label="Recipient's username"
                    aria-describedby="button-addon2"
                />
                <button
                    className="btn btn-primary"
                    type="button"
                    id="button-addon2"
                >
                    Search
                </button>
                <a
                    href="#"
                    className="text-reset"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                >
                    <div className="lh-1">
                        <div className="position-relative d-inline-block mb-2">
                            <i className="bi bi-bell fs-4"></i>
                            <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                                1
                                <span className="visually-hidden">
                                    unread messages
                                </span>
                            </span>
                        </div>
                        <p className="mb-0 d-none d-xl-block small">
                            Notification
                        </p>
                    </div>
                </a>
            </div>
        </>
    )
}

export default HomePage
