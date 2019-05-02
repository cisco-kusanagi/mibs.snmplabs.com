#
# PySNMP MIB module MPLS-ID-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-ID-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:14:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
MplsNodeId, MplsIccId, MplsCcId, MplsGlobalId = mibBuilder.importSymbols("MPLS-TC-EXT-STD-MIB", "MplsNodeId", "MplsIccId", "MplsCcId", "MplsGlobalId")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Unsigned32, Counter32, MibIdentifier, ModuleIdentity, IpAddress, iso, Counter64, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Counter32", "MibIdentifier", "ModuleIdentity", "IpAddress", "iso", "Counter64", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsIdStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 18))
mplsIdStdMIB.setRevisions(('2015-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsIdStdMIB.setRevisionsDescriptions(('This MIB modules defines the MIB objects for MPLS-TP identifiers',))
if mibBuilder.loadTexts: mplsIdStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsIdStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsIdStdMIB.setContactInfo(' Venkatesan Mahalingam Dell Inc, 5450 Great America Parkway, Santa Clara, CA 95054, USA Email: venkat.mahalingams@gmail.com Kannan KV Sampath Redeem, India Email: kannankvs@gmail.com Sam Aldrin Huawei Technologies 2330 Central Express Way, Santa Clara, CA 95051, USA Email: aldrin.ietf@gmail.com Thomas D. Nadeau Email: tnadeau@lucidvision.com ')
if mibBuilder.loadTexts: mplsIdStdMIB.setDescription("This MIB module contains identifier object definitions for MPLS Traffic Engineering in transport networks. Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
mplsIdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 0))
mplsIdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 1))
mplsIdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2))
mplsIdGlobalId = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 1), MplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdGlobalId.setStatus('current')
if mibBuilder.loadTexts: mplsIdGlobalId.setDescription('This object allows the operator or service provider to assign a unique operator identifier, also called the MPLS-TP Global_ID. If this value is used in mplsTunnelExtNodeConfigGlobalId for mapping Global_ID::Node_ID with the local identifier, then this object value MUST NOT be changed.')
mplsIdNodeId = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 2), MplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdNodeId.setStatus('current')
if mibBuilder.loadTexts: mplsIdNodeId.setDescription('This object allows the operator or service provider to assign a unique MPLS-TP Node_ID. The Node_ID is assigned within the scope of the Global_ID/ICC_Operator_ID. If this value is used in mplsTunnelExtNodeConfigNodeId for mapping Global_ID::Node_ID with the local identifier, then this object value SHOULD NOT be changed. If this value is used in mplsTunnelExtNodeConfigNodeId for mapping ICC_Operator_ID::Node_ID with the local identifier, then this object value MUST NOT be changed.')
mplsIdCc = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 3), MplsCcId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdCc.setReference('MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3')
if mibBuilder.loadTexts: mplsIdCc.setStatus('current')
if mibBuilder.loadTexts: mplsIdCc.setDescription('This object allows the operator or service provider to assign a Country Code (CC) to the node. Global uniqueness of ICC is assured by concatenating the ICC with a Country Code (CC). If this value is used in mplsTunnelExtNodeConfigCcId for mapping ICC_Operator_ID::Node_ID with the local identifier, then this object value MUST NOT be changed.')
mplsIdIcc = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 4), MplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdIcc.setReference('MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3')
if mibBuilder.loadTexts: mplsIdIcc.setStatus('current')
if mibBuilder.loadTexts: mplsIdIcc.setDescription('This object allows the operator or service provider to assign a unique MPLS-TP ITU-T Carrier Code (ICC) to the node. Together, the CC and the ICC form the ICC_Operator_ID as CC::ICC. If this value is used in mplsTunnelExtNodeConfigIccId for mapping ICC_Operator_ID::Node_ID with the local identifier, then this object value MUST NOT be changed.')
mplsIdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1))
mplsIdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2))
mplsIdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 1)).setObjects(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"), ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdModuleFullCompliance = mplsIdModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsIdModuleFullCompliance.setDescription('Compliance statement for agents that provide full support of the MPLS-ID-STD-MIB module.')
mplsIdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 2)).setObjects(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"), ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdModuleReadOnlyCompliance = mplsIdModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsIdModuleReadOnlyCompliance.setDescription('Compliance statement for agents that only provide read-only support for the MPLS-ID-STD-MIB module.')
mplsIdIpOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 1)).setObjects(("MPLS-ID-STD-MIB", "mplsIdGlobalId"), ("MPLS-ID-STD-MIB", "mplsIdNodeId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdIpOperatorGroup = mplsIdIpOperatorGroup.setStatus('current')
if mibBuilder.loadTexts: mplsIdIpOperatorGroup.setDescription('The objects in this group are optional for an ICC-based node.')
mplsIdIccOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 2)).setObjects(("MPLS-ID-STD-MIB", "mplsIdNodeId"), ("MPLS-ID-STD-MIB", "mplsIdCc"), ("MPLS-ID-STD-MIB", "mplsIdIcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdIccOperatorGroup = mplsIdIccOperatorGroup.setStatus('current')
if mibBuilder.loadTexts: mplsIdIccOperatorGroup.setDescription('The objects in this group are optional for an IP-based node.')
mibBuilder.exportSymbols("MPLS-ID-STD-MIB", mplsIdStdMIB=mplsIdStdMIB, mplsIdCompliances=mplsIdCompliances, mplsIdGroups=mplsIdGroups, mplsIdCc=mplsIdCc, mplsIdObjects=mplsIdObjects, PYSNMP_MODULE_ID=mplsIdStdMIB, mplsIdIcc=mplsIdIcc, mplsIdModuleReadOnlyCompliance=mplsIdModuleReadOnlyCompliance, mplsIdIpOperatorGroup=mplsIdIpOperatorGroup, mplsIdNotifications=mplsIdNotifications, mplsIdGlobalId=mplsIdGlobalId, mplsIdNodeId=mplsIdNodeId, mplsIdModuleFullCompliance=mplsIdModuleFullCompliance, mplsIdConformance=mplsIdConformance, mplsIdIccOperatorGroup=mplsIdIccOperatorGroup)
