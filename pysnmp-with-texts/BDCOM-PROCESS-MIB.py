#
# PySNMP MIB module BDCOM-PROCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BDCOM-PROCESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
bdMgmt, = mibBuilder.importSymbols("BDCOM-SMI", "bdMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("BDCOM-TC", "EntPhysicalIndexOrZero")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, TimeTicks, IpAddress, Integer32, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Counter32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "TimeTicks", "IpAddress", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Counter32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
bdcomProcessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320, 9, 109))
bdcomProcessMIB.setRevisions(('2003-10-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bdcomProcessMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: bdcomProcessMIB.setLastUpdated('200311060000Z')
if mibBuilder.loadTexts: bdcomProcessMIB.setOrganization('BDCOM, Inc.')
if mibBuilder.loadTexts: bdcomProcessMIB.setContactInfo(' Tel: +86-21-50800666 Postal: No.123,Juli RD,Zhangjiang Hitech Park, Shanghai Baud Data Communication Corporation Inc, Shanghai City 201203, P.R.C ')
if mibBuilder.loadTexts: bdcomProcessMIB.setDescription('The MIB module to describe active system processes.')
bdcomProcessMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1))
bdpmCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1))
bdpmProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2))
bdpmCPUTotalTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1), )
if mibBuilder.loadTexts: bdpmCPUTotalTable.setStatus('current')
if mibBuilder.loadTexts: bdpmCPUTotalTable.setDescription('A table of overall CPU statistics. ')
bdpmCPUTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1), ).setIndexNames((0, "BDCOM-PROCESS-MIB", "bdpmCPUTotalIndex"))
if mibBuilder.loadTexts: bdpmCPUTotalEntry.setStatus('current')
if mibBuilder.loadTexts: bdpmCPUTotalEntry.setDescription('Overall information about the CPU load. Entries in this table come and go as CPUs are added and removed from the system.')
bdpmCPUTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: bdpmCPUTotalIndex.setStatus('current')
if mibBuilder.loadTexts: bdpmCPUTotalIndex.setDescription('An index that uniquely represents a CPU (or group of CPUs) whose CPU load information is reported by a row in this table. This index is assigned arbitrarily by the engine and is not saved over reboots.')
bdpmCPUTotalPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 2), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdpmCPUTotalPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: bdpmCPUTotalPhysicalIndex.setDescription('The entPhysicalIndex of the physical entity for which the CPU statistics in this entry are maintained. The physical entity can be a CPU chip, a group of CPUs, a CPU card etc. The exact type of this entity is described by its entPhysicalVendorType value. If the CPU statistics in this entry correspond to more than one physical entity (or to no physical entity), or if the entPhysicalTable is not supported on the SNMP agent, the value of this object must be zero.')
bdpmCPUTotal5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdpmCPUTotal5sec.setStatus('current')
if mibBuilder.loadTexts: bdpmCPUTotal5sec.setDescription('The overall CPU busy percentage in the last 5 second period. This object obsoletes the busyPer object from the OLD-CISCO-SYSTEM-MIB. This object is deprecated by bdpmCPUTotal5secRev which has the changed range of value (0..100).')
bdpmCPUTotal1min = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdpmCPUTotal1min.setStatus('current')
if mibBuilder.loadTexts: bdpmCPUTotal1min.setDescription('The overall CPU busy percentage in the last 1 minute period. This object obsoletes the avgBusy1 object from the OLD-CISCO-SYSTEM-MIB. This object is deprecated by bdpmCPUTotal1minRev which has the changed range of value (0..100).')
bdpmCPUTotal5min = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdpmCPUTotal5min.setStatus('current')
if mibBuilder.loadTexts: bdpmCPUTotal5min.setDescription('The overall CPU busy percentage in the last 5 minute period. This object deprecates the avgBusy5 object from the OLD-CISCO-SYSTEM-MIB. This object is deprecated by bdpmCPUTotal5minRev which has the changed range of value (0..100).')
bdpmProcessTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1), )
if mibBuilder.loadTexts: bdpmProcessTable.setStatus('current')
if mibBuilder.loadTexts: bdpmProcessTable.setDescription('A table of generic information on all active processes on this device.')
bdpmProcessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1), ).setIndexNames((0, "BDCOM-PROCESS-MIB", "bdpmCPUTotalIndex"), (0, "BDCOM-PROCESS-MIB", "bdpmProcessPID"))
if mibBuilder.loadTexts: bdpmProcessEntry.setStatus('current')
if mibBuilder.loadTexts: bdpmProcessEntry.setDescription('Generic information about an active process on this device. Entries in this table come and go as processes are created and destroyed by the device.')
bdpmProcessPID = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdpmProcessPID.setStatus('current')
if mibBuilder.loadTexts: bdpmProcessPID.setDescription('This object contains the process ID. bdpmProcessTimeCreated should be checked against the last time it was polled, and if it has changed the PID has been reused and the entire entry should be polled again. The process IDs are discrete.')
bdpmProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdpmProcessName.setStatus('current')
if mibBuilder.loadTexts: bdpmProcessName.setDescription("The name associated with this process. If the name is longer than 32 characters, it will be truncated to the first 31 characters, and a `*' will be appended as the last character to imply this is a truncated process name.")
bdpmProcessPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 55, 60, 128, 180, 255))).clone(namedValues=NamedValues(("critical", 0), ("veryhigh", 55), ("high", 60), ("normal", 128), ("low", 180), ("verylow", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdpmProcessPriority.setStatus('current')
if mibBuilder.loadTexts: bdpmProcessPriority.setDescription('The priority level at which the process is running. This object is deprecated by bdpmProcExtPriorityRev.')
bdpmProcessTimeCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdpmProcessTimeCreated.setStatus('current')
if mibBuilder.loadTexts: bdpmProcessTimeCreated.setDescription('The time when the process was created. The process ID and the time when the process was created, uniquely identifies a process.')
bdcomProcessMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 109, 2))
bdcomProcessMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 109, 2, 0))
mibBuilder.exportSymbols("BDCOM-PROCESS-MIB", bdpmCPUTotalTable=bdpmCPUTotalTable, bdpmCPUTotalEntry=bdpmCPUTotalEntry, bdpmProcessTable=bdpmProcessTable, bdcomProcessMIBNotifPrefix=bdcomProcessMIBNotifPrefix, bdpmProcessEntry=bdpmProcessEntry, bdpmCPUTotal5min=bdpmCPUTotal5min, bdpmCPUTotalPhysicalIndex=bdpmCPUTotalPhysicalIndex, bdpmProcess=bdpmProcess, bdpmCPUTotal5sec=bdpmCPUTotal5sec, bdpmCPUTotalIndex=bdpmCPUTotalIndex, bdpmProcessPID=bdpmProcessPID, bdcomProcessMIBNotifs=bdcomProcessMIBNotifs, bdpmProcessPriority=bdpmProcessPriority, bdpmProcessName=bdpmProcessName, PYSNMP_MODULE_ID=bdcomProcessMIB, bdpmCPU=bdpmCPU, bdpmCPUTotal1min=bdpmCPUTotal1min, bdcomProcessMIB=bdcomProcessMIB, bdpmProcessTimeCreated=bdpmProcessTimeCreated, bdcomProcessMIBObjects=bdcomProcessMIBObjects)
