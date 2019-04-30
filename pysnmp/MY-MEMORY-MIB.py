#
# PySNMP MIB module MY-MEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-MEMORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, ModuleIdentity, Counter64, Bits, Counter32, Gauge32, TimeTicks, iso, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter64", "Bits", "Counter32", "Gauge32", "TimeTicks", "iso", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
myMemoryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35))
myMemoryMIB.setRevisions(('2003-10-14 00:00',))
if mibBuilder.loadTexts: myMemoryMIB.setLastUpdated('200310140000Z')
if mibBuilder.loadTexts: myMemoryMIB.setOrganization('D-Link Crop.')
class Percent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

myMemoryPoolMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1))
myMemoryPoolUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1), )
if mibBuilder.loadTexts: myMemoryPoolUtilizationTable.setStatus('current')
myMemoryPoolUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1), ).setIndexNames((0, "MY-MEMORY-MIB", "myMemoryPoolIndex"))
if mibBuilder.loadTexts: myMemoryPoolUtilizationEntry.setStatus('current')
myMemoryPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolIndex.setStatus('current')
myMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolName.setStatus('current')
myMemoryPoolCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolCurrentUtilization.setStatus('current')
myMemoryPoolLowestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolLowestUtilization.setStatus('current')
myMemoryPoolLargestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolLargestUtilization.setStatus('current')
myMemoryPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolSize.setStatus('current')
myMemoryPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolUsed.setStatus('current')
myMemoryPoolFree = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolFree.setStatus('current')
myMemoryPoolWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 9), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMemoryPoolWarning.setStatus('current')
myMemoryPoolCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 10), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMemoryPoolCritical.setStatus('current')
myNodeMemoryPoolTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2), )
if mibBuilder.loadTexts: myNodeMemoryPoolTable.setStatus('current')
myNodeMemoryPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1), ).setIndexNames((0, "MY-MEMORY-MIB", "myNodeMemoryPoolIndex"))
if mibBuilder.loadTexts: myNodeMemoryPoolEntry.setStatus('current')
myNodeMemoryPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolIndex.setStatus('current')
myNodeMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolName.setStatus('current')
myNodeMemoryPoolCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolCurrentUtilization.setStatus('current')
myNodeMemoryPoolLowestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolLowestUtilization.setStatus('current')
myNodeMemoryPoolLargestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolLargestUtilization.setStatus('current')
myNodeMemoryPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolSize.setStatus('current')
myNodeMemoryPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolUsed.setStatus('current')
myNodeMemoryPoolFree = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolFree.setStatus('current')
myNodeMemoryPoolWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 9), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeMemoryPoolWarning.setStatus('current')
myNodeMemoryPoolCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 10), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeMemoryPoolCritical.setStatus('current')
myMemoryMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2))
myMemoryMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 1))
myMemoryMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2))
myMemoryMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 1, 1)).setObjects(("MY-MEMORY-MIB", "myMemoryPoolUtilizationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myMemoryMIBCompliance = myMemoryMIBCompliance.setStatus('current')
myMemoryPoolUtilizationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2, 1)).setObjects(("MY-MEMORY-MIB", "myMemoryPoolIndex"), ("MY-MEMORY-MIB", "myMemoryPoolName"), ("MY-MEMORY-MIB", "myMemoryPoolCurrentUtilization"), ("MY-MEMORY-MIB", "myMemoryPoolLowestUtilization"), ("MY-MEMORY-MIB", "myMemoryPoolLargestUtilization"), ("MY-MEMORY-MIB", "myMemoryPoolSize"), ("MY-MEMORY-MIB", "myMemoryPoolUsed"), ("MY-MEMORY-MIB", "myMemoryPoolFree"), ("MY-MEMORY-MIB", "myMemoryPoolWarning"), ("MY-MEMORY-MIB", "myMemoryPoolCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myMemoryPoolUtilizationMIBGroup = myMemoryPoolUtilizationMIBGroup.setStatus('current')
myNodeMemoryPoolMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2, 2)).setObjects(("MY-MEMORY-MIB", "myNodeMemoryPoolIndex"), ("MY-MEMORY-MIB", "myNodeMemoryPoolName"), ("MY-MEMORY-MIB", "myNodeMemoryPoolCurrentUtilization"), ("MY-MEMORY-MIB", "myNodeMemoryPoolLowestUtilization"), ("MY-MEMORY-MIB", "myNodeMemoryPoolLargestUtilization"), ("MY-MEMORY-MIB", "myNodeMemoryPoolSize"), ("MY-MEMORY-MIB", "myNodeMemoryPoolUsed"), ("MY-MEMORY-MIB", "myNodeMemoryPoolFree"), ("MY-MEMORY-MIB", "myNodeMemoryPoolWarning"), ("MY-MEMORY-MIB", "myNodeMemoryPoolCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNodeMemoryPoolMIBGroup = myNodeMemoryPoolMIBGroup.setStatus('current')
mibBuilder.exportSymbols("MY-MEMORY-MIB", myMemoryPoolUtilizationEntry=myMemoryPoolUtilizationEntry, myMemoryMIBCompliances=myMemoryMIBCompliances, Percent=Percent, myNodeMemoryPoolSize=myNodeMemoryPoolSize, myMemoryPoolIndex=myMemoryPoolIndex, myNodeMemoryPoolLowestUtilization=myNodeMemoryPoolLowestUtilization, myMemoryPoolName=myMemoryPoolName, myMemoryPoolUsed=myMemoryPoolUsed, PYSNMP_MODULE_ID=myMemoryMIB, myMemoryPoolUtilizationMIBGroup=myMemoryPoolUtilizationMIBGroup, myNodeMemoryPoolMIBGroup=myNodeMemoryPoolMIBGroup, myMemoryMIBCompliance=myMemoryMIBCompliance, myMemoryPoolWarning=myMemoryPoolWarning, myMemoryPoolLargestUtilization=myMemoryPoolLargestUtilization, myNodeMemoryPoolTable=myNodeMemoryPoolTable, myNodeMemoryPoolCurrentUtilization=myNodeMemoryPoolCurrentUtilization, myMemoryPoolCritical=myMemoryPoolCritical, myMemoryPoolMIBObjects=myMemoryPoolMIBObjects, myMemoryPoolSize=myMemoryPoolSize, myNodeMemoryPoolIndex=myNodeMemoryPoolIndex, myMemoryPoolUtilizationTable=myMemoryPoolUtilizationTable, myMemoryPoolCurrentUtilization=myMemoryPoolCurrentUtilization, myNodeMemoryPoolEntry=myNodeMemoryPoolEntry, myMemoryMIB=myMemoryMIB, myMemoryPoolLowestUtilization=myMemoryPoolLowestUtilization, myMemoryPoolFree=myMemoryPoolFree, myMemoryMIBGroups=myMemoryMIBGroups, myNodeMemoryPoolUsed=myNodeMemoryPoolUsed, myNodeMemoryPoolName=myNodeMemoryPoolName, myMemoryMIBConformance=myMemoryMIBConformance, myNodeMemoryPoolWarning=myNodeMemoryPoolWarning, myNodeMemoryPoolFree=myNodeMemoryPoolFree, myNodeMemoryPoolLargestUtilization=myNodeMemoryPoolLargestUtilization, myNodeMemoryPoolCritical=myNodeMemoryPoolCritical)