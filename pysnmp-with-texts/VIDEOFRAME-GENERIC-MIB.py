#
# PySNMP MIB module VIDEOFRAME-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VIDEOFRAME-GENERIC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
system, = mibBuilder.importSymbols("SNMPv2-MIB", "system")
TimeTicks, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, MibIdentifier, IpAddress, iso, Integer32, Counter64, ModuleIdentity, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "iso", "Integer32", "Counter64", "ModuleIdentity", "Unsigned32", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
vfMIBModules, vfGeneric = mibBuilder.importSymbols("VIDEOFRAME-REGISTRATIONS-MIB", "vfMIBModules", "vfGeneric")
videoframeGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 1, 2))
videoframeGenericMIB.setRevisions(('1901-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: videoframeGenericMIB.setRevisionsDescriptions(('First release.',))
if mibBuilder.loadTexts: videoframeGenericMIB.setLastUpdated('0101190000Z')
if mibBuilder.loadTexts: videoframeGenericMIB.setOrganization('Videoframe Systems')
if mibBuilder.loadTexts: videoframeGenericMIB.setContactInfo('Videoframe Systems P.O. Box 1991, Grass Valley, CA 95945, USA. +1 (530) 477-2000 http://www.videoframesystems.com')
if mibBuilder.loadTexts: videoframeGenericMIB.setDescription('This MIB module describes the generic objects for a manageable device in the Videoframe Systems product line. This MIB does not describe the device specific objects of the managed system, and augments MIB-2 in the identification of a Videoframe Systems managed device. This module will be extended, or modified as required. Videoframe Systems reserves the right to make changes in specification and other information contained in this document without prior notice. The reader should consult Videoframe Systems to determine whether any such changes have been made. In no event shall Videoframe Systems be liable for any incidental, indirect, special, or consequential damages whatsoever (including but not limited to lost profits) arising out of or related to this document or the information contained in it. Videoframe Systems grants vendors, end users, and other interested parties a non-exclusive license to use this specification in connection with the management of Videoframe Systems products. Copyright 2001 Videoframe, Inc.')
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectID.setStatus('current')
if mibBuilder.loadTexts: sysObjectID.setDescription('The standard identification of the managed system this agent represents. These are OIDs from the vfRegistrations branch of the videoframe MIB namespace.')
vfBox = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 3, 1))
vfAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 3, 2))
vfBoxEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 3, 1, 0))
vfMaxBoxes = MibScalar((1, 3, 6, 1, 4, 1, 4596, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfMaxBoxes.setStatus('current')
if mibBuilder.loadTexts: vfMaxBoxes.setDescription('The maximum number of managed boxes that this agent can represent. If the value of this variable is -1, the device is capable of representing a theoretically infinite number of boxes dynamically. In othercases, the maximum number of boxes that can be represented by this device is limited to the value of this variable.')
vfBoxTableNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4596, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfBoxTableNextIndex.setStatus('current')
if mibBuilder.loadTexts: vfBoxTableNextIndex.setDescription('Identifies a hint for the next value of vfBoxEntryIndex to be used in a row creation attempt for the vfBoxTable table. If no new rows can be created, this object will have a value of 0.')
vfBoxTable = MibTable((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3), )
if mibBuilder.loadTexts: vfBoxTable.setStatus('current')
if mibBuilder.loadTexts: vfBoxTable.setDescription('Each row contains information about one generic Videoframe managed box.')
vfBoxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1), ).setIndexNames((0, "VIDEOFRAME-GENERIC-MIB", "vfBoxId"))
if mibBuilder.loadTexts: vfBoxEntry.setStatus('current')
if mibBuilder.loadTexts: vfBoxEntry.setDescription('Information about one generic Videoframe managed box.')
vfBoxEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: vfBoxEntryIndex.setStatus('current')
if mibBuilder.loadTexts: vfBoxEntryIndex.setDescription('The index of a row in the box table.')
vfBoxId = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vfBoxId.setStatus('current')
if mibBuilder.loadTexts: vfBoxId.setDescription('Name of box in system drawings. e.g. GPICTLR-5.')
vfBoxPartNo = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vfBoxPartNo.setStatus('current')
if mibBuilder.loadTexts: vfBoxPartNo.setDescription('Videoframe part no. from nameplate.')
vfBoxPsAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfBoxPsAStatus.setStatus('current')
if mibBuilder.loadTexts: vfBoxPsAStatus.setDescription('Power Supply A Status is on/off.')
vfBoxPsBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfBoxPsBStatus.setStatus('current')
if mibBuilder.loadTexts: vfBoxPsBStatus.setDescription('Power Supply B Status is on/off.')
vfBoxFailoverStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("main", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfBoxFailoverStatus.setStatus('current')
if mibBuilder.loadTexts: vfBoxFailoverStatus.setDescription('This box is currently main(2) or backup(1) of a redundant pair.')
vfBoxTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vfBoxTrapEnable.setStatus('current')
if mibBuilder.loadTexts: vfBoxTrapEnable.setDescription('Enables or disables the Trap that is associated with a box status change event.')
vfBoxSoftwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfBoxSoftwareRev.setStatus('current')
if mibBuilder.loadTexts: vfBoxSoftwareRev.setDescription('The revision of the software (if any) running on the box.')
vfBoxState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vfBoxRunning", 1), ("vfBoxInMaintenance", 2), ("vfBoxFaulty", 3), ("vfBoxDisabled", 4), ("vfBoxIdling", 5), ("vfBoxInitializing", 6), ("vfBoxResetting", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfBoxState.setStatus('current')
if mibBuilder.loadTexts: vfBoxState.setDescription('The operational state of a device. NOTE: It is not mandatory that a managed device support all of the enumerated device states. vfBoxActive(1) - The device is running and processing load. vfBoxInMaintenance(2) - The device is online, but either the device as a whole, or one or more of its components are in maintenance mode. Maintenance mode could be described as a mode where diagnostics are being run on the device, or some tasks such as device configuration are being excuted on the device that has inhibited its normal operation. vfBoxFaulty(3) - The device has experienced a faulty condition in one or more of its components. vfBoxDisabled(4) - The device may not be in a faulty condition, but has been explicitly disabled from its normal mode of operation, such as when selected as the backup of a redundant pair. vfBoxIdling(5) - The device is running in an idle state (no clients are currently active). vfBoxInitializing(6) - This is a post bootstrap state where the device has been restarted, and is initializing its hardware and software components. vfBoxResetting(7) - The device is in a post- reset cycle. Any information collected, or dynamic configuration of the device prior to this state may be lost.')
vfBoxEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vfBoxEntryStatus.setStatus('current')
if mibBuilder.loadTexts: vfBoxEntryStatus.setDescription('This object controls the creation, activation and deletion of a row in the box table.')
boxPsAEvent = NotificationType((1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 1)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-GENERIC-MIB", "vfBoxPsAStatus"))
if mibBuilder.loadTexts: boxPsAEvent.setStatus('current')
if mibBuilder.loadTexts: boxPsAEvent.setDescription('Box Power Supply A changed status.')
boxPsBEvent = NotificationType((1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 2)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-GENERIC-MIB", "vfBoxPsAStatus"))
if mibBuilder.loadTexts: boxPsBEvent.setStatus('current')
if mibBuilder.loadTexts: boxPsBEvent.setDescription('Box Power Supply B changed status.')
boxFailoverEvent = NotificationType((1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 3)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-GENERIC-MIB", "vfBoxFailoverStatus"))
if mibBuilder.loadTexts: boxFailoverEvent.setStatus('current')
if mibBuilder.loadTexts: boxFailoverEvent.setDescription('Box failover status changed.')
boxStateChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 4)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-GENERIC-MIB", "vfBoxState"))
if mibBuilder.loadTexts: boxStateChangeEvent.setStatus('current')
if mibBuilder.loadTexts: boxStateChangeEvent.setDescription('Notifies when a state change occurs on an device. The vfBoxState variable will hold the new state that the device is operating in.')
vfAgentTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4596, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vfAgentTrapEnable.setStatus('current')
if mibBuilder.loadTexts: vfAgentTrapEnable.setDescription('Enables or disables all Traps from this agent.')
vfTrapTargMaxTargets = MibScalar((1, 3, 6, 1, 4, 1, 4596, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfTrapTargMaxTargets.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargMaxTargets.setDescription('The maximum number of trap targets that this device can support. If the value of this variable is -1, the device is capable of supporting a theoretically infinite number of trap targets dynamically. In othercases, the maximum number of trap targets that can be supported by this device is limited to the value of this variable.')
vfTrapTargCfgTableNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4596, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vfTrapTargCfgTableNextIndex.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargCfgTableNextIndex.setDescription('Identifies a hint for the next value of vfTrapTargCfgIndex to be used in a row creation attempt for the vfTrapTargCfgTable table. If no new rows can be created, this object will have a value of 0.')
vfTrapTargCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4596, 3, 2, 4), )
if mibBuilder.loadTexts: vfTrapTargCfgTable.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargCfgTable.setDescription("A list of trap target configuration entries on this device. Trap Target Configuration Entry Creation: ========================================= When creating a trap target configuration entry the manager should use a GET operation to determine the value of vfTrapTargCfgTableNextIndex.0. If this value is non-zero, the manager can then use this value as the index while creating a table row. The process of creating and activating a row of this table takes two forms: the one-set mode and the multiple-set mode. In the one-set mode, a manager must specify the values of vfTrapTargCfgIpAddress and vfTrapTargCfgCommunity required to activate a row in a single SET operation along with an assignment of the vfTrapTargCfgEntryStatus to 'createAndGo(4)'. If the values and instances supplied are correct, an instance of the trap target configuration is created and the value of vfTrapTargCfgEntryStatus transitions to 'active(1)'. for example: ============ SnmpGet(<vfTrapTargCfgTableNextIndex.0, NULL>) returns <vfTrapTargCfgTableNextIndex.0, 2> SnmpSet(<vfTrapTargCfgIpAddress.2, 192.168.1.8>, <vfTrapTargCfgCommunity.2, 'public'>, <vfTrapTargCfgEntryStatus.2, createAndGo(4)>) returns <vfTrapTargCfgIpAddress.2, 192.168.1.8>, <vfTrapTargCfgCommunity.2, 'public'>, <vfTrapTargCfgEntryStatus.2, active(1)> In the multiple-set mode, creating a trap target configuration table row, filling it with values, and activating it are carried out in discrete steps. To create the row, the manager specifies a value of 'createAndWait(5)' for the vfTrapTargCfgEntryStatus status variable. This SET request could contain values of vfTrapTargCfgIpAddress and vfTrapTargCfgCommunity but it is not required. More often, the values for these columnar objects are specified in additional SET requests. After each SET operation, the vfTrapTargCfgEntryStatus variable takes on the value 'notReady(3)' or 'notInService(2)'. To place the entry into service, the manager requests that the vfTrapTargCfgEntryStatus variable transition to the 'active(1)' state. for example: ============ SnmpGet(<vfTrapTargCfgTableNextIndex.0>, NULL) returns <vfTrapTargCfgTableNextIndex.0, 2> SnmpSet(<vfTrapTargCfgEntryStatus.2, createAndWait(5)>) returns <vfTrapTargCfgEntryStatus.2, notReady(3)> SnmpSet(<vfTrapTargCfgIpAddress.2, 192.168.1.8>, <vfTrapTargCfgCommunity.2, 'public'>) returns <vfTrapTargCfgIpAddress.2, 192.168.1.8>, <vfTrapTargCfgCommunity.2, 'public'> SnmpSet(<vfTrapTargCfgEntryStatus.2, active(1)>) returns <vfTrapTargCfgEntryStatus.2, active(1)> Trap Target Configuration Entry Deletion: ========================================= To delete an existing trap target configuration entry, the manager performs a SET operation on the vfTrapTargCfgEntryStatus variable with the value 'destroy(6)'.")
vfTrapTargCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1), ).setIndexNames((0, "VIDEOFRAME-GENERIC-MIB", "vfTrapTargCfgIndex"))
if mibBuilder.loadTexts: vfTrapTargCfgEntry.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargCfgEntry.setDescription('A trap target configuration entry.')
vfTrapTargCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: vfTrapTargCfgIndex.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargCfgIndex.setDescription('The index of a trap target configuration row. Note that the value of this object will not be visible to a manager and any GET/SET operations on this variable will fail.')
vfTrapTargCfgIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vfTrapTargCfgIpAddress.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargCfgIpAddress.setDescription('The IP address of the target/manager to which this device is supposed to send notifications.')
vfTrapTargCfgCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vfTrapTargCfgCommunity.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargCfgCommunity.setDescription('The community name to be used when this device sends notifications to the target identified by the value of this entries vfTrapTargCfgIpAddress.')
vfTrapTargCfgEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vfTrapTargCfgEntryStatus.setStatus('current')
if mibBuilder.loadTexts: vfTrapTargCfgEntryStatus.setDescription('This object controls the creation, activation and deletion of a row in the trap target configuration table.')
mibBuilder.exportSymbols("VIDEOFRAME-GENERIC-MIB", sysObjectID=sysObjectID, vfAgentTrapEnable=vfAgentTrapEnable, vfTrapTargCfgEntry=vfTrapTargCfgEntry, vfBoxTable=vfBoxTable, vfTrapTargCfgIpAddress=vfTrapTargCfgIpAddress, vfTrapTargCfgIndex=vfTrapTargCfgIndex, vfTrapTargCfgCommunity=vfTrapTargCfgCommunity, vfTrapTargCfgTableNextIndex=vfTrapTargCfgTableNextIndex, vfTrapTargCfgEntryStatus=vfTrapTargCfgEntryStatus, boxStateChangeEvent=boxStateChangeEvent, vfBoxEntryStatus=vfBoxEntryStatus, boxFailoverEvent=boxFailoverEvent, vfMaxBoxes=vfMaxBoxes, vfTrapTargCfgTable=vfTrapTargCfgTable, vfAgent=vfAgent, vfBoxEntry=vfBoxEntry, PYSNMP_MODULE_ID=videoframeGenericMIB, vfBoxFailoverStatus=vfBoxFailoverStatus, vfBoxSoftwareRev=vfBoxSoftwareRev, boxPsAEvent=boxPsAEvent, vfBoxTrapEnable=vfBoxTrapEnable, vfTrapTargMaxTargets=vfTrapTargMaxTargets, videoframeGenericMIB=videoframeGenericMIB, vfBoxEntryIndex=vfBoxEntryIndex, vfBoxTableNextIndex=vfBoxTableNextIndex, vfBoxState=vfBoxState, vfBoxPartNo=vfBoxPartNo, vfBoxEvents=vfBoxEvents, vfBoxPsBStatus=vfBoxPsBStatus, vfBox=vfBox, vfBoxPsAStatus=vfBoxPsAStatus, boxPsBEvent=boxPsBEvent, vfBoxId=vfBoxId)
