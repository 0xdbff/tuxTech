// MiddleContentContext.tsx
import { createContext, MutableRefObject } from "react";

export type MiddleContentContextType = {
  middleContentRef: MutableRefObject<HTMLDivElement | null>;
};

export const MiddleContentContext = createContext<Partial<MiddleContentContextType>>({});

