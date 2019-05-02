#
# PySNMP MIB module TRAPEZE-NETWORKS-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-CLUSTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, iso, Counter32, Unsigned32, Gauge32, IpAddress, Counter64, Integer32, MibIdentifier, NotificationType, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "iso", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "Counter64", "Integer32", "MibIdentifier", "NotificationType", "ObjectIdentity", "TimeTicks")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
TrpzApNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApNum")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzClusterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 21))
trpzClusterMib.setRevisions(('2011-02-24 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzClusterMib.setRevisionsDescriptions(('v1.0.1: Initial version, for 7.5 release',))
if mibBuilder.loadTexts: trpzClusterMib.setLastUpdated('201102240001Z')
if mibBuilder.loadTexts: trpzClusterMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzClusterMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzClusterMib.setDescription("Cluster objects for Trapeze Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent implementing this MIB; PAM = Primary AP Manager; SAM = Secondary AP Manager. Copyright 2010-2011 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
trpzClusterMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1))
trpzClusterApAssignmentTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1), )
if mibBuilder.loadTexts: trpzClusterApAssignmentTable.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignmentTable.setDescription('A table describing the AP manager assignments for the APs currently present and managed by the Cluster this AC is part of.')
trpzClusterApAssignmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignApNum"))
if mibBuilder.loadTexts: trpzClusterApAssignmentEntry.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignmentEntry.setDescription('Information about a particular AP assignment in this Cluster.')
trpzClusterApAssignApNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 1), TrpzApNum())
if mibBuilder.loadTexts: trpzClusterApAssignApNum.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignApNum.setDescription('The AP Number.')
trpzClusterApAssignPamIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignPamIp.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignPamIp.setDescription('The IP address of the assigned Primary AP Manager controller.')
trpzClusterApAssignSamIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignSamIp.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignSamIp.setDescription('The IP address of the assigned Secondary AP Manager controller. A value of 0.0.0.0 means this AP does not have an assigned SAM.')
trpzClusterApAssignConnectedToPam = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignConnectedToPam.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignConnectedToPam.setDescription('Indicates whether this AP is currently connected to its assigned Primary AP Manager controller.')
trpzClusterApAssignConnectedToSam = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignConnectedToSam.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignConnectedToSam.setDescription('Indicates whether this AP is currently connected to its assigned Secondary AP Manager controller.')
trpzClusterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2))
trpzClusterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 1))
trpzClusterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 2))
trpzClusterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignmentGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClusterCompliance = trpzClusterCompliance.setStatus('current')
if mibBuilder.loadTexts: trpzClusterCompliance.setDescription('The compliance statement for devices that implement Cluster MIB. This compliance statement is for releases 7.5 and greater of AC (wireless switch) software.')
trpzClusterApAssignmentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignPamIp"), ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignSamIp"), ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignConnectedToPam"), ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignConnectedToSam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClusterApAssignmentGroup = trpzClusterApAssignmentGroup.setStatus('current')
if mibBuilder.loadTexts: trpzClusterApAssignmentGroup.setDescription('Group of columnar objects implemented to provide Cluster AP Assignments info in releases 7.5 and greater.')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-CLUSTER-MIB", trpzClusterConformance=trpzClusterConformance, trpzClusterApAssignSamIp=trpzClusterApAssignSamIp, trpzClusterApAssignmentEntry=trpzClusterApAssignmentEntry, PYSNMP_MODULE_ID=trpzClusterMib, trpzClusterGroups=trpzClusterGroups, trpzClusterApAssignmentTable=trpzClusterApAssignmentTable, trpzClusterApAssignmentGroup=trpzClusterApAssignmentGroup, trpzClusterMibObjects=trpzClusterMibObjects, trpzClusterApAssignConnectedToPam=trpzClusterApAssignConnectedToPam, trpzClusterMib=trpzClusterMib, trpzClusterApAssignConnectedToSam=trpzClusterApAssignConnectedToSam, trpzClusterCompliance=trpzClusterCompliance, trpzClusterApAssignApNum=trpzClusterApAssignApNum, trpzClusterApAssignPamIp=trpzClusterApAssignPamIp, trpzClusterCompliances=trpzClusterCompliances)
