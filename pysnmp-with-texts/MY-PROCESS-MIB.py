#
# PySNMP MIB module MY-PROCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-PROCESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:16:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, TimeTicks, ObjectIdentity, iso, MibIdentifier, Counter32, ModuleIdentity, Bits, Integer32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "ObjectIdentity", "iso", "MibIdentifier", "Counter32", "ModuleIdentity", "Bits", "Integer32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
myProcessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36))
myProcessMIB.setRevisions(('2003-10-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: myProcessMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: myProcessMIB.setLastUpdated('200310140000Z')
if mibBuilder.loadTexts: myProcessMIB.setOrganization('D-Link Crop.')
if mibBuilder.loadTexts: myProcessMIB.setContactInfo(' http://support.dlink.com')
if mibBuilder.loadTexts: myProcessMIB.setDescription('This module defines my system mibs.')
class Percent(TextualConvention, Integer32):
    description = 'An integer that is in the range of a percent value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

myCPUMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1))
myCpuGeneralMibsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1))
myCPUUtilization5Sec = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 1), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization5Sec.setStatus('current')
if mibBuilder.loadTexts: myCPUUtilization5Sec.setDescription('This is the CPU utilization for 5 seconds.')
myCPUUtilization1Min = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 2), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization1Min.setStatus('current')
if mibBuilder.loadTexts: myCPUUtilization1Min.setDescription('This is the CPU utilization for 1 minutes.')
myCPUUtilization5Min = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization5Min.setStatus('current')
if mibBuilder.loadTexts: myCPUUtilization5Min.setDescription('This is the CPU utilization for 5 minutes.')
myCPUUtilizationWarning = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 4), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCPUUtilizationWarning.setStatus('current')
if mibBuilder.loadTexts: myCPUUtilizationWarning.setDescription('This is the first warning of cpu using rate.')
myCPUUtilizationCritical = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 5), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCPUUtilizationCritical.setStatus('current')
if mibBuilder.loadTexts: myCPUUtilizationCritical.setDescription('This is the second warning of cpu using rate.')
myNodeCPUTotalTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2), )
if mibBuilder.loadTexts: myNodeCPUTotalTable.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotalTable.setDescription("A table of line cards's CPU utilization entries. Each of the objects provides a general idea of how much of the CPU resource of a line card has been used over a given period of time.")
myNodeCPUTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1), ).setIndexNames((0, "MY-PROCESS-MIB", "myNodeCPUTotalIndex"))
if mibBuilder.loadTexts: myNodeCPUTotalEntry.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotalEntry.setDescription("An entry in the node's CPU utilization table.")
myNodeCPUTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotalIndex.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotalIndex.setDescription('An index that uniquely represents a Memory Pool.')
myNodeCPUTotalName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotalName.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotalName.setDescription('The name of a node, for example, slot x is the x slot.')
myNodeCPUTotal5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal5sec.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotal5sec.setDescription('This is the CPU utilization of a node for 5 seconds.')
myNodeCPUTotal1min = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal1min.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotal1min.setDescription('This is the CPU utilization of a node for 1 minutes.')
myNodeCPUTotal5min = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal5min.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotal5min.setDescription('This is the CPU utilization of a node for 5 minutes.')
myNodeCPUTotalWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 6), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeCPUTotalWarning.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotalWarning.setDescription("This is the first warning of the node's cpu using rate.")
myNodeCPUTotalCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 7), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeCPUTotalCritical.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotalCritical.setDescription("This is the second warning of the node's cpu using rate.")
myProcessMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2))
myProcessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1))
myProcessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2))
myProcessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1, 1)).setObjects(("MY-PROCESS-MIB", "myCPUUtilizationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myProcessMIBCompliance = myProcessMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: myProcessMIBCompliance.setDescription('The compliance statement for entities which implement the My Process MIB')
myCPUUtilizationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 1)).setObjects(("MY-PROCESS-MIB", "myCPUUtilization5Sec"), ("MY-PROCESS-MIB", "myCPUUtilization1Min"), ("MY-PROCESS-MIB", "myCPUUtilization5Min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myCPUUtilizationMIBGroup = myCPUUtilizationMIBGroup.setStatus('current')
if mibBuilder.loadTexts: myCPUUtilizationMIBGroup.setDescription('A collection of objects providing CPU utilization to a My agent.')
myNodeCPUTotalGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 2)).setObjects(("MY-PROCESS-MIB", "myNodeCPUTotalIndex"), ("MY-PROCESS-MIB", "myNodeCPUTotalName"), ("MY-PROCESS-MIB", "myNodeCPUTotal5sec"), ("MY-PROCESS-MIB", "myNodeCPUTotal1min"), ("MY-PROCESS-MIB", "myNodeCPUTotal5min"), ("MY-PROCESS-MIB", "myNodeCPUTotalWarning"), ("MY-PROCESS-MIB", "myNodeCPUTotalCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNodeCPUTotalGroups = myNodeCPUTotalGroups.setStatus('current')
if mibBuilder.loadTexts: myNodeCPUTotalGroups.setDescription("A collection of objects providing node's CPU utilization to a My agent.")
mibBuilder.exportSymbols("MY-PROCESS-MIB", myCpuGeneralMibsGroup=myCpuGeneralMibsGroup, myNodeCPUTotalEntry=myNodeCPUTotalEntry, myNodeCPUTotal5min=myNodeCPUTotal5min, myNodeCPUTotal1min=myNodeCPUTotal1min, myCPUUtilizationMIBGroup=myCPUUtilizationMIBGroup, myNodeCPUTotalCritical=myNodeCPUTotalCritical, myCPUUtilization1Min=myCPUUtilization1Min, myNodeCPUTotalTable=myNodeCPUTotalTable, myProcessMIBCompliance=myProcessMIBCompliance, myProcessMIB=myProcessMIB, myNodeCPUTotal5sec=myNodeCPUTotal5sec, PYSNMP_MODULE_ID=myProcessMIB, myCPUUtilization5Min=myCPUUtilization5Min, myNodeCPUTotalGroups=myNodeCPUTotalGroups, myCPUUtilizationCritical=myCPUUtilizationCritical, myNodeCPUTotalWarning=myNodeCPUTotalWarning, myProcessMIBConformance=myProcessMIBConformance, Percent=Percent, myNodeCPUTotalName=myNodeCPUTotalName, myCPUMIBObjects=myCPUMIBObjects, myNodeCPUTotalIndex=myNodeCPUTotalIndex, myProcessMIBCompliances=myProcessMIBCompliances, myCPUUtilizationWarning=myCPUUtilizationWarning, myCPUUtilization5Sec=myCPUUtilization5Sec, myProcessMIBGroups=myProcessMIBGroups)
