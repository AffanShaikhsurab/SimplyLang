/* eslint-disable react/prop-types */
const SectionHeader = ({ eyebrow, title, description, centered = false, light = false }) => (
  <div className={`mb-10 md:mb-12 ${centered ? "mx-auto max-w-2xl text-center" : "max-w-3xl"}`}>
    <p className={light ? "text-sm font-semibold uppercase tracking-wider text-brand-200" : "section-eyebrow"}>
      {eyebrow}
    </p>
    <h2 className={`mt-3 text-3xl font-bold md:text-4xl ${light ? "text-white" : "section-title !mt-3"}`}>
      {title}
    </h2>
    {description ? (
      <p
        className={`mt-4 max-w-3xl text-lg leading-relaxed ${
          light ? "text-brand-100" : "section-desc"
        } ${centered ? "mx-auto" : ""}`}
      >
        {description}
      </p>
    ) : null}
  </div>
);

export default SectionHeader;
