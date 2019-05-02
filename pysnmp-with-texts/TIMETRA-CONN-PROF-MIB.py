#
# PySNMP MIB module TIMETRA-CONN-PROF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-CONN-PROF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, Counter64, TimeTicks, ObjectIdentity, MibIdentifier, ModuleIdentity, IpAddress, NotificationType, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Counter64", "TimeTicks", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "IpAddress", "NotificationType", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32")
DisplayString, TimeStamp, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention", "RowStatus")
tmnxSRConfs, timetraSRMIBModules, tmnxSRObjs, tmnxSRNotifyPrefix = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRConfs", "timetraSRMIBModules", "tmnxSRObjs", "tmnxSRNotifyPrefix")
TmnxEncapVal, TItemDescription = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxEncapVal", "TItemDescription")
timetraConnProfMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 75))
timetraConnProfMIBModule.setRevisions(('2011-02-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraConnProfMIBModule.setRevisionsDescriptions(('Rev 1.0 1 Feb 2011 00:00 Initial Release of the TIMETRA-CONN-PROF-MIB in SROS 9.0.',))
if mibBuilder.loadTexts: timetraConnProfMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraConnProfMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: timetraConnProfMIBModule.setContactInfo('Alcatel-Lucent SROS Support Web: http://support.alcatel-lucent.com')
if mibBuilder.loadTexts: timetraConnProfMIBModule.setDescription("This document is the SNMP MIB module to manage connection profiles associated with VLL services of the Alcatel-Lucent SROS system. Copyright (c) 2012 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel-Lucent's proprietary intellectual property. Alcatel-Lucent retains all title and ownership in the Specification, including any revisions. Alcatel-Lucent grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel-Lucent products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied `as is', and Alcatel-Lucent makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
tmnxConnProfObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75))
tmnxConnProfNtfyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 75))
tmnxConnProfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75))
tmnxConnProfConfigTimeStamps = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1))
tmnxConnProfConfigObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2))
tmnxConnProfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 75, 0))
tmnxConnProfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 1))
tmnxConnProfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2))
class TmnxConnProfId(TextualConvention, Unsigned32):
    description = 'A number used to identify a connection profile. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1000), )
class TmnxConnProfVlanRanges(DisplayString):
    description = 'String which represents vlan range of a connection profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 200)

tmnxConnProfTblLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxConnProfTblLastChanged.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfTblLastChanged.setDescription('The value of tmnxConnProfTblLastChanged indicates the time, since system startup, when the tmnxConnProfTable last changed state.')
tmnxConnProfTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1), )
if mibBuilder.loadTexts: tmnxConnProfTable.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfTable.setDescription('The tmnxConnProfTable contains an entry for each connection profile.')
tmnxConnProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1), ).setIndexNames((0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfId"))
if mibBuilder.loadTexts: tmnxConnProfEntry.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfEntry.setDescription('Each tmnxConnProfEntry contains connection profile specific configuration.')
tmnxConnProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 1), TmnxConnProfId())
if mibBuilder.loadTexts: tmnxConnProfId.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfId.setDescription('The value of tmnxConnProfId specifies the index to a specific connection profile. tmnxConnProfId is system unique.')
tmnxConnProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfRowStatus.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfRowStatus.setDescription("The value of tmnxConnProfRowStatus specifies the row status. It allows entries to be created and deleted in the tmnxConnProfTable. Rows are created by specifying the value of 'createAndGo(4)' and deleted by specifying the value of 'destroy(6)'. To delete an entry, all references to the connection profile in existing SAPs and in tmnxConnProfAtmMemberTable must be deleted.")
tmnxConnProfLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxConnProfLastChanged.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfLastChanged.setDescription('The value of tmnxConnProfLastChanged indicates the time, since system startup, that the connection profile was created or modified.')
tmnxConnProfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 4), TItemDescription()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfDescription.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfDescription.setDescription('The value of tmnxConnProfDescription specifies the description of this connection profile.')
tmnxConnProfVlanRange = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 5), TmnxConnProfVlanRanges()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfVlanRange.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfVlanRange.setDescription('The value of tmnxConnProfVlanRange specifies the vlan ranges of this connection profile.')
tmnxConnProfAtmMemberTblLastChgd = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxConnProfAtmMemberTblLastChgd.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfAtmMemberTblLastChgd.setDescription('The value of tmnxConnProfAtmMemberTblLastChgd indicates the time, since system startup, when the tmnxConnProfAtmMemberTable last changed state.')
tmnxConnProfAtmMemberTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2), )
if mibBuilder.loadTexts: tmnxConnProfAtmMemberTable.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfAtmMemberTable.setDescription("The tmnxConnProfAtmMemberTable contains an entry for each ATM connection profile member. Each ATM connection profile member is a VPI/VCI value to be assigned to an ATM SAP of an APIPE VLL service with TIMETRA-SERV-MIB:svcVllType set to a value of 'atmCell(7)'. Up to a maximum of 16 ATM connection profile members can be added to a connection profile.")
tmnxConnProfAtmMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1), ).setIndexNames((0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfId"), (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberEncapValue"))
if mibBuilder.loadTexts: tmnxConnProfAtmMemberEntry.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfAtmMemberEntry.setDescription('Each tmnxConnProfAtmMemberEntry contains ATM connection profile member specific configuration.')
tmnxConnProfAtmMemberEncapValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1, 1), TmnxEncapVal())
if mibBuilder.loadTexts: tmnxConnProfAtmMemberEncapValue.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfAtmMemberEncapValue.setDescription('The value of tmnxConnProfAtmMemberEncapValue specifies, along with tmnxConnProfId, the index to a specific ATM connection profile member. The TmnxEncapVal supported is ATM VC, for which the top 3 bits are 000.')
tmnxConnProfAtmMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfAtmMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfAtmMemberRowStatus.setDescription("The value of tmnxConnProfAtmMemberRowStatus specifies the row status. It allows entries to be created and deleted in the tmnxConnProfAtmMemberTable. Rows are created by specifying the value of 'createAndGo(4)' and deleted by specifying the value of 'destroy(6)'.")
tmnxConnProfV9v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 1, 1)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfTimeStampGroup"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfGroup"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfV9v0Compliance = tmnxConnProfV9v0Compliance.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfV9v0Compliance.setDescription('The compliance statement for management of connection profiles on Alcatel-Lucent SROS series systems for release 9.0.')
tmnxConnV9v0Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1))
tmnxConnProfTimeStampGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 1)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfTblLastChanged"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberTblLastChgd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfTimeStampGroup = tmnxConnProfTimeStampGroup.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfTimeStampGroup.setDescription('The group of objects maintaining table/row statistics for connection profile tables on Alcatel-Lucent SROS series systems.')
tmnxConnProfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 2)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfRowStatus"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfLastChanged"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfDescription"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanRange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfGroup = tmnxConnProfGroup.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfGroup.setDescription('The group of objects supporting management of connection profiles on Alcatel-Lucent SROS series systems.')
tmnxConnProfAtmMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 3)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfAtmMemberGroup = tmnxConnProfAtmMemberGroup.setStatus('current')
if mibBuilder.loadTexts: tmnxConnProfAtmMemberGroup.setDescription('The group of objects supporting management of ATM connection profile members on Alcatel-Lucent SROS series systems.')
mibBuilder.exportSymbols("TIMETRA-CONN-PROF-MIB", tmnxConnV9v0Groups=tmnxConnV9v0Groups, tmnxConnProfNotifications=tmnxConnProfNotifications, tmnxConnProfConfigObjs=tmnxConnProfConfigObjs, tmnxConnProfAtmMemberGroup=tmnxConnProfAtmMemberGroup, tmnxConnProfAtmMemberRowStatus=tmnxConnProfAtmMemberRowStatus, tmnxConnProfAtmMemberEntry=tmnxConnProfAtmMemberEntry, tmnxConnProfAtmMemberTblLastChgd=tmnxConnProfAtmMemberTblLastChgd, tmnxConnProfVlanRange=tmnxConnProfVlanRange, TmnxConnProfId=TmnxConnProfId, tmnxConnProfGroup=tmnxConnProfGroup, tmnxConnProfNtfyPrefix=tmnxConnProfNtfyPrefix, tmnxConnProfAtmMemberTable=tmnxConnProfAtmMemberTable, PYSNMP_MODULE_ID=timetraConnProfMIBModule, tmnxConnProfObjs=tmnxConnProfObjs, tmnxConnProfAtmMemberEncapValue=tmnxConnProfAtmMemberEncapValue, tmnxConnProfConfigTimeStamps=tmnxConnProfConfigTimeStamps, timetraConnProfMIBModule=timetraConnProfMIBModule, tmnxConnProfDescription=tmnxConnProfDescription, TmnxConnProfVlanRanges=TmnxConnProfVlanRanges, tmnxConnProfGroups=tmnxConnProfGroups, tmnxConnProfLastChanged=tmnxConnProfLastChanged, tmnxConnProfConformance=tmnxConnProfConformance, tmnxConnProfTblLastChanged=tmnxConnProfTblLastChanged, tmnxConnProfCompliances=tmnxConnProfCompliances, tmnxConnProfRowStatus=tmnxConnProfRowStatus, tmnxConnProfEntry=tmnxConnProfEntry, tmnxConnProfTable=tmnxConnProfTable, tmnxConnProfV9v0Compliance=tmnxConnProfV9v0Compliance, tmnxConnProfId=tmnxConnProfId, tmnxConnProfTimeStampGroup=tmnxConnProfTimeStampGroup)
