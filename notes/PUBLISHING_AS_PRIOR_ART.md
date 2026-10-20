# Making "A POINT of contention" count as a defensive publication (checklist)

Not legal advice. I am not a lawyer, and the rules of the services below change; check each one's current terms before relying on it. A patent attorney is the person to ask about what a publication does and doesn't achieve in your country.

## What a defensive publication needs

The aim is for the idea to be public, dated, and easy to find later, so nobody can fairly patent it. In practice that means:

1. **Public.** Anyone can read it without logging in or paying.
2. **Dated in a way you can't quietly change.** A third party's timestamp beats your own claim.
3. **Stable.** The same text at the same address in five years.
4. **Findable.** Searchable by the words an examiner would use ("STL", "attribute byte count", "face label", "CAD face", "mesh to STEP").
5. **Enabling.** Detailed enough that a competent person could build it. Section 8 of the paper is written for that.

A private artifact link does none of this. It becomes public only when you set it to "anyone with the link" in the artifact's Share menu, and even then it sits on one company's site.

## Steps, in order

1. **Share the artifact** (Share menu, "anyone with the link"). Quick, but not the archive.
2. **GitHub repository.** Publish `hardpoint-stl` from GitHub Desktop (the zip and PUBLISHING.md from the earlier hand-over). Add this paper under `paper/`. The commit dates and tag are visible to everyone.
3. **Zenodo DOI.** Link the GitHub repository to Zenodo, then make a GitHub Release; Zenodo archives that release and issues a DOI, which is a fixed, citable, dated copy. Check Zenodo's current instructions for linking GitHub.
4. **A defensive-publication service.** Technical Disclosure Commons (a service I have not used; check who runs it and its current rules) accepts disclosures for this purpose; others exist. Their submission rules decide whether they take a hobbyist paper.
5. **Internet Archive.** Save the artifact URL and the GitHub page with the Wayback Machine ("Save Page Now") for a third-party snapshot with a date.
6. **dev.to or a blog post** linking to all of the above. Good for people finding it; weak as proof on its own.
7. **Keep a record.** Note the dates, URLs and DOI in the repo's CHANGELOG.

## After publishing

- Do not edit the text silently. Publish a new version (v1.1) and keep the old one.
- Put the DOI into the paper's "How to cite" section in the new version.
- Tell people the licence: text CC BY-SA 4.0; code PolyForm Noncommercial 1.0.0 (source-available, not open source). Note that this licence is about copyright; a defensive publication is about stopping patents. They are separate.

## Limits worth knowing

- Defensive publication only blocks later patents on **what the paper discloses**. Things it left out can still be patented by others.
- It does not stop a patent filed **before** your date. The paper's prior-art search (3 to 10 October 2026) was informal and found nothing, which is not the same as there being nothing.
- Examiners find some archives more easily than others; the more places it is, the better.
