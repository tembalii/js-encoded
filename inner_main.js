<SpecHeading>{change.heading}</SpecHeading>
<Divider />
<div className="flex h-full w-full flex-col items-center justify-center gap-3 pt-3 text-base">
  {submission === "pending" && (
    <>
      <span
        dangerouslySetInnerHTML={{ __html: change.oldLabel }}
        className="text-primary"
      />
      <ChevronDoubleDownIcon className="h-5 w-5 shrink-0 text-primary" />
      <span
        dangerouslySetInnerHTML={{ __html: change.newLabel }}
        className="text-xl font-bool"
      />
    </>
  )}
</div>
