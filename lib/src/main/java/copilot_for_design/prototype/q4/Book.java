package copilot_for_design.prototype.q4;

import java.util.List;

/**
 * Represents a book in the bookstore having a composition relationship
 * with a titlepage, dedication, ordered list of chapters, and afterword.
 */
public class Book {
    private final TitlePage titlePage;
    private final Dedication dedication;
    private final List<Chapter> chapters;
    private final Afterword afterword;

    public Book(
        TitlePage titlePage,
        Dedication dedication,
        List<Chapter> chapters,
        Afterword afterword
    ) {
        this.titlePage = titlePage;
        this.dedication = dedication;
        this.chapters = chapters;
        this.afterword = afterword;
    }

    public TitlePage getTitlePage() {
        return titlePage;
    }

    public Dedication getDedication() {
        return dedication;
    }

    public List<Chapter> getChapters() {
        return chapters;
    }

    public Afterword getAfterword() {
        return afterword;
    }
}