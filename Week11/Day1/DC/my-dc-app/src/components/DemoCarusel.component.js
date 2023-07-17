import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel'
import './DemoCarusel.component.css'
    

const DemoCarousel = () => {
        return (
            <Carousel
                autoPlay = {true}
                interval={500}
                infiniteLoop={true}>
                <div className="box">
                    <img src="p1.jpg" />
                    <p className="legend">City 1</p>
                </div>
                <div className="box">
                    <img src="p2.webp" />
                    <p className="legend">City 2</p>
                </div>
                <div className="box">
                    <img src="p3.webp" />
                    <p className="legend">City 3</p>
                </div>
                <div className="box">
                    <img src="p4.webp" />
                    <p className="legend">City 4</p>
                </div>
                
            </Carousel>
        );
    
};


export default DemoCarousel;