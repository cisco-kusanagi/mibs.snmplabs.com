#
# PySNMP MIB module CISCO-IETF-MPLS-ID-STD-03-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-MPLS-ID-STD-03-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:00:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
CMplsGlobalId, CMplsIccId, CMplsNodeId = mibBuilder.importSymbols("CISCO-MPLS-TC-EXT-STD-MIB", "CMplsGlobalId", "CMplsIccId", "CMplsNodeId")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, IpAddress, Gauge32, Bits, ObjectIdentity, Unsigned32, Integer32, Counter32, Counter64, iso, TimeTicks, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Gauge32", "Bits", "ObjectIdentity", "Unsigned32", "Integer32", "Counter32", "Counter64", "iso", "TimeTicks", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmplsIdStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 147))
cmplsIdStdMIB.setRevisions(('2012-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmplsIdStdMIB.setRevisionsDescriptions(('MPLS identifiers mib object extension',))
if mibBuilder.loadTexts: cmplsIdStdMIB.setLastUpdated('201206070000Z')
if mibBuilder.loadTexts: cmplsIdStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: cmplsIdStdMIB.setContactInfo('Venkatesan Mahalingam Dell Inc, 350 Holger way, San Jose, CA, USA Email: venkat.mahalingams@gmail.com Kannan KV Sampath Aricent, India Email: Kannan.Sampath@aricent.com Sam Aldrin Huawei Technologies 2330 Central Express Way, Santa Clara, CA 95051, USA Email: aldrin.ietf@gmail.com Thomas D. Nadeau Juniper Networks 10 Technology Park Drive, Westford, MA 01886 Email: tnadeau@juniper.net')
if mibBuilder.loadTexts: cmplsIdStdMIB.setDescription('Copyright (c) 2012 IETF Trust and the persons identified as the document authors. All rights reserved. This MIB module contains generic object definitions for MPLS Traffic Engineering in transport networks. This module is a cisco-ized version of the IETF draft: draft-ietf-mpls-tp-te-mib-03.')
cmplsIdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 0))
cmplsIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 1))
cmplsIdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2))
cmplsGlobalId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 1), CMplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsGlobalId.setReference('MPLS-TP Identifiers [RFC6370].')
if mibBuilder.loadTexts: cmplsGlobalId.setStatus('current')
if mibBuilder.loadTexts: cmplsGlobalId.setDescription('This object allows the administrator to assign a unique operator identifier also called MPLS-TP Global_ID.')
cmplsIcc = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 2), CMplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsIcc.setReference('MPLS-TP Identifiers [RFC6370].')
if mibBuilder.loadTexts: cmplsIcc.setStatus('current')
if mibBuilder.loadTexts: cmplsIcc.setDescription('This object allows the operator or service provider to assign a unique MPLS-TP ITU-T Carrier Code (ICC) to a network.')
cmplsNodeId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 3), CMplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeId.setReference('MPLS-TP Identifiers [RFC6370].')
if mibBuilder.loadTexts: cmplsNodeId.setStatus('current')
if mibBuilder.loadTexts: cmplsNodeId.setDescription('This object allows the operator or service provider to assign a unique MPLS-TP Node_ID. The Node_ID is assigned within the scope of the Global_ID.')
cmplsIdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1))
cmplsIdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2))
cmplsIdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleFullCompliance = cmplsIdModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsIdModuleFullCompliance.setDescription('Compliance statement for agents that provide full support the MPLS-ID-STD-MIB module.')
cmplsIdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 2)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleReadOnlyCompliance = cmplsIdModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsIdModuleReadOnlyCompliance.setDescription('Compliance statement for agents that provide full support the MPLS-ID-STD-MIB module.')
cmplsIdScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsGlobalId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsNodeId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdScalarGroup = cmplsIdScalarGroup.setStatus('current')
if mibBuilder.loadTexts: cmplsIdScalarGroup.setDescription('Scalar object needed to implement MPLS TP path.')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-ID-STD-03-MIB", cmplsIdGroups=cmplsIdGroups, PYSNMP_MODULE_ID=cmplsIdStdMIB, cmplsNodeId=cmplsNodeId, cmplsIcc=cmplsIcc, cmplsIdModuleFullCompliance=cmplsIdModuleFullCompliance, cmplsIdConformance=cmplsIdConformance, cmplsIdCompliances=cmplsIdCompliances, cmplsIdScalarGroup=cmplsIdScalarGroup, cmplsIdModuleReadOnlyCompliance=cmplsIdModuleReadOnlyCompliance, cmplsIdStdMIB=cmplsIdStdMIB, cmplsIdObjects=cmplsIdObjects, cmplsIdNotifications=cmplsIdNotifications, cmplsGlobalId=cmplsGlobalId)
