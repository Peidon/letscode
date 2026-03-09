function detectField(field) {

    const text = (
        (field.name || "") +
        (field.id || "") +
        (field.placeholder || "")
    ).toLowerCase();

    if (text.includes("job")) return "name";
    if (text.includes("phone") || text.includes("mobile")) return "phone";
    if (text.includes("email")) return "email";
    if (text.includes("address")) return "address";

    return null;
}