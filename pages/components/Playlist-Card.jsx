const Card = ({ content }) => (
    <div className="w-full sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/4 p-4">
        <div className="border p-4">{content}</div>
    </div>
);
export default Card;