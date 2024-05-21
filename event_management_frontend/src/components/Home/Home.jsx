import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container">
      <h>Welcome to Eventify</h>
      <p>
        <Link to="/events">View Events</Link>
      </p>
      <p>
        <Link to={"login"}>Login</Link>
      </p>
    </div>
  );
}

export default Home;
