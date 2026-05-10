# Trace: apache__rocketmq-7346

## Step 1: Localization
Identified relevant file(s): tieredstore/src/main/java/org/apache/rocketmq/tieredstore/file/TieredFlatFile.java

## Step 2: Fix
Applied the following patch:

```diff
diff --git a/tieredstore/src/main/java/org/apache/rocketmq/tieredstore/file/TieredFlatFile.java b/tieredstore/src/main/java/org/apache/rocketmq/tieredstore/file/TieredFlatFile.java
index 426c4e09d..d973179ee 100644
--- a/tieredstore/src/main/java/org/apache/rocketmq/tieredstore/file/TieredFlatFile.java
+++ b/tieredstore/src/main/java/org/apache/rocketmq/tieredstore/file/TieredFlatFile.java
@@ -365,7 +365,10 @@ public class TieredFlatFile {
             if (!segmentList.isEmpty()) {
                 return boundaryType == BoundaryType.UPPER ? segmentList.get(0) : segmentList.get(segmentList.size() - 1);
             }
-            return fileSegmentList.isEmpty() ? null : fileSegmentList.get(fileSegmentList.size() - 1);
+            if (fileSegmentList.isEmpty()) {
+                return null;
+            }
+            return boundaryType == BoundaryType.UPPER ? fileSegmentList.get(fileSegmentList.size() - 1) : fileSegmentList.get(0);
         } finally {
             fileSegmentLock.readLock().unlock();
         }

```

## Step 3: Outcome
Resolved: Yes
