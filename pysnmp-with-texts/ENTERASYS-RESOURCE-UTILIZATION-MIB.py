#
# PySNMP MIB module ENTERASYS-RESOURCE-UTILIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-RESOURCE-UTILIZATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Counter64, Integer32, NotificationType, Bits, IpAddress, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Counter64", "Integer32", "NotificationType", "Bits", "IpAddress", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysResourceUtilizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49))
etsysResourceUtilizationMIB.setRevisions(('2009-11-02 15:41', '2004-11-30 16:33',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysResourceUtilizationMIB.setRevisionsDescriptions(('Added the usbFlash(4) enumeration to the ResourceStorageType TEXTUAL-CONVENTION.', 'The initial version of this MIB module',))
if mibBuilder.loadTexts: etsysResourceUtilizationMIB.setLastUpdated('200911021541Z')
if mibBuilder.loadTexts: etsysResourceUtilizationMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysResourceUtilizationMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysResourceUtilizationMIB.setDescription("This module provides authoritative definitions for Enterasys Networks' Resource Utilization MIB.")
class ResourceStorageType(TextualConvention, Integer32):
    description = 'This data type is used as the syntax of the etsysResourceStorageType object in the definition of the etsysResourceStorageTable. other(1) storage type not defined by textual convention ram(2) volatile storage flash(3) nonvolatile storage usbFlash(4) nonvolatile USB stick flash storage'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("ram", 2), ("flash", 3), ("usbFlash", 4))

class ResourceUtilization(TextualConvention, Integer32):
    description = 'This data type is used as the syntax for objects which report the utilization of a resource as a percentage of a defined period of time. Each value embeds the first digit to the right of the decimal, 1/10ths of a percent, by multiplying the utilization by 10. For example, a utilization of 95.7 encodes to a ResourceUtilization value of 957.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1000)

etsysResourceUtilizationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1))
etsysResourceUtilizationNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 0))
etsysResourceCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1))
etsysResourceProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2))
etsysResourceStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3))
etsysResourceScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 4))
etsysResourceCpuTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1), )
if mibBuilder.loadTexts: etsysResourceCpuTable.setStatus('current')
if mibBuilder.loadTexts: etsysResourceCpuTable.setDescription('The table of processors contained in the chassis.')
etsysResourceCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuId"))
if mibBuilder.loadTexts: etsysResourceCpuEntry.setStatus('current')
if mibBuilder.loadTexts: etsysResourceCpuEntry.setDescription('An entry for a processor contained in the system. The entPhysicalIndex represents the chassis module the processor is contained in.')
etsysResourceCpuId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysResourceCpuId.setStatus('current')
if mibBuilder.loadTexts: etsysResourceCpuId.setDescription('A value assigned to the processor. Each value needs only to be unique for the module identified by the entPhysicalIndex of this entry.')
etsysResourceCpuLoad5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 2), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceCpuLoad5sec.setStatus('current')
if mibBuilder.loadTexts: etsysResourceCpuLoad5sec.setDescription('The average, over the last 5 seconds, of the percentage of time that this processor was not idle.')
etsysResourceCpuLoad1min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 3), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceCpuLoad1min.setStatus('current')
if mibBuilder.loadTexts: etsysResourceCpuLoad1min.setDescription('The average, over the last 1 minute, of the percentage of time that this processor was not idle.')
etsysResourceCpuLoad5min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 4), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceCpuLoad5min.setStatus('current')
if mibBuilder.loadTexts: etsysResourceCpuLoad5min.setDescription('The average, over the last 5 minutes, of the percentage of time that this processor was not idle.')
etsysResourceProcessTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1), )
if mibBuilder.loadTexts: etsysResourceProcessTable.setStatus('current')
if mibBuilder.loadTexts: etsysResourceProcessTable.setDescription('The table of processes running in the chassis.')
etsysResourceProcessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuId"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessID"))
if mibBuilder.loadTexts: etsysResourceProcessEntry.setStatus('current')
if mibBuilder.loadTexts: etsysResourceProcessEntry.setDescription('An entry for a process running in the chassis. The etsysResourceCpuId identifies the processor the process is running in. ')
etsysResourceProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysResourceProcessID.setStatus('current')
if mibBuilder.loadTexts: etsysResourceProcessID.setDescription('A value assigned to the process. This value is only unique per processor, not per chassis.')
etsysResourceProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessName.setStatus('current')
if mibBuilder.loadTexts: etsysResourceProcessName.setDescription('A textual description of this running process.')
etsysResourceProcessLoad5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 3), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessLoad5sec.setStatus('current')
if mibBuilder.loadTexts: etsysResourceProcessLoad5sec.setDescription('The average, over the last 5 seconds, of the percentage of time that this process was not idle.')
etsysResourceProcessLoad1min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 4), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessLoad1min.setStatus('current')
if mibBuilder.loadTexts: etsysResourceProcessLoad1min.setDescription('The average, over the last 1 minute, of the percentage of time that this process was not idle.')
etsysResourceProcessLoad5min = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 5), ResourceUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceProcessLoad5min.setStatus('current')
if mibBuilder.loadTexts: etsysResourceProcessLoad5min.setDescription('The average, over the last 5 minutes, of the percentage of time that this process was not idle.')
etsysResourceStorageTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1), )
if mibBuilder.loadTexts: etsysResourceStorageTable.setStatus('current')
if mibBuilder.loadTexts: etsysResourceStorageTable.setDescription('The Table of storage utilization in the chassis.')
etsysResourceStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageType"), (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageTypeID"))
if mibBuilder.loadTexts: etsysResourceStorageEntry.setStatus('current')
if mibBuilder.loadTexts: etsysResourceStorageEntry.setDescription('An entry for one storage area in the chassis.')
etsysResourceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 1), ResourceStorageType())
if mibBuilder.loadTexts: etsysResourceStorageType.setStatus('current')
if mibBuilder.loadTexts: etsysResourceStorageType.setDescription('The type of storage represented by this entry.')
etsysResourceStorageTypeID = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: etsysResourceStorageTypeID.setStatus('current')
if mibBuilder.loadTexts: etsysResourceStorageTypeID.setDescription('A unique arbitrary value per storage type assigned to the entry.')
etsysResourceStorageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceStorageDescr.setStatus('current')
if mibBuilder.loadTexts: etsysResourceStorageDescr.setDescription('A textual description of this storage area.')
etsysResourceStorageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceStorageSize.setStatus('current')
if mibBuilder.loadTexts: etsysResourceStorageSize.setDescription('The size, in Kilobytes, of the storage area.')
etsysResourceStorageAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysResourceStorageAvailable.setStatus('current')
if mibBuilder.loadTexts: etsysResourceStorageAvailable.setDescription('The available space, in Kilobytes, left on the storage area.')
etsysResource1minThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 4, 1), ResourceUtilization().clone(800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysResource1minThreshold.setStatus('current')
if mibBuilder.loadTexts: etsysResource1minThreshold.setDescription('The threshold for generating etsysResourceLoad1minThresholdExceeded Notifications. Setting this object to 0 will prevent the agent from generating etsysResourceCpuLoad1minThresholdExceeded notifications. When this object is set to a nonzero value, the agent will generate etsysResourceLoad1minThresholdExceeded notifications when it is detected that an etsysResourceCpuLoad1min object value has exceeded this threshold value. After the threshold has been exceeded additional notifications will be sent once a minute until the corresponding etsysResourceCpuLoad1min drops back below the threshold.')
etsysResourceCpuLoad1minThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 0, 1)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1min"))
if mibBuilder.loadTexts: etsysResourceCpuLoad1minThresholdExceeded.setStatus('current')
if mibBuilder.loadTexts: etsysResourceCpuLoad1minThresholdExceeded.setDescription('This notification indicates that the average, over the last 1 minute, of the percentage of time that a processor was not idle, has exceeded the etsysResourceCpuLoad1minThreshold value.')
etsysResourceUtilizationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2))
etsysResourceUtilizationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1))
etsysResourceUtilizationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 2))
etsysResourceUtilizationCpuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 1)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad5sec"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1min"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationCpuGroup = etsysResourceUtilizationCpuGroup.setStatus('current')
if mibBuilder.loadTexts: etsysResourceUtilizationCpuGroup.setDescription('A collection of objects providing basic instrumentation of CPU Resource Utilization.')
etsysResourceUtilizationProcessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 2)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessName"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad5sec"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad1min"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationProcessGroup = etsysResourceUtilizationProcessGroup.setStatus('current')
if mibBuilder.loadTexts: etsysResourceUtilizationProcessGroup.setDescription('A collection of objects providing basic instrumentation of Process Resource Utilization.')
etsysResourceUtilizationStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 3)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageDescr"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageSize"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationStorageGroup = etsysResourceUtilizationStorageGroup.setStatus('current')
if mibBuilder.loadTexts: etsysResourceUtilizationStorageGroup.setDescription('A collection of objects providing basic instrumentation of Storage Resource Utilization.')
etsysResourceUtilizationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 4)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1minThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationNotificationGroup = etsysResourceUtilizationNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysResourceUtilizationNotificationGroup.setDescription('The utilization threshold exceeded Notification.')
etsysResourceUtilizationScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 5)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResource1minThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationScalarsGroup = etsysResourceUtilizationScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: etsysResourceUtilizationScalarsGroup.setDescription('A collection of objects providing basic instrumentation for Threshold configuration.')
etsysResourceUtilizationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 2, 1)).setObjects(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationCpuGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationProcessGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationStorageGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationNotificationGroup"), ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceUtilizationScalarsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysResourceUtilizationCompliance = etsysResourceUtilizationCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysResourceUtilizationCompliance.setDescription('The compliance statement for devices that support the Enterasys Resource Utilization MIB.')
mibBuilder.exportSymbols("ENTERASYS-RESOURCE-UTILIZATION-MIB", etsysResourceCpuLoad1minThresholdExceeded=etsysResourceCpuLoad1minThresholdExceeded, etsysResourceCpuEntry=etsysResourceCpuEntry, etsysResourceUtilizationNotifications=etsysResourceUtilizationNotifications, etsysResourceProcessEntry=etsysResourceProcessEntry, etsysResourceScalars=etsysResourceScalars, etsysResourceUtilizationGroups=etsysResourceUtilizationGroups, etsysResourceUtilizationNotificationGroup=etsysResourceUtilizationNotificationGroup, etsysResourceCpuTable=etsysResourceCpuTable, etsysResourceUtilizationCpuGroup=etsysResourceUtilizationCpuGroup, etsysResourceUtilizationConformance=etsysResourceUtilizationConformance, etsysResourceStorage=etsysResourceStorage, etsysResourceStorageDescr=etsysResourceStorageDescr, etsysResourceProcessID=etsysResourceProcessID, etsysResourceProcess=etsysResourceProcess, etsysResourceStorageTable=etsysResourceStorageTable, etsysResourceCpuId=etsysResourceCpuId, etsysResourceCpuLoad5sec=etsysResourceCpuLoad5sec, etsysResourceProcessName=etsysResourceProcessName, etsysResourceStorageAvailable=etsysResourceStorageAvailable, ResourceStorageType=ResourceStorageType, etsysResourceProcessLoad1min=etsysResourceProcessLoad1min, etsysResourceProcessLoad5sec=etsysResourceProcessLoad5sec, etsysResourceStorageType=etsysResourceStorageType, etsysResourceStorageTypeID=etsysResourceStorageTypeID, etsysResourceUtilizationCompliances=etsysResourceUtilizationCompliances, etsysResourceUtilizationCompliance=etsysResourceUtilizationCompliance, etsysResourceProcessLoad5min=etsysResourceProcessLoad5min, etsysResourceUtilizationObjects=etsysResourceUtilizationObjects, etsysResource1minThreshold=etsysResource1minThreshold, PYSNMP_MODULE_ID=etsysResourceUtilizationMIB, ResourceUtilization=ResourceUtilization, etsysResourceCpuLoad1min=etsysResourceCpuLoad1min, etsysResourceUtilizationStorageGroup=etsysResourceUtilizationStorageGroup, etsysResourceUtilizationProcessGroup=etsysResourceUtilizationProcessGroup, etsysResourceProcessTable=etsysResourceProcessTable, etsysResourceStorageSize=etsysResourceStorageSize, etsysResourceStorageEntry=etsysResourceStorageEntry, etsysResourceUtilizationMIB=etsysResourceUtilizationMIB, etsysResourceCpu=etsysResourceCpu, etsysResourceCpuLoad5min=etsysResourceCpuLoad5min, etsysResourceUtilizationScalarsGroup=etsysResourceUtilizationScalarsGroup)
