#
# PySNMP MIB module EQLISCSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EQLISCSI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:05:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
iscsiSessionStatsEntry, iscsiSessionAttributesEntry = mibBuilder.importSymbols("ISCSI-MIB", "iscsiSessionStatsEntry", "iscsiSessionAttributesEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Gauge32, TimeTicks, iso, ModuleIdentity, MibIdentifier, ObjectIdentity, Unsigned32, Bits, Opaque, experimental, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Gauge32", "TimeTicks", "iso", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Bits", "Opaque", "experimental", "Counter32", "enterprises")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
eqliscsiExtModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 11))
eqliscsiExtModule.setRevisions(('2002-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqliscsiExtModule.setRevisionsDescriptions(('Equallogic Inc augmented ISCSI MIB module Copyright (c) 2002-2009 by Dell, Inc. All rights reserved. This software may not be copied, disclosed, transferred, or used except in accordance with a license granted by Dell, Inc. This software embodies proprietary information and trade secrets of Dell, Inc. ',))
if mibBuilder.loadTexts: eqliscsiExtModule.setLastUpdated('201403121459Z')
if mibBuilder.loadTexts: eqliscsiExtModule.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: eqliscsiExtModule.setContactInfo('Contact: Customer Support Postal: Dell Inc 300 Innovative Way, Suite 301, Nashua, NH 03062 Tel: +1 603-579-9762 E-mail: US-NH-CS-TechnicalSupport@dell.com WEB: www.equallogic.com')
if mibBuilder.loadTexts: eqliscsiExtModule.setDescription('Equallogic Inc augmented ISCSI MIB module.')
eqliscsiExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 11, 1))
eqliscsiSessionStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1), )
if mibBuilder.loadTexts: eqliscsiSessionStatsTable.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSessionStatsTable.setDescription('A Dynamic list of general iSCSI traffic counters for each of the sessions present on the system.')
eqliscsiSessionStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1), )
iscsiSessionStatsEntry.registerAugmentions(("EQLISCSI-MIB", "eqliscsiSessionStatsEntry"))
eqliscsiSessionStatsEntry.setIndexNames(*iscsiSessionStatsEntry.getIndexNames())
if mibBuilder.loadTexts: eqliscsiSessionStatsEntry.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSessionStatsEntry.setDescription('An entry (row) containing general iSCSI traffic counters for a particular session.')
eqliscsiSsnErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnErrorCount.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSsnErrorCount.setDescription('The number of errors encountered since this session was established')
eqliscsiSsnTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnTimeUp.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSsnTimeUp.setDescription('The time in ticks that has elapsed since this session was first established with the iSCSI target')
eqliscsiSsnTotalDataTrnsfrd = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 3), Counter32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnTotalDataTrnsfrd.setStatus('deprecated')
if mibBuilder.loadTexts: eqliscsiSsnTotalDataTrnsfrd.setDescription('The amount of data transfered for this session in Kilobytes. This number is determined by the sum of the inbound and outbound traffic counters.')
eqliscsiNodeUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiNodeUuid.setStatus('current')
if mibBuilder.loadTexts: eqliscsiNodeUuid.setDescription('The UUID of the iscs')
eqliscsiSsnTotalDataTrnsfrd64 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 5), Counter64()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnTotalDataTrnsfrd64.setStatus('deprecated')
if mibBuilder.loadTexts: eqliscsiSsnTotalDataTrnsfrd64.setDescription('The amount of data transfered for this session in Kilobytes. This number is determined by the sum of the inbound and outbound traffic counters.')
eqliscsiSsnMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 6), Opaque().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnMembers.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSsnMembers.setDescription("List of eligible member id's. This is sizeof(uint32_t) * pss_max_num_grp_members defined in pss_constants.h")
eqliscsiSsnRouteStats = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 7), Opaque().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnRouteStats.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSsnRouteStats.setDescription('Array of the percentage of traffic being routed to each member. This is a 1 to 1 relationship to the Members array. This is sizeof(uint32_t) * pss_max_num_grp_members defined in pss_constants.h')
eqliscsiSsnLoadValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnLoadValue.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSsnLoadValue.setDescription('Calculated value of how busy this connection is. 0 is 100% busy, 100 is 0% busy')
eqliscsiSessionAttributesTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 11, 1, 2), )
if mibBuilder.loadTexts: eqliscsiSessionAttributesTable.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSessionAttributesTable.setDescription('EqualLogic-Dynamic A Dynamic list of general iSCSI connection attributes for connections present on the system.')
eqliscsiSessionAttributesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 11, 1, 2, 1), )
iscsiSessionAttributesEntry.registerAugmentions(("EQLISCSI-MIB", "eqliscsiSessionAttributesEntry"))
eqliscsiSessionAttributesEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())
if mibBuilder.loadTexts: eqliscsiSessionAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSessionAttributesEntry.setDescription('An entry (row) containing general iSCSI connection attributes.')
eqliscsiSessionAttributesType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("external", 1), ("syncrepl", 2), ("xcopy", 3), ("replica", 4))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSessionAttributesType.setStatus('current')
if mibBuilder.loadTexts: eqliscsiSessionAttributesType.setDescription('Describes the src initiator of the connection as external to the array group, or one of various connection types between group members.')
mibBuilder.exportSymbols("EQLISCSI-MIB", eqliscsiSessionStatsEntry=eqliscsiSessionStatsEntry, eqliscsiSessionAttributesType=eqliscsiSessionAttributesType, eqliscsiExtModule=eqliscsiExtModule, eqliscsiSsnMembers=eqliscsiSsnMembers, eqliscsiSsnTimeUp=eqliscsiSsnTimeUp, eqliscsiNodeUuid=eqliscsiNodeUuid, eqliscsiSsnErrorCount=eqliscsiSsnErrorCount, eqliscsiSessionAttributesTable=eqliscsiSessionAttributesTable, eqliscsiSsnTotalDataTrnsfrd=eqliscsiSsnTotalDataTrnsfrd, eqliscsiSsnRouteStats=eqliscsiSsnRouteStats, eqliscsiSessionStatsTable=eqliscsiSessionStatsTable, eqliscsiExtObjects=eqliscsiExtObjects, eqliscsiSsnLoadValue=eqliscsiSsnLoadValue, eqliscsiSessionAttributesEntry=eqliscsiSessionAttributesEntry, eqliscsiSsnTotalDataTrnsfrd64=eqliscsiSsnTotalDataTrnsfrd64, PYSNMP_MODULE_ID=eqliscsiExtModule)
