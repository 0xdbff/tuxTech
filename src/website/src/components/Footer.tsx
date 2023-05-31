import React from "react";
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from "react-icons/fa";
import "../assets/css/footer.css";
import { getStaticPath } from "../utils/path";

const Footer: React.FC = () => {
    const logoUrl = getStaticPath("logo512.png");

    return (
        <footer className="footer">
            <div className="footer-content">
                <img src={logoUrl} alt=" " className="logoFooter" />
                <p style={{ lineHeight: "1.5" }}>
                    A TuxTech é a sua loja de tecnologia.
                    <br />
                    Oferecemos uma grande variedade de produtos de várias categorias como
                    <br />
                    computadores, smartphones, acessórios e muito mais.
                </p>

                <div className="social-links">
                    <a
                        href="https://www.facebook.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaFacebook />
                    </a>
                    <a
                        href="https://www.twitter.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaTwitter />
                    </a>
                    <a
                        href="https://www.instagram.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaInstagram />
                    </a>
                    <a
                        href="https://www.linkedin.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaLinkedin />
                    </a>
                </div>
            </div>
            <div className="footer-line">
                <h2> Academic work </h2>
                <a className="link" href="https://github.com/Db-Dev2002/tuxTech">
                    https://github.com/Db-Dev2002/tuxTech
                </a>
            </div>
        </footer>
    );
};

export default Footer;
